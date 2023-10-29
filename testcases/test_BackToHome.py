import os
import time
from pageObjects.CartPage import CartPage
from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_Back_ToHomePageFromProductPage():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_BackToProductPage(self, setup):
        self.logger.info("******* Starting test_BackToProductPage **********")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)

        self.logger.info("**** browser is initialising ****")
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**** navigating to productPage ****")
        self.cp = CartPage(self.driver)
        self.cp.clickBoltTshirtPd()
        self.cp.clickCartAddBoltTshirt()
        self.logger.info("**** adding product  to the cart **** ")
        self.cp.clickButBack()
        self.cp.clickBikeLightPd()
        self.cp.clickCartAddBackLight()
        self.cp.clickCartLink()
        self.logger.info("***** clicking on cartLink  ****")
        self.cp.clickContShop()
        self.cp.clickSacLabPd()
        self.cp.clickAddCartSacLabPd()
        self.cp.clickCartLink()
        self.cp.clickCheckOut()
        self.logger.info("**** clicking on the checkout button ****")
        self.co = CheckOutPage(self.driver)
        self.co.setFirstName('kiran')
        self.co.setLastName("patil")
        self.co.setPostalCode('pune')
        self.logger.info("**** entered input to the checkoutPage  ****")
        self.co.clickContinueBt()
        self.co.clickFinishBt()
        self.logger.info("*****clicking on the Finish Button ******")
        time.sleep(4)
        self.co.click_Bt_Back_TO_HOme()
        self.targetPage = self.lp.productPageExists()
        self.logger.info("**** returning to the product page*****")
        if self.targetPage == "Products":
            assert True
            self.logger.info("**** successfully returned to the product Page")
            self.driver.close()

        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_Back_TO_Home.png")
            self.driver.close()
            self.logger.info("**** not successfully returned to productPage")

            assert False
