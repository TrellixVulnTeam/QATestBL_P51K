from selenium.webdriver.common.by import By

class Second_selection:
    def __init__(self, myDriver):
        self.driver = myDriver
        self.products_name = (By.CLASS_NAME, 's-item__title')
        self.products_price = (By.CLASS_NAME, 's-item__price')

    def get_info_desc(self):
        list_names = self.driver.find_elements(*self.products_name)
        list_prices = self.driver.find_elements(*self.products_price)

        print('\n','Products ordered by price, descendant')
        for i in range(5):
            print(list_prices[i].text, list_names[i+1].text)
