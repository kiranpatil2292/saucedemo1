import os

from pageObjects.CartPage import CartPage
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen


class Test_CheckOut():
    baseURL = " https://www.saucedemo.com/"
    logger = LogGen.loggen()

    def test_Checkout_WithNoProductToCart(self, setup):
        self.logger.info("******* Starting test_001_Checkout_With_valid_credential **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername("standard_user")
        self.lp.setPassword("secret_sauce")
        self.lp.clickLogin()
        self.cp = CartPage(self.driver)
        self.cp.clickCartLink()
        self.cp.clickCheckOut()

        self.targetpage = self.cp.conFroMsgCheckout()
        if self.targetpage == "Checkout: Your Information":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test001_No_product_to_cart")
            assert False
