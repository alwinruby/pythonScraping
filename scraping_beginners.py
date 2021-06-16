from selenium import webdriver
import time

# Writing our First Selenium Python Test
# web = 'https://sports.tipico.de/en/all/football/spain/la-liga'  # choose any other league
web = 'https://sports.tipico.de/en/all/football/england'
path = '/usr/local/bin/chromedriver'

driver = webdriver.Chrome(path)
driver.get(web)

#Make ChromeDriver click a button
time.sleep(5) #add implicit wait, if necessary
accept = driver.find_element_by_xpath('//*[@id="_evidon-accept-button"]')
accept.click()

time.sleep(5) #add implicit wait, if necessary
driver.quit()