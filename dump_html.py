import json
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import json
import time
from selenium import webdriver
import argparse
import scrapy
from progressbar import *


class dumpHTML():
    
    def getrl(self, url):
        path = r'/Users/umangsaraf/Downloads/chromedriver'
        dic = {}
        driver = webdriver.Chrome(executable_path = path)
        driver.get(url)
        time.sleep(5)
        selector = scrapy.Selector(text = driver.page_source)
        driver.quit()
        dic['url']  = url
        dic['body'] = selector.css("*").get()
        dic['title']  = selector.css('title::text').get()
        return dic

    def dump(self, list_links, file_name):
        with open(file_name, "w") as f:
            for link in list_links:
                f.write(str(link) +"\n")
                
    def json_dump(self, filename, dumpList):
        with open(filename, 'w') as outfile:
            json.dump(dumpList, outfile)
            
    def append(self, list_links, file_name):
        with open(file_name, "a") as f:
            for link in list_links:
                f.write(str(link) +"\n")
                
    def read(self, text_file):
        lst = []
        with open(text_file, "r") as f:
            for line in f:
                lst.append(line.strip())
        return lst
    
    
    
    def main(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--inputFile",
                            default=None,
                            type=str,
                            required=True,
                            help="file containing all links of websites needed to be scraped")

        parser.add_argument("--outputFile",
                            default=None,
                            type=str,
                            required=True,
                            help="name and location of the file")
        
        args = parser.parse_args()
        all_the_links = self.read(args.inputFile)
        dumped_html = {}
        dumped_html['data'] = []
        widgets = ['Test: ', Percentage(), ' ', Bar(marker='0',left='[',right=']'),
           ' ', ETA(), ' ', Timer()] #see docs for other options

        pbar = ProgressBar(widgets=widgets, maxval=500)
        pbar.start()


        for link in pbar(range(len(all_the_links))):
            html = self.getrl(all_the_links[link])
            dumped_html['data'].append(html)
            pbar.update(link)
        pbar.finish()
        self.json_dump(args.outputFile, dumped_html)
        
if __name__ == "__main__":
    func = dumpHTML()
    func.main()
    
