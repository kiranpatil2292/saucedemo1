from selenium.webdriver.common.by import By


class CheckOutPage():
    txt_Firstname_xpath = "//input[@id='first-name']"
    txt_lastname_xpath = "//input[@id='last-name']"
    txt_Postalcode_xpath = "//input[@id='postal-code']"
    btn_continue_xpath = "//input[@id='continue']"
    confmsg_checkoverview_xpath = "//span[@class='title']"
    but_Finish_xpath = "//button[@id='finish']"
    but_cancel_xpath = "//button[@id='cancel']"
    confmsg_ordersucc_xpath = "//h2[@class='complete-header']"
    confmsg_price_xpath = "//div[@class='summary_info_label summary_total_label']"
    click_Back_to_Home_Xpath = "//button[@id='back-to-products']"
    Scroll_ele_Total_Price_xpath="//div[@class='summary_info_label summary_total_label']"

    def __init__(self, driver):
        self.driver = driver

    def setFirstName(self, name):
        self.driver.find_element(By.XPATH, self.txt_Firstname_xpath).send_keys(name)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txt_lastname_xpath).send_keys(lname)

    def setPostalCode(self, address):
        self.driver.find_element(By.XPATH, self.txt_Postalcode_xpath).send_keys(address)

    def clickContinueBt(self):
        self.driver.find_element(By.XPATH, self.btn_continue_xpath).click()

    def clickCancelBt(self):
        self.driver.find_element(By.XPATH, self.but_cancel_xpath).click()

    def clickFinishBt(self):
        self.driver.find_element(By.XPATH, self.but_Finish_xpath).click()

    def click_Bt_Back_TO_HOme(self):
        self.driver.find_element(By.XPATH, self.click_Back_to_Home_Xpath).click( )

    def scroll_action_price_ele(self):
        scroll_ele= self.driver.find_element(By.XPATH,self.Scroll_ele_Total_Price_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_ele)


    def ConfmsgCheckOverView(self):
        try:
            return self.driver.find_element(By.XPATH, self.confmsg_checkoverview_xpath).text

        except:
            return False

    def confmsgOrdersucc(self):
        try:
            return self.driver.find_element(By.XPATH, self.confmsg_ordersucc_xpath).text
        except:
            return False

    def ConfmsgTotalPrice(self):
        try:
            return self.driver.find_element(By.XPATH, self.confmsg_price_xpath).text()
        except:
            return False
