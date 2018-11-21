from pages.base_element import BaseElement


class BasePage(object):

    url = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)

    def refresh(self):
        self.driver.refresh()

    def scroll_down(self, y=300):
        self.driver.execute_script("window.scrollTo(0, {})".format(y))

    def scroll_up(self, y=-300):
        self.driver.execute_script("window.scrollTo(0, {})".format(y))