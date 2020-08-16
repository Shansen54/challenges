import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../venv/chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge3(self):
        self.driver.get("https://www.copart.com")
        self.assertIn('Copart', self.driver.title)


if __name__ == '__main__':
    unittest.main()
