import os
import time

from pageObjects.CartPage import CartPage
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

class Test_Cart():
    baseURL = ReadConfig.getApplicationURL()
    userName= ReadConfig.getUserName()
    password= ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test001_AddMultiProductToCart(self, setup):
        self.logger.info("******* Starting test_001_Remove_from_cart **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.userName)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.cp = CartPage(self.driver)
        self.cp.clickBikeLightPd()
        time.sleep(2)
        self.cp.clickCartAddBackLight()
        time.sleep(1)
        self.cp.clickButBack()
        self.cp.clickBoltTshirtPd()
        self.cp.clickCartAddBoltTshirt()
        self.cp.clickCartLink()
        self.cp.clickRemovePd()
        self.cp.clickContShop()
        self.cp.clickSacLabPd()
        self.cp.clickAddCartSacLabPd()

        self.targetpage = self.cp.clickCartAddValue()
        if self.targetpage == '2':
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test001_removeFrom cart")
            self.driver.close()
            assert False

