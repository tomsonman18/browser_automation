from selenium import webdriver

from pages.website_pages.php_travel_main import PhpTravelsMain
from pages.website_pages.php_travel_demo import PhpTravelDemo

# Test Setup
browser = webdriver.Chrome()
browser.maximize_window()
php_travel_main_page = PhpTravelsMain(driver=browser)
php_travel_demo_page = PhpTravelDemo(driver=browser)

# test 1
php_travel_main_page.go()
php_travel_main_page.notification_popup_cancel_button.click()
php_travel_main_page.mailing_popup_exit_button.click()
php_travel_main_page.nav_demo_button.click()
# assert
assert php_travel_demo_page.TopTextMessage.html_text == 'Application Test Drive.'
# end test 1
print('Test 1 passed')
browser.quit()

