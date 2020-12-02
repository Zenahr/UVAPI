import pickle
import selenium.webdriver as webdriver
import time
from bs4 import BeautifulSoup
from VaultItemInfoRetriever import Retriever
import json


class API_Feeder:
    def __init__(self):
        self.__current_feed = None # Current HTML source for bs4
        options    = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        # options.add_argument('--headless') # TODO: Add in API prod code
        self.COOKIE_URL = 'https://www.unrealengine.com/en-US/'
        self.VAULT_URL  = 'https://www.unrealengine.com/marketplace/en-US/vault'
        self.DRIVER     = webdriver.Chrome(chrome_options=options)
        self.DRIVER.maximize_window()
        self.cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in self.cookies:
            self.DRIVER.add_cookie(cookie)
    
    def get_current_feed(self):
        return self.DRIVER.page_source

    def next_page(self):
        time.sleep(2)
        pagination_button = self.DRIVER.find_element_by_class_name('rc-pagination-next').find_element_by_tag_name('a') # li element. <a> is nested as immediate child.
        active_page_number = self.DRIVER.find_element_by_class_name('rc-pagination-item-active').find_element_by_tag_name('a').get_attribute('innerHTML')
        print('API_Feeder: active page:', active_page_number)
        pagination_button.click()
        time.sleep(1)

    def generate_API_JSON_feed(self):
        """
        Summary:
            Generate JSON file containing all data for all vault items

        returns:
            JSON
        """
        retriever = Retriever()
        data = []
        for i in range(0, 20):
            data.append(retriever.retrieve(self.get_current_feed))
            self.next_page()
            print('API Feeder: generated JSON from webpage')
        print('API Feeder: Finished generating JSON objects')
        return json.dump(data)


    def __inspect_cookies(self):
        self.DRIVER.get(self.COOKIE_URL)
        for k in self.DRIVER.get_cookies():
            print(k)

    def __save_cookies(self):
        self.DRIVER.get(self.COOKIE_URL)
        pickle.dump( self.DRIVER.get_cookies() , open("cookies.pkl","wb"))