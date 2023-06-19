import os

from utilities.customLogger import LogGen
from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.LoginPage import LoginPage
from pageObjects.CartPage import CartPage


class OrderedProductPrice():
    baseURL = " https://www.saucedemo.com/"
    logger = LogGen.loggen()

    def test_Place_order(self,setup):
        self.logger.info("****test_Cancel_order*****")
        self.driver= setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp=LoginPage(self.driver)
        self.lp.setUsername("standard_user")
        self.lp.setPassword("secret_sauce")
        self.lp.clickLogin()
        self.cp=CartPage(self.driver)
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
        self.co=CheckOutPage(self.driver)
        self.co.setFirstName('kiran')
        self.co.setLastName("patil")
        self.co.setPostalCode('pune')
        self.co.clickContinueBt()
        self.co.clickCancelBt()
        self.Target_value=self.lp.productPageExists()
        if self.Target_value==True:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_Cancel_order")
            self.driver.close()
            assert False



