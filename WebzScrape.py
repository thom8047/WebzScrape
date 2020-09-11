# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 11:03:08 2020

@author: Kyle


import requests                     # | REQUESTS Module, meant for pulling requests
import csv                          # | CSV package for exporting data(Switch to pandas)
import re                           # | RE Module, meant for uniting bytes and strings(visa versa)
from bs4 import BeautifulSoup       # | Beautiful Soup for organizing JSON data scraped
from selenium import webdriver      # | 
import time                         # |
import html                         # |

amazonlink = "http://www.amazon.com"

class AmazonClient:
    
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:/Users/Kyle/Downloads/chromedriver_win32/chromedriver')
        #self.driver.get(amazonlink)
        
    def printInfo(self):
        page = requests.get(amazonlink)
        soup = BeautifulSoup(page.content, 'lxml')
        print(soup)
        
def main():
    client = AmazonClient()
    client.printInfo()
    try:
        pass
    except:
        print('Error')

if __name__ == '__main__':
    main()
"""

import time
import textwrap; wrapper = textwrap.TextWrapper(width=20)
import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import html

def wait(n):
    time.sleep(n)
    return True
    
def get_user_input():
    search = input('\nWhat would you like to search on AMAZON: ')
    return search.capitalize()
def get_user_input_first():
    search = input('To EXIT search API, press enter when prompted for new search.\nWhat would you like to search on AMAZON: ')
    return search
def wrap_text(text):
    return wrapper.fill(text)



##      Make class

class Client:
    def __init__(self):
        pass
    
    def write_data(self, data):
        return json.dumps(data, indent="    ")
        
    def get_data(self, page_source, driver):
        soup = BeautifulSoup(page_source, 'lxml')
        # get text

        data = []
        try:
            bestsellers = soup.findAll('a', {'class': 'a-link-normal'})
            if len(bestsellers): print(len(bestsellers)); href = bestsellers[0].get('href'); data.append(
                {
                    'best_sellers_page': href       # Should give the best sellers webpage if it exists.
                }
                )
        except:
            print('...no best sellers page found\n')
        
        for names in soup.findAll('div', {'class': 'a-section a-spacing-medium'}):
            name = names.find('span', {'class': 'a-text-normal'})
            price = names.find('span', {'class': 'a-offscreen'})
            if name:
                name = name.get_text()
                
                if price:
                    price = price.get_text()
                    price = price[1:]
                    
                    element = {
                        'name': name,
                        'price': price
                    }
                    data.append(element)
        
        return data
        
    
    def get_search(self, url, search):
        driver = webdriver.Chrome(executable_path='C:/bin/chromedriver')
        wait(2)
        driver.get(url)
        #   content = driver.page_source
        
        search_bar, submit = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]'), driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input')
        search_bar.send_keys(search)
        # HAD TO SWITCH EXCECUTION FOR CLICK DUE TO CLICK INTERCEPTION
        submit.submit()
        wait(2)
        
        data = self.get_data(driver.page_source, driver)
        
        driver.close()
        
        return data
            

if __name__ == '__main__':
    link = 'https://www.amazon.com/'
    client = Client()
    search = get_user_input_first()
    
    while search:
        data = client.get_search(link, search)
        jsonData = client.write_data(data)
        
        #text = ''
        
        lowest, highest = [10000.0, ''], [0, '']
        for dic in data:
            if 'price' in dic:
                if float(dic['price']) < lowest[0]:
                    lowest[0] = float(dic['price']); lowest[1] = dic['name']
            else:
                pass
        
        print(f'\nLowest Priced {search} is: {lowest[0]}; {lowest[1]}\n', jsonData)
        
        search = get_user_input() #     To continue loop
    else:
        print('Thank you for using automated parser.')
