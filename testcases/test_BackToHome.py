import os

import pytest

from utilities.customLogger import LogGen
from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.LoginPage import LoginPage
from pageObjects.CartPage import CartPage


class BackToHomePage():
    baseURL = " https://www.saucedemo.com/"
    logger = LogGen.loggen()

    def test_Back_To_ProductPage(self, setup):
        self.logger.info("****test_Back_To_HomePage_From_Success_OrderPage*****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername("standard_user")
        self.lp.setPassword("secret_sauce")
        self.lp.clickLogin()
        self.cp = CartPage(self.driver)
        self.cp.clickBoltTshirtPd()
        self.cp.clickCartAddBoltTshirt()
        self.cp.clickButBack()
        self.cp.clickBikeLightPd()
        self.cp.clickCartAddBackLight()
        self.cp.clickCartLink()
        self.cp.clickContShop()
        self.cp.clickSacLabPd()
        self.cp.clickAddCartSacLabPd()
        self.cp.clickCartLink()
        self.cp.clickCheckOut()
        self.co = CheckOutPage(self.driver)
        self.co.setFirstName('kiran')
        self.co.setLastName("patil")
        self.co.setPostalCode('pune')
        self.co.clickContinueBt()
        self.co.clickFinishBt()
        self.co.click_Bt_Back_TO_HOme()
        self.targetpage = self.lp.productPageExists()
        if self.targetpage == "Products":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_Back_TO_Home")
            self.driver.close()
            assert False
