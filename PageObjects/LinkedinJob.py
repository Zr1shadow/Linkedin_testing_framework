from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class LinkedinPostings:
    jobSearch_xpath = '/html[1]/body[1]/header[1]/nav[1]/section[1]/section[2]/form[1]/section[1]/input[1]'
    jobLocation = 'location'
    pressSearch = 'base-search-bar__submit-btn'
    jobs_css = 'li[class *= \'result-card\']'
    jobTitle_css = 'h2[class *= \'topcard__title\']'
    jobCompany_css = 'a[class *= \'topcard__org-name-link topcard__flavor--black-link\']'
    
  
    
    def __init__(self, driver):
        self.driver = driver
    
    def maxScreen(self):
        self.driver.maximize_window()
    def searchJobs(self, jobInput):
        self.driver.find_element_by_xpath(self.jobSearch_xpath).send_keys(jobInput)
        # self.driver.find_element_by_xpath(self.jobSearch_xpath).send_keys(Keys.ENTER)
    def inputLocation(self, location):
        self.driver.find_element_by_name(self.jobLocation).clear()
        self.driver.find_element_by_name(self.jobLocation).send_keys(location)
        self.driver.find_element_by_name(self.jobLocation).send_keys(Keys.ENTER)
        return self.driver.find_element_by_name(self.jobLocation).get_attribute("value")

    # def continueToListing(self):
    #     button = self.driver.find_element_by_class_name(self.pressSearch)
    def getJobs(self):
        return self.driver.find_elements_by_css_selector(self.jobs_css)
    def getJobTitle(self):
        return self.driver.find_element_by_css_selector(self.jobTitle_css).text

    def getJobCompany(self):
        return self.driver.find_element_by_css_selector(self.jobCompany_css).text

    def loopJobs(self, jobs):
        jobs_Details = []
        
        for job in jobs:
            job.click()
            #replace time with selenium timer/await method
            time.sleep(1)
            title = self.getJobTitle()
            company = self.getJobCompany()
            # company = self.getJobCompany()
            # jobs_Details.append(title)
        return jobs_Details 