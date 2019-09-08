from Pages.Home import *
from Pages.First_selection import *
from Pages.Second_selection import *
import unittest

class TestsBl(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('https://www.ebay.com/')
        self.home = Home(self.driver)
        self.first_selection = First_selection(self.driver)
        self.second_selection = Second_selection(self.driver)

    def test_ebay(self):
        self.home.search_filter_products('shoes')
        self.first_selection.get_amount()
        self.home.sort_products()
        self.first_selection.test_order()
        self.first_selection.get_info_asc()
        self.home.re_sort_products()
        self.second_selection.get_info_desc()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

