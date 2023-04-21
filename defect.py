from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

options = Options()
options.add_argument('--start-maximized')

service = Service()

dc = DesiredCapabilities.CHROME
dc['loggingPrefs'] = { 'browser':'ALL' }

driver = webdriver.Chrome(options=options, service=service, desired_capabilities=dc)
driver.get(r'https://rayan-ali1083.github.io/Automated-Testing-using-Selenium/')

file_input = driver.find_element('id',"formFile")

file_input.send_keys(r"/Users/faheem/Desktop/FAST NUCES/SE/Assignment 2/Automated-Testing-using-Selenium/input-wrong.txt")          # check with input.txt and inputw.txt


submitButton = driver.find_element('xpath',"//button[@id='ins-btn']")                                  # check with ins-btn and bub-btn
submitButton.send_keys("\n")

import ast

f = open("input-wrong.txt", "r")                                                                              # check with input.txt and inputw.txt
                                             
ls = ast.literal_eval(f.readline())
arr = driver.execute_script('return data')
ls = ls.split(',')

check = False
for ch in ls:
    if ch.isdigit() == False:
        check = True
        break

assert check != True, 'Wrong input given to the program. This type of data cannot be sorted. TEST FAILED'
print("DEFECT TEST PASSED")
driver.quit()