from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains

class Home():

    def __init__(self, myDriver):
        self.driver = myDriver
        self.search_box = (By.ID, 'gh-ac')
        self.search_button = (By.ID, "gh-btn")
        self.select_brand = (By.XPATH, "//span[contains(@class, 'cbx x-refine__multi-select-cbx') and text() = 'adidas']")
        self.select_size = (By.XPATH, "//span[contains(@class, 'cbx x-refine__multi-select-cbx') and text() = '10']")
        self.result_num = (By.CLASS_NAME, 'srp-controls__count-heading')
        self.sort_op = (By.ID, 'w9')
        self.sort_price_as = (By.XPATH,"//a[contains(.,'Precio + Envío: más bajo primero')]")
        self.sort_price_desc = (By.XPATH, "//a[contains(.,'Precio + Envío: más bajo primero')]")
        self.products_name  = (By.CLASS_NAME, 's-item__title')
        self.products_price = (By.CLASS_NAME, 's-item__price')

    def search_filter_products(self, object):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.search_box).send_keys(object)
        self.driver.find_element(*self.search_button).click()
        self.driver.implicitly_wait(5)

        # element = self.driver.find_element_by_id("//span[contains(@class, 'cbx x-refine__multi-select-cbx') and text() = 'PUMA']")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()

        self.driver.find_element(*self.select_brand).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.select_size).click()

    def sort_products(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.sort_op).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.sort_op).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.sort_price_as).click()
        self.driver.implicitly_wait(5)

    def re_sort_products(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.sort_op).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.sort_op).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.sort_price_desc).click()
        self.driver.implicitly_wait(5)





