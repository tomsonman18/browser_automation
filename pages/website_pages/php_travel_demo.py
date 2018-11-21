from selenium.webdriver.common.by import By

from pages.base_page import *


class PhpTravelDemo(BasePage):

    url = 'https://phptravels.com/demo/'

    @property
    def TopTextMessage(self):
        by = By.XPATH
        value = "//h2[@class='wow fadeIn cw upper animated']"
        return BaseElement(driver=self.driver, by=by, value=value)

