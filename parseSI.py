import json
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import json
import time
from selenium import webdriver
import argparse
import scrapy
import pandas as pd
from tqdm import tqdm


class parseHTML():
    
    def readJson(self, text_file):
        lst = []
        for line in open(text_file, 'r'):
            lst.append(json.loads(line))
        return lst
    
    def get_dic(self, ur):
        soup = BeautifulSoup(ur['body'], 'lxml')
        body = soup.body
        dic = {}
        dic['url'] = ur['url']
        company_info = body.find('div', {'class':"company-name"})
        if len(company_info.findAll('h6')) ==2:
            dic['Company name'] = company_info.find('p').text.strip()
        if company_info.find('span', {'class':'orglevel'}) != None:
            dic['Engagement level'] = company_info.find('span', {'class':'orglevel'}).text.strip()
        if company_info.find('span',{'class':'orglevel active-since'}) != None:
            dic['Active on Portal Since'] = company_info.find('span',{'class':'orglevel active-since'}).text.strip()
        if company_info.find('a', {'class':'website'}) != None:
            dic['website'] = company_info.find('a', {'class':'website'}).text.strip()
        if body.find('div',{'class':'read margin-t20'}) != None:
            dic['text'] = body.find('div',{'class':'read margin-t20'}).text.strip().encode('ascii', 'ignore').decode("utf-8")
        attributes = body.findAll('span', {'class':'content'})
        for i,atr in enumerate(attributes):
            if i ==0:
                dic['Stage'] = atr.text.strip()
            if i ==1:
                dic['FOCUS INDUSTRY'] = atr.text.strip()
            if i ==2:
                dic['FOCUS SECTOR'] = atr.text.strip()
            if i ==3:
                dic['SERVICE AREA(S)'] = atr.text.strip()
            if i ==4:
                dic['LOCATION'] = atr.text.strip()
            if i ==5:
                dic['NO OF ACTIVE YEARS'] = atr.text.strip()

        return dic

    def get_dataframe(self, dump_list):
        lst = []
        for i in tqdm(dump_list):
            lst.append(self.get_dic(i))
        df= pd.DataFrame(lst)
        df = df.set_index('Company name')
        return df
    
    def save_to_file(self, df, filename):
        df.to_csv(filename)
    
        
    def main(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--inputFile",
                            default=None,
                            type=str,
                            required=True,
                            help="file containing html dump")

        parser.add_argument("--outputFile",
                            default=None,
                            type=str,
                            required=True,
                            help="name and location of the file")
        
        args = parser.parse_args()
        dump_list = self.readJson('test_dump.json')
        df = self.get_dataframe(dump_list[0]['data'])
        self.save_to_file(df, args.outputFile)

if __name__ == "__main__":
    func = parseHTML()
    func.main()
        
        
    
