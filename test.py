import os
import sys
from unittest import TestCase

from selenium import webdriver

'''
NW.js Selenium test suite example
'''
class TestWindow(TestCase):

    '''
    Setup Selenium driver.
    '''
    def setUp(self):

        # Set NW.js project root to present working directory
        # NW.js project requires an index.html and package.json
        pwd = os.path.dirname(os.path.abspath(__file__))
        sys.path.append(pwd)

        # We are using the nw node module to download NW.js
        # Change the path as necessary
        chromedriver_path = "./node_modules/nw/nwjs/chromedriver"

        if sys.platform == "win":
            chromedriver_path += ".exe"
        
        options = webdriver.ChromeOptions()
        # File path to NW.js project
        options.add_argument("nwapp=" + pwd)
        # Useful if running in CI
        options.add_argument("headless=new")

        # Pass file path of NW.js chromedriver to ServiceBuilder
        service = webdriver.ChromeService(executable_path=chromedriver_path)

        # Create a new session using the Chromium options and DriverService defined above.
        self.driver = webdriver.Chrome(service=service, options=options)

    '''
    Get text via element's id and assert it is equal.
    '''
    def test_text_by_id(self):
        try:
            text_element = self.driver.find_element(webdriver.common.by.By.ID, 'test')
            text = text_element.get_attribute('innerText')
            assert(text == "Hello, World!")
        except:
            assert False

    '''
    Quit Selenium driver.
    '''
    def tearDown(self):
        self.driver.quit()
