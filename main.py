from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


webdriver_path= "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(webdriver_path)

url = "https://orteil.dashnet.org/cookieclicker/"


def upgrade_if_possible():

    element= driver.find_element_by_id('cookies')
    cookies = int(element.text.split()[0])
    print("Cookies",cookies)


    enabled_buttons = driver.find_elements_by_css_selector('#products div.enabled')
    enabled_prices = driver.find_elements_by_css_selector('div.enabled .price')
    
    
    max_button = None
    max_amount = float("-inf")


    for enabled_button,enabled_price in zip(enabled_buttons,enabled_prices):
        price = int(enabled_price.text)
        print("Price",price)
        if cookies >= price and price  > max_amount:
            max_amount = price
            max_button = enabled_button

    if max_button:    
        print(max_button.get_attribute('class'))
        if max_button:    
            max_button.click()




driver.get(url)


cookie = driver.find_element_by_id('bigCookie')


start_time = time.time()
seconds_to_run = 60 *5
while True:
    cookie.click()

    current_time =time.time()
    
    if current_time  - start_time >= seconds_to_run:
        break


    if current_time - start_time >= 5:
        upgrade_if_possible()
        start_time = current_time




element = driver.find_element_by_css_selector("#cookies div")

per_second_cookies = float(element.text().split(':')[1])

print(f"{per_second_cookies} per second")


driver.quit()












