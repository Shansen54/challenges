import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Challenge1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../venv/chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge2(self):
        self.driver.get("https://www.copart.com")
        self.assertIn('Copart', self.driver.title)
        searchbox = self.driver.find_element_by_id('input-search')
        searchbox.send_keys("exotics")
        searchbox.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(5)
        makeItem = self.driver.find_element_by_xpath("//tr[1]//td[5]//span[1]")
        self.assertIn('PORSCHE', makeItem.text)


if __name__ == '__main__':
    unittest.main()
