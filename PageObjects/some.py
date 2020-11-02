from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\\Drivers\\chromedriver')

driver.get('https://www.yahoo.com/')

print(driver.find_element_by_class_name('_yb_1wyof ').text)