from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CartPage():
    pd_bikelight_xpath = "//div[normalize-space()='Sauce Labs Bike Light']"
    cartadd_bikelight_xpath = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    btn_back_xpath = "//button[@id='back-to-products']"
    pd_boltTshirt_xpath = "//div[normalize-space()='Sauce Labs Bolt T-Shirt']"
    cartadd_boltTshirt_id = 'add-to-cart-sauce-labs-bolt-t-shirt'
    cartmsg_addvalue_xpath = "//span[@class='shopping_cart_badge']"
    cart_link_xpath = "//a[@class='shopping_cart_link']"
    cart_removepd_xpath = "//button[@id='remove-sauce-labs-bike-light']"
    but_contshop_xpath = "//button[@id='continue-shopping']"
    pd_saclabone_xpath = "//div[normalize-space()='Sauce Labs Onesie']"
    cartadd_saclabone_xpath = "//button[@id='add-to-cart-sauce-labs-onesie']"
    but_checkout_xpath = "//button[@id='checkout']"
    confmsg_checkout_xpath = "//span[@class='title']"
    drp_pd_sort_container = "//select[@class='product_sort_container']"

    def __init__(self, driver):
        self.driver = driver

    def clickBikeLightPd(self):
        self.driver.find_element(By.XPATH, self.pd_bikelight_xpath).click()

    def clickCartAddBackLight(self):
        self.driver.find_element(By.XPATH, self.cartadd_bikelight_xpath).click()

    def clickButBack(self):
        self.driver.find_element(By.XPATH, self.btn_back_xpath).click()

    def clickBoltTshirtPd(self):
        self.driver.find_element(By.XPATH, self.pd_boltTshirt_xpath).click()

    def clickCartAddBoltTshirt(self):
        self.driver.find_element(By.ID, self.cartadd_boltTshirt_id).click()

    def clickCartLink(self):
        self.driver.find_element(By.XPATH, self.cart_link_xpath).click()

    def clickRemovePd(self):
        self.driver.find_element(By.XPATH, self.cart_removepd_xpath).click()

    def clickContShop(self):
        self.driver.find_element(By.XPATH, self.but_contshop_xpath).click()

    def clickSacLabPd(self):
        self.driver.find_element(By.XPATH, self.pd_saclabone_xpath).click()

    def clickAddCartSacLabPd(self):
        self.driver.find_element(By.XPATH, self.cartadd_saclabone_xpath).click()

    def clickCheckOut(self):
        self.driver.find_element(By.XPATH, self.but_checkout_xpath).click()

    def seleDropOpt(self):
        Product_sort = Select(self.driver.find_element(By.XPATH, self.drp_pd_sort_container))
        Product_sort.select_by_visible_text("Price (low to high)")

    def clickCartAddValue(self):
        try:
            return self.driver.find_element(By.XPATH, self.cartmsg_addvalue_xpath).text
        except:
            return False

    def conFroMsgCheckout(self):
        try:
            return self.driver.find_element(By.XPATH, self.confmsg_checkout_xpath).text
        except:
            return False
