import os

from pageObjects.CartPage import CartPage
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from pageObjects.CheckoutPage import CheckOutPage


class Test_CheckOut():
    baseURL = " https://www.saucedemo.com/"
    logger = LogGen.loggen()

    def test001_checkout_with_valid_Credential(self, setup):
        self.logger.info("******* Starting test_001_checkout with_valid_Credential **********")
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
        self.co=CheckOutPage(self.driver)
        self.co.setFirstName('kiran')
        self.co.setLastName('patil')
        self.co.setPostalCode('pune')
        self.co.clickContinueBt()

        self.targetpage = self.co.ConfmsgCheckOverView()
        if self.targetpage == True:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+" test002_checkout_with_valid_Credential")
            self.driver.close()
            assert False

    def test002_checkout_with_Invalid_Credential(self, setup):
        self.logger.info("******* Starting test_001_checkout with_Invalid_Credential **********")
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
        self.co=CheckOutPage(self.driver)
        self.co.setFirstName('kiran')
        self.co.setLastName('')
        self.co.setPostalCode('pune')
        self.co.clickContinueBt()

        self.targetpage = self.co.ConfmsgCheckOverView()
        if self.targetpage == True:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_checkOut_invalid_credential")
            self.driver.close()
            assert False


    def test003_checkout_with_Invalid_Credential(self, setup):
        self.logger.info("******* Starting test_001_checkout with_valid_Credential **********")
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
        self.co=CheckOutPage(self.driver)
        self.co.setFirstName('kiran')
        self.co.setLastName('patil')
        self.co.setPostalCode('')
        self.co.clickContinueBt()

        self.targetpage = self.co.ConfmsgCheckOverView()
        if self.targetpage == True:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(
                os.path.abspath(os.curdir) + "\\screenshots\\" + "test_checkOut_invalid_credential")
            self.driver.close()

            assert False


    def test004_checkout_with_Invalid_Credential(self, setup):
        self.logger.info("******* Starting test_001_checkout with_Invalid_Credential **********")
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
        self.co=CheckOutPage(self.driver)
        self.co.setFirstName('')
        self.co.setLastName('')
        self.co.setPostalCode('')
        self.co.clickContinueBt()

        self.targetpage = self.co.ConfmsgCheckOverView()
        if self.targetpage == True:
            assert True
        else:
            self.driver.save_screenshot(
                os.path.abspath(os.curdir) + "\\screenshots\\" + "test_checkOut_invalid_credential")
            self.driver.close()
            assert False

    def test005_checkout_with_Invalid_Credential(self, setup):
        self.logger.info("******* Starting test_001_checkout with_valid_Credential **********")
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
        self.co=CheckOutPage(self.driver)
        self.co.setFirstName('')
        self.co.setLastName('patil')
        self.co.setPostalCode('pune')
        self.co.clickContinueBt()

        self.targetpage = self.co.ConfmsgCheckOverView()
        if self.targetpage == True:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(
                os.path.abspath(os.curdir) + "\\screenshots\\" + "test_checkOut_invalid_credential")
            self.driver.close()
            assert False




