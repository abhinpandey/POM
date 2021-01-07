import time


import pytest
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        homePage=HomePage(self.driver)
        # Search_btn = self.driver.find_element_by_xpath("//input[@type='search']")
        # Search_btn.send_keys("ber")
        time.sleep(4)
        count = self.driver.find_elements_by_xpath("//div[@class='product']")
        time.sleep(4)
        counts = len(count)
        assert counts == 3

        Add_to_cart = self.driver.find_elements_by_xpath("//div[@class='product-action']/button")
        for btn in Add_to_cart:
            btn.click()
        cart = self.driver.find_element_by_xpath("//a[@class='cart-icon']/img")
        cart.click()

        proceed_to_checkout = self.driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']")
        proceed_to_checkout.click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//input[@class='promoCode']").send_keys("rahulshettyacademy")

        time.sleep(6)
        self.driver.find_element_by_class_name("promoBtn").click()

        time.sleep(6)
        promo_inf0 = self.driver.find_element_by_class_name("promoInfo")
        print(promo_inf0.text)
