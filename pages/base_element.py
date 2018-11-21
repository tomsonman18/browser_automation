from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pyautogui as pg


class BaseElement(object):
    def __init__(self, driver, value, by):
        self.driver = driver
        self.value = value
        self.by = by
        self.locator = self.by, self.value

        # needed for moving the mouse
        self.screen_width, self.screen_height = pg.size()
        self.outer_width = self.driver.execute_script("return outerWidth")
        self.outer_height = self.driver.execute_script("return outerHeight")
        self.mid_height = self.driver.execute_script("return outerHeight - innerHeight")
        self.pos_x = self.screen_width/2
        self.pos_y = self.mid_height/2
        self.hover_speed = 0.3

        self.web_element = None
        self.find_element()

    def find_element(self):
        # Wait for the element to be visible and then returns that element
        # This is the same as self.driver.find_element(by.id, 'id') except its better cause it waits for the element
        element = WebDriverWait(
            self.driver, 10).until(
            EC.visibility_of_element_located(
                locator=self.locator))

        # reset the web element to this
        self.web_element = element
        # moves the mouse
        self.move_mouse()
        return None

    def move_mouse(self):
        # locates the positions of the next elements
        middle_width_elem = self.web_element.size['width']/2
        self.pos_x = (self.web_element.location['x'] + middle_width_elem) * self.screen_width / self.outer_width
        self.pos_y = (self.web_element.location['y'] + self.mid_height) * self.screen_height / self.outer_height
        # moves the mouse to the located element position
        pg.moveTo(self.pos_x, self.pos_y, self.hover_speed, pg.easeOutQuad)

    def click(self):
        element = WebDriverWait(
            self.driver, 10).until(
            EC.visibility_of_element_located(
                locator=self.locator))
        # reset the web element to this
        element.click()
        return None

    def send_text(self, text):
        element = WebDriverWait(
            self.driver, 10).until(
            EC.visibility_of_element_located(
                locator=self.locator))
        # reset the web element to this
        element.send_keys(text)
        return None

    @property
    def get_text(self):
        text = self.web_element.text
        return text

    @property
    def html_text(self):
        html = self.web_element.get_attribute('innerHTML')
        return html
