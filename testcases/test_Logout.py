import os

from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen


class Test_Login():
    baseURL = " https://www.saucedemo.com/"
    logger = LogGen.loggen()

    def test_Logout(self, setup):
        self.logger.info("******* Starting test_001_logout **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername("standard_user")
        self.lp.setPassword("secret_sauce")
        self.lp.clickLogin()
        self.lp.clickLogout()
        self.Target=self.lp.confmsg_login_xpath()
        if self.Target==True:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_loginLogo")
            self.driver.close()
            assert False


