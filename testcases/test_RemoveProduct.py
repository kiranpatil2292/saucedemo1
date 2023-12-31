import os

from pageObjects.CartPage import CartPage
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen


class Test_Cart():
    baseURL = " https://www.saucedemo.com/"
    logger = LogGen.loggen()

    def test001_RemoveFromCart(self, setup):
        self.logger.info("******* Starting test_001_Remove_from_cart **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername("standard_user")
        self.lp.setPassword("secret_sauce")
        self.lp.clickLogin()
        self.cp=CartPage(self.driver)
        self.cp.clickBikeLightPd()
        self.cp.clickCartAddBackLight()
        self.cp.clickButBack()
        self.cp.clickBoltTshirtPd()
        self.cp.clickCartAddBoltTshirt()
        self.cp.clickCartLink()
        self.cp.clickRemovePd()

        self.targetpage = self.cp.clickCartAddValue()
        if self.targetpage == "1":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test001_removeFrom cart")
            self.driver.close()
            assert False
