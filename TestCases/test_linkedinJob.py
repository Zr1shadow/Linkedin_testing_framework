import pytest
import logging
import time
from selenium import webdriver
from PageObjects.LinkedinJob import LinkedinPostings
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
class Test_LinkedinJobs:
    
    URL =  ReadConfig.getApplicationURL()
    QA_Positions = "QA Engineer"
    Python_Positions = "Python"
    location = "Houston, Texas, United States"
    
    logger = LogGen.log()
    def test_demo(self,setUp):
        self.driver = setUp
        self.driver.get(self.URL)
        # self.logger.info('*** Test_DEMO ***')
        # self.logger.info('** Verifying Linkedin job POStings **')
        
        test = LinkedinPostings(self.driver)
        
        test.searchJobs(self.QA_Positions)
        area = test.inputLocation(self.location)
        
        test.loopJobs(test.getJobs())
        # print(test.getJobTitle)
        # self.logger.info(test.loopJobs())
        assert area == self.location
        time.sleep(5)
        # test.continueToListing()
        
        
        self.driver.close()
        
        
