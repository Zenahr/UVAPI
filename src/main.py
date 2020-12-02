import pickle
import selenium.webdriver as webdriver
import time

# Init *******************************************************************************
options    = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
# options.add_argument('--headless') # TODO: Add in API prod code
COOKIE_URL = 'https://www.unrealengine.com/en-US/'
VAULT_URL  = 'https://www.unrealengine.com/marketplace/en-US/vault'
DRIVER     = webdriver.Chrome(chrome_options=options)
DRIVER.maximize_window()
# Init *******************************************************************************

# Run *******************************************************************************
DRIVER.get(COOKIE_URL)
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    DRIVER.add_cookie(cookie)
DRIVER.get(VAULT_URL)
page_source = DRIVER.page_source

# # Vault Page Traversal *******************************************************************************
# for i in range(0, 20):
#     time.sleep(2)
#     pagination_button = DRIVER.find_element_by_class_name('rc-pagination-next').find_element_by_tag_name('a') # li element. <a> is nested as immediate child.
#     active_page_number = DRIVER.find_element_by_class_name('rc-pagination-item-active').find_element_by_tag_name('a').get_attribute('innerHTML')
#     print('LOG: active page:', active_page_number)
#     # pagination_button.location_once_scrolled_into_view
#     pagination_button.click()
#     time.sleep(1)
#     page_source = DRIVER.page_source
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