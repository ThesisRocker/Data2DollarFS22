from urllib.parse import urljoin
import scrapy


class NumbersSpider(scrapy.Spider):
    name = 'numbers'
    allowed_domains = ['local.ch']
    # Start URL for the Gemeinde "Brügg BE"
    start_urls = ['https://www.local.ch/fr/q?what=&where=Br%C3%BCgg+BE&rid=nqNz&slot=tel']

    def parse(self, response):
        # Identify xpath with all the relevant data which we can iterate over
        containers = response.xpath(
            "//*[@class='js-entry-card-container row lui-margin-vertical-xs lui-sm-margin-vertical-m']")

        # Iterate over all containers to extract information
        for container in containers:
            # Try to extract the information from the container. If one operation fails, continue
            try:
                # Extract name of contact
                name = container.xpath(".//*[@class='lui-margin-vertical-zero card-info-title']/text()").extract_first()
                # Extract address of contact
                adresse = container.xpath(".//*[@class='card-info-address']/span/text()").extract_first()
                # Split address into multiple components, creating a list
                split = adresse.split(",",1)
                # The road is the first component of the list
                strasse = split[0]
                # Make a no_space version of the address to make matching with other datasets easier
                strasse_no_space = strasse.replace(" ", "")
                # The location is the second part of the list
                ort = split[1]
                # The ZIP code (PLZ) are the first 4 digits of the location
                plz = ort[1:5]
                # The name of the location is folliwng the ZIP code
                name_ort = ort[6:]
                """ The number is stored in various locations and is sometimes hidden behind a button on the website.
                    To make sure the number is retrieved, all locations of numbers are searched for."""
                # Extract number from path behind button (hidden-xs)
                nummer = container.xpath('.//*[@class="hidden-xs"]/text()').extract_first()

                # If the number was not hidden, extract the number from the second placeholder for numbers
                if nummer == None:
                    nummer = container.xpath(
                        ".//*[@class='js-gtm-event js-kpi-event action-button text-center hidden-xs "
                        "hidden-sm hidden-print action-button-primary']/@data-overlay-label").extract()
                    nummer = nummer[0]

                else:
                    # Since number in hidden placeholder is placed between ' ', remove those
                    nummer = nummer[1:-1]

                # Extract email from path
                email = container.xpath(".//*[@class='js-gtm-event js-kpi-event action-button text-center "
                                        "hidden-xs hidden-sm action-button-default']"
                                        "/span[@class='visible-print']/text()").extract_first()

                # Extract website from path
                website = container.xpath(".//*[@class='js-gtm-event js-kpi-event action-button "
                                          "text-center action-button-default']"
                                          "/span[@class='visible-print']/text()").extract_first()

                # Since name is placed between ' ', remove them
                if name != None:
                    name = name[1:-1]

                # Yield all the obtained results into csv
                yield {'Name': name,
                       'Strasse': strasse,
                       'Strasse_no_space': strasse_no_space,
                       'PlZ': plz,
                       'Ort': name_ort,
                       'Tel': nummer,
                       'E-Mail': email,
                       "Webseite": website}

            # If one of the operation was unsuccessful, it means that something is wrong and we simply continue
            # This happened only about 20 times for 1'000 results
            except:
                continue

        # Continue to the next page by extracting the next page in the xpath and create new request
        next_page = response.xpath("//li/a[@rel='next'][@class='pagination-link']/@href").extract_first()
        print(next_page) #Only to keep an overview of progress when scraping
        # If next page exists, scrape the next page
        if next_page is not None:
            # join base url with extracted path to create new request
            yield scrapy.Request(urljoin("https://www.local.ch", next_page))