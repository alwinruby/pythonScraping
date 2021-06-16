from selenium import webdriver
import time

# Writing our First Selenium Python Test
web = 'https://sports.tipico.de/en/all/football/spain/la-liga'  # you can choose any other league (update 1)
path = '/usr/local/bin/chromedriver'


driver = webdriver.Chrome(path)
driver.get(web)