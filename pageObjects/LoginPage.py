from selenium.webdriver.common.by import By


class LoginPage():
    txt_username_xpath = "//input[@id='user-name']"
    txt_password_xpath = "//input[@id='password']"
    btn_login_xpath = "//input[@id='login-button']"
    msg_productpage_xpath = "//span[@class='title']"
    but_logout_xpath="//a[@id='logout_sidebar_link']"
    confmsg_login_xpath="//div[@class='login_logo']"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.XPATH, self.txt_username_xpath).send_keys(username)

    def setPassword(self, pwd):
        self.driver.find_element(By.XPATH,self.txt_password_xpath).send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.but_logout_xpath)

    def productPageExists(self):
        try:
            return self.driver.find_element(By.XPATH,self.msg_productpage_xpath).text
        except:
            return False
    def LoginLogoPage(self):
        try:
            return self.driver.find_element(By.XPATH,self.confmsg_login_xpath).text
        except:
            return None