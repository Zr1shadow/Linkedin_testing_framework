import pytest
from selenium import webdriver
import time
    
# def tearDown(): 
    # self.driver.close()

  
@pytest.fixture()
def setUp():
    driver = webdriver.Chrome(executable_path='C:\\Drivers\\chromedriver')
    return driver


