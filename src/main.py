import pickle
import selenium.webdriver as webdriver
import time
from bs4 import BeautifulSoup
from VaultItemInfoRetriever import Retriever



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

    def navigate_to_next_page(self):
        time.sleep(2)
        pagination_button = self.DRIVER.find_element_by_class_name('rc-pagination-next').find_element_by_tag_name('a') # li element. <a> is nested as immediate child.
        active_page_number = self.DRIVER.find_element_by_class_name('rc-pagination-item-active').find_element_by_tag_name('a').get_attribute('innerHTML')
        print('API_Feeder: active page:', active_page_number)
        pagination_button.click()
        time.sleep(1)
    

feeder = API_Feeder()
feed   = feeder.get_current_feed()
feeder.next_page()
feed   = feeder.get_current_feed()
retriever = Retriever()
html_source = feed
data = retriever.retrieve(html_source)
print(data)

# # Vault Page Traversal *******************************************************************************
# for i in range(0, 20):
#     
# # Vault Page Traversal *******************************************************************************



























def navigate_to_vault():
    """
    Navigate to the vault webpage
    """
    pass

def __inspect_cookies():
    DRIVER.get(COOKIE_URL)
    for k in DRIVER.get_cookies():
        print(k)

def save_cookies():
    DRIVER.get(COOKIE_URL)
    pickle.dump( DRIVER.get_cookies() , open("cookies.pkl","wb"))