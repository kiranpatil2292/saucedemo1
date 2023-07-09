import os

from pageObjects.CartPage import CartPage
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_Cart():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test001_AddToCart(self, setup):
        self.logger.info("******* Starting test_001_login **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.cp = CartPage(self.driver)
        self.cp.clickBikeLightPd()
        self.cp.clickCartAddBackLight()

        self.targetPage = self.cp.clickCartAddValue()
        if self.targetPage == '1':
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test001_addcart")
            self.driver.close()
            assert False
