"""
This helps users get started with their personal cookie pickle file generation.
"""

import pickle
from time import sleep
import selenium.webdriver as webdriver

def init():
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        COOKIE_URL = 'https://www.unrealengine.com/en-US/'
        DRIVER     = webdriver.Chrome(chrome_options=options)
        DRIVER.maximize_window()
        DRIVER.get(COOKIE_URL)
        print('Cookie Backer: Loading complete.')
        print('Please log into your account.')
        input("when you're logged in, press ENTER here to finish backing the cookies.")
        pickle.dump(DRIVER.get_cookies() , open("./cookies/cookies.pkl","wb"))
        print('Cookies are out of the oven and ready to be fed to the JSON generator!')
        print('Please head over to the installation folder and run "Generate_JSON.exe"')
        input('You can close this window now.')