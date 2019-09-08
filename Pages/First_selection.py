from selenium.webdriver.common.by import By
import unittest

class First_selection:
    def __init__(self, myDriver):
        self.driver = myDriver
        self.result_num = (By.CLASS_NAME, 'srp-controls__count-heading')
        self.products_name = (By.CLASS_NAME, 's-item__title')
        self.products_price = (By.CLASS_NAME, 's-item__price')

    def get_amount(self):
        number = (self.driver.find_element(*self.result_num).text)
        print('The amount of shoes PUMA size 10 is ' , number)

    def test_order(self):
        list_prices = self.driver.find_elements(*self.products_price)
        list_prices_num = []
        for i in range(5):
            x = float(list_prices[i].text[3:])
            list_prices_num.append(x)

        tc = unittest.TestCase('__init__')
        tc.assertTrue (list_prices_num[0] <= list_prices_num[1] <= list_prices_num[2] <= list_prices_num[3] <= list_prices_num[4])

        if (list_prices_num[0] <= list_prices_num[1] <= list_prices_num[2] <= list_prices_num[3] <= list_prices_num[4]):
            print('\n','The sort option Precio + Envío: más bajo primero is working as expected')

    def get_info_asc(self):
        list_names = self.driver.find_elements(*self.products_name)
        list_prices = self.driver.find_elements(*self.products_price)
        print('\n', 'Products ordered by price, ascendant')
        for i in range(5):
            print(list_prices[i].text, list_names[i+1].text)
