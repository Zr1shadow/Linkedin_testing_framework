import pytest
from selenium import webdriver
import logging
from utilities.readProperties import ReadConfig

class Test_Google_Search():
    google_url = ReadConfig.getApplicationgoogle_url()
    def test_search_company(self, setup):
        self.driver = setup
        self.driver.get(self.google_url)
