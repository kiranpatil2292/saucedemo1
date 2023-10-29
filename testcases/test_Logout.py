import os
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen


class Test_Logout():
    baseURL = ReadConfig.getApplicationURL()
    username= ReadConfig.getUserName()
    password= ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_Logout(self, setup):
        self.logger.info("******* Starting test_001_logout **********")
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.clickBurgerMenuBt()
        self.lp.clickLogout()
        self.Target=self.lp.LoginLogoPage()
        if self.Target=='Swag Labs':
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"testLogout")
            self.driver.close()
            assert False


