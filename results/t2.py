from selenium import webdriver

from pages.website_pages.php_travel_main import PhpTravelsMain
from pages.website_pages.php_travel_demo import PhpTravelDemo

# Test Setup
browser = webdriver.Chrome()
browser.maximize_window()
php_travel_main_page = PhpTravelsMain(driver=browser)
php_travel_demo_page = PhpTravelDemo(driver=browser)

# test 2
php_travel_demo_page.go()


# assert
php_travel_demo_page.scroll_down()

# end test 2
print('Test 2 passed')
browser.quit()

