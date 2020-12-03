import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../venv/chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge3(self):
        self.driver.get("https://www.copart.com")
        self.assertIn('Copart', self.driver.title)
        driver_wait = WebDriverWait(self.driver, 20)

        vehicles = self.driver.find_elements_by_css_selector("#tabTrending > div > div > div > ul > li > a")
        for vehicle in vehicles:
            print( str(vehicle.get_attribute('title')) + str(vehicle.get_attribute('text')) + " - " + str(vehicle.get_attribute('href')))


if __name__ == '__main__':
    unittest.main()
