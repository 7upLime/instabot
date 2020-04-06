#! /bin/python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import argparse

################## ###################### ##################### ##########################
# Calling from command line
################## ###################### ##################### ##########################

parser = argparse.ArgumentParser(
    description = "Feed the bot with username and password",
    prog="instabot",)

parser.add_argument('username', metavar = 'username', type=str, help="Username required", nargs=1)
parser.add_argument('password', metavar='password', type=str, help="Password required", nargs=1)
################## ###################### ##################### ##########################


class Instabot(object):
    def __init__(self):
        """Initializes all the important stuff, like user and pass from the command line, the random timer...
        Goes directly to homepage with provided arguments"""
        self.username = parser.parse_args().username
        self.password = parser.parse_args().password
        self.browser = webdriver.Firefox()
        self.browser.get('https://instagram.com')
        self.browser.implicitly_wait(5)
        self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(self.username)
        self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(self.password)
        self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div').click()
        self.browser.implicitly_wait(10)
        self.searchbar = self.browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div/div/span[2]')
        self.timer = random.randint(1,5) + random.random()

    def daily_follow_loop(self):
        """This loops trought profiles in follow page
            This should be the daily limit"""
        # This works from home page... clicks the see more section on top of follow sidebar section
        self.browser.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[3]/div[1]/a/div').click()

        for k in range(20):
            
            for i in range(1,40): # yes, actually 39
                
                self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/div/div/div[{0}]/div[3]/button'.format(i)).click() # heart button
                time.sleep(self.timer)
                
            # self.browser.refresh()
            time.sleep(60*60)  ## Hourly limit is approximately 40


    def explore(self):
        self.browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
        time.sleep(self.timer)
        self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/div/div[1]/div[1]/div').click()

        
    def go_there(self,where):
        """ requires an arguments, the text to write to the searchbar
               best use with hastags"""
        self.browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input').send_keys('#{0}'.format(where))
        self.browser.implicitly_wait(2)
        self.browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]').click()
        self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[2]').click()

    def do_likes(self, likes=100, every=4):
        """ Loops from the current card """
        #initiate counter
        chose = 0
        for i in range(likes):  #the one provided in args
            self.browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click() ##Next_one
            time.sleep(self.timer) # randomness 
            chose += 1
            if chose >= every: # sometimes may miss one
                self.browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button').click()
                chose = 0
                
    def do_comments(self, message, comments=100, every=4):
        """ Basically just like do_likes """
        #initiate counter
        chose = 0
        for i in range(comments):  #the one provided in args
            self.browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click() ##Next_one
            time.sleep(self.timer) # randomness 
            chose += 1
            if chose >= every: # sometimes may miss one
                self.browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea').click()
                self.browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea').send_keys(message)
                self.browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button').click()
                chose = 0

    def watch_stories(self,till_wake_up):
        self.browser.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[1]/button/div[1]/span/img').click()
        time.sleep(till_wake_up)



if __name__ == '__main__':
    bot = Instabot()
