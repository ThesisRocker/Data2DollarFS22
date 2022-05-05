#!/usr/bin/python
# -*- coding: utf-8 -*-
# Import Bibliotheken

import scrapy

from scrapy.selector import Selector

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

from time import sleep
from datetime import datetime

import os
opts = Options()

# Spider Template


class GetlinksSpider(scrapy.Spider):

    name = 'getlinks'
    allowed_domains = ['www.galaxus.ch']
    start_urls = ['https://www.galaxus.ch']

    # Parse-Methode

    def parse(self, response):
        url = 'https://www.galaxus.ch/de/Wiki/2736'
        chrome_options = Options()
        self.driver = \
            webdriver.Chrome(executable_path='/Applications/chromedriver'
                             , options=chrome_options)
        self.driver.get(url)
        self.driver.delete_all_cookies()
        sleep(5)

        item_link = ''

        #Dauerschleife

        while True:
            add_item, item_link, item_text = self.getNexSoldItem(item_link)
            print("scraped item: " + str(add_item) + ", link: " + item_link + "content: " + item_text)
            #Daten für csv-File bereitstellen
            if add_item:
                writetofile(str(add_item),item_link, item_text)
            sleep(1)

        self.driver.close()

    #Definition xpath für Link und Text

    def getNexSoldItem(self, item_link_old):
        try:
            item_link = self.driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div[1]/aside/section[3]/div/div/div/div[3]/div/a').get_attribute('href')
            item_text = self.driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div[1]/aside/section[3]/div/div/div/div[3]/div/div[2]/span').get_attribute("textContent").lower()

            add_item = 'bestellt' in item_text and (item_link != item_link_old)

            return (add_item, item_link, item_text)
        except:
            print("Error item")
            return (False, item_link_old, "")


# csv-File schreiben

def writetofile(add_item, item_link, item_text):
    now = datetime.now()
    filename = 'scrapeddata-' + now.strftime('%Y-%m-%d') + '.csv'
    if os.path.exists(filename) == False:
        f = open(filename, 'a')
        f.write('add_item,item_link,item_time,item_text\n')
        f.close()

    f = open(filename, 'a')
    f.write(add_item + ',' + item_link + ','
            + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ','
            + item_text + '\n')
    f.close()
