import requests
from bs4 import BeautifulSoup


page = requests.get("https://www.nzz.ch/international/krieg-gegen-die-ukraine")
soup = BeautifulSoup(page.content, "html.parser")

def find_news_articles():
    all_news_articles = []
    all_spans = soup.findAll('span', {'class':'teaser__title-name'})
    for span in all_spans:
        all_news_articles.append(span.get_text())
    return all_news_articles


def format_output():
    output_lines = []
    news_articles = find_news_articles ()
    for i in range(len(news_articles)):
        output = news_articles [i] + '\n'
        output_lines.append(output)
    return output_lines



def save_to_file():
    output = format_output()
    with open("data.xls", "a+") as file:
        file.writelines(output)
        file.close()
        print ("file created successfuly")

save_to_file()
