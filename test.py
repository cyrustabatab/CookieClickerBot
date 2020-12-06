from selenium import webdriver


webdriver_path= "C:\Development\chromedriver.exe"



driver = webdriver.Chrome(webdriver_path)

url = "https://orteil.dashnet.org/cookieclicker/"

driver.get(url)


element = driver.find_element_by_css_selector('div#store')



print(element)









