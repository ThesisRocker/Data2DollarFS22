import scrapy
import csv

item_link = ''

def getitem_csv(filename, column_index, ignore_header=True):
    tags = []
    with open('galaxuslive.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for (i, row) in enumerate(reader):
            tags.append(row[column_index])
    return tags

class GetdatasSpider(scrapy.Spider):
    name = 'getdatas'
    allowed_domains = ['www.galaxus.ch']
    start_urls = getitem_csv("", 1, True)

    def parse(self, response):

        single_etikette = \
            response.xpath('//*[@class="sc-1pqr3io-0 iKiIIZ"]'
                           )

        for etikette in single_etikette:
            item_name = \
                etikette.xpath('//*[@class="sc-jqo5ci-1 enyGfm"]/text()'
                               ).extract()
            preis = \
                etikette.xpath('//*[@class="sc-1aeovxo-1 gvrGle"]/text()'
                               ).extract()
            warengruppe = \
                etikette.xpath('//*[@class="sc-1xxwfxa-0 ermtyO sc-4cfuhz-4 kaeDTE"]/text()'
                               ).extract()
            bewertungen = \
                etikette.xpath('//*[@class="sc-oxgatm-2 doWVQv"]/text()'
                               ).extract()
            lagermenge = \
                etikette.xpath('//*[@class="sc-1bt7pq0-1 dAbjGG"]/text()'
                               ).extract()
            herstellername = \
                etikette.xpath('//*[@class="sc-1xxwfxa-0 ermtyO"]/text()'
                               ).extract()
            item_page = \
                etikette.xpath('/html/head/link[1]/@href'
                              ).get()

        yield {
            'Produkt': item_name,
            'Preis': preis,
            'Warengruppe': warengruppe,
            'Bewertungen': bewertungen,
            'Lagermenge': lagermenge,
            'Hersteller': herstellername,
            'Website': item_page,
            }
