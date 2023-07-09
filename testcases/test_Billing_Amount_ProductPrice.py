import os
import time
from pageObjects.CartPage import CartPage
from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_BillingAmountOfOrderedProduct():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_Billing_priceOfOrdered_product(self, setup):
        self.logger.info("**** started test_Billing_priceOfOrdered_product ****")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info("***** browser is initializing *****")
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***** successfully logged into product page *****")
        self.cp = CartPage(self.driver)
        self.cp.seleDropOpt()
        time.sleep(4)
        self.logger.info("**** sorting the product ****")
        self.cp.clickSacLabPd()

        self.cp.clickAddCartSacLabPd()
        self.logger.info("**** adding the product to the cart *****")
        self.cp.clickButBack()
        self.logger.info("***** comes back  from cartPage to ProductPage ****")
        self.cp.clickBikeLightPd()
        self.cp.clickCartAddBackLight()
        self.cp.clickCartLink()
        self.logger.info("**** clicking on cartLink ****")
        self.cp.clickContShop()
        self.logger.info("**** clicking on continueShopping button ****")
        self.cp.clickBoltTshirtPd()
        self.cp.clickCartAddBoltTshirt()
        self.cp.clickCartLink()
        self.cp.clickCheckOut()
        self.logger.info("**** clicking on checkout button ***")
        self.co = CheckOutPage(self.driver)
        self.co.setFirstName('kiran')
        self.co.setLastName('Patil')
        self.co.setPostalCode('Pune')
        self.co.clickContinueBt()
        self.logger.info("**** adding input to the checkoutPage ")
        self.co.scroll_action_price_ele()
        self.targetPage = self.co.ConfmsgTotalPrice()
        time.sleep(10)
        if self.targetPage == "Total: $36.69" :
            assert True
            self.logger.info("**** successfully billing amount is verified ****")
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "price_amount.png")
            self.co.clickFinishBt()
            time.sleep(4)
            self.driver.close()
            self.logger.info("**** price amount is not successfully verified ****")

            assert False
