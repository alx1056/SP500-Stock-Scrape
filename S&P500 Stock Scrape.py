# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
#imports all modules/packages needed for analysis
import requests
from bs4 import BeautifulSoup
import re
import datetime
import pandas as pd
import webbrowser


# %%
#picking the city/state/zip you want to search from within
state = 'NC'
city = 'Charlotte'
zipcd = '28201'

#URL reference
link = 'https://www.kbb.com/cars-for-sale/used/'+state+'-'+city+'-'+zipcd+'?dma=&vehicleStyleCodes=SUVCROSS&searchRadius=0&isNewSearch=true&marketExtension=include&showAccelerateBanner=false&sortBy=relevance&numRecords=50'

#declaring page variable to scrape
page = requests.get(link)


# %%
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC 

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

DRIVER_PATH = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=chrome_options)
driver.get(link)

#search = driver.find_element_by_name("q")

#search.send_keys("scraping")
#search.send_keys(Keys.RETURN)


try: 
#locate search results 
    search_results = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CLASS_NAME, "col-xs-12 col-md-9")))
    #EC.presence_of_element_located((By.CLASS_NAME, "rpBJOHq2PR60pnwJlUyP0")) 
    #scrape posts' headings 
    #posts = search_results.find_elements_by_css_selector("h3._eYtD2XCVieq6emjKBH3m")
    posts = search_results.find_elements_by_css_selector("div.inventory-listing-body padding-top-3 padding-right-3 margin-bottom-2") 
    for post in posts: 
        header = post.find_element_by_tag_name("div") 
        print(header.text) 
finally: 
    #quit browser
    print("", end="")
    print("", end="")
    print("done")


