from selenium.webdriver.common.by import By

from pages.base_page import *


class PhpTravelsMain(BasePage):

    url = 'https://phptravels.com/'

    @property
    def notification_popup_cancel_button(self):
        by = By.ID
        value = "onesignal-popover-cancel-button"
        return BaseElement(driver=self.driver, by=by, value=value)

    @property
    def mailing_popup_exit_button(self):
        by = By.XPATH
        value = "//div[@id='PopupSignupForm_0']/div[@class='mc-modal']/div[@class='mc-closeModal']"
        return BaseElement(driver=self.driver, by=by, value=value)

    @property
    def nav_demo_button(self):
        by = By.XPATH
        value = "//nav[@class='main-nav main-nav-holder']/ul/li[1]/span/span/a"
        return BaseElement(driver=self.driver, by=by, value=value)

    @property
    def nav_pricing_button(self):
        by = By.XPATH
        value = "//nav[@class='main-nav main-nav-holder']/ul/li[2]/span/span/a"
        return BaseElement(driver=self.driver, by=by, value=value)

    @property
    def nav_features_button(self):
        by = By.XPATH
        value = "//nav[@class='main-nav main-nav-holder']/ul/li[3]/span/span/a"
        return BaseElement(driver=self.driver, by=by, value=value)

    @property
    def nav_product_button(self):
        by = By.XPATH
        value = "//nav[@class='main-nav main-nav-holder']/ul/li[4]/span/span/a"
        return BaseElement(driver=self.driver, by=by, value=value)

    @property
    def nav_hosting_button(self):
        by = By.XPATH
        value = "//nav[@class='main-nav main-nav-holder']/ul/li[5]/span/span/a"
        return BaseElement(driver=self.driver, by=by, value=value)

    @property
    def nav_services_button(self):
        by = By.XPATH
        value = "//nav[@class='main-nav main-nav-holder']/ul/li[6]/span/span/a"
        return BaseElement(driver=self.driver, by=by, value=value)

    @property
    def nav_company_button(self):
        by = By.XPATH
        value = "//nav[@class='main-nav main-nav-holder']/ul/li[7]/span/span/a"
        return BaseElement(driver=self.driver, by=by, value=value)

    @property
    def nav_login_button(self):
        by = By.XPATH
        value = "//nav[@class='main-nav main-nav-holder']/ul/li[8]/span/span/a"
        return BaseElement(driver=self.driver, by=by, value=value)