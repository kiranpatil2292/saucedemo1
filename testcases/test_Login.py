import os

from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen


class Test_Login():
    baseURL = " https://www.saucedemo.com/"
    logger = LogGen.loggen()

    def test001_Login(self, setup):
        self.logger.info("******* Starting test_001_login **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername("standard_user")
        self.lp.setPassword("secret_sauce")
        self.lp.clickLogin()

        self.targetpage = self.lp.productPageExists()
        if self.targetpage == "Products":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_login001")
            self.driver.close()
            assert False

    def test002_Invalid_Login(self, setup):
        self.logger.info("******* Starting test_002_login **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername("Sagar")
        self.lp.setPassword("secret_sauce")
        self.lp.clickLogin()

        self.targetpage = self.lp.productPageExists()
        if self.targetpage == "Products":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_login002")
            self.driver.close()
            assert False

    def test003_Invalid_Login(self, setup):
        self.logger.info("******* Starting test_003_login **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername("standard_user")
        self.lp.setPassword("KiranPatil")
        self.lp.clickLogin()

        self.targetpage = self.lp.productPageExists()
        if self.targetpage == "Products":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_login003")
            self.driver.close()
            assert False

    def test004_Login(self, setup):
        self.logger.info("******* Starting test_004_login **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername("asharram")
        self.lp.setPassword("Pasdewk")
        self.lp.clickLogin()

        self.targetpage = self.lp.productPageExists()
        if self.targetpage == "Products":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_login004")
            self.driver.close()
            assert False

    def test005_Login(self, setup):
        self.logger.info("******* Starting test_004_login **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername("")
        self.lp.setPassword("")
        self.lp.clickLogin()

        self.targetpage = self.lp.productPageExists()
        if self.targetpage == "Products":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_login005")
            self.driver.close()
            assert False







