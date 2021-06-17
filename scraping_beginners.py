from selenium import webdriver
import time

# Writing our First Selenium Python Test
# web = 'https://sports.tipico.de/en/all/football/spain/la-liga'  # choose any other league
web = 'https://sports.tipico.de/en/all/football/spain/'
# web = 'https://sports.tipico.de/en/all/football/england'
# web = 'https://sports.tipico.de/en/all/football/euro-2020?mode=tc'
path = '/usr/local/bin/chromedriver'

driver = webdriver.Chrome(path)
driver.get(web)

#Make ChromeDriver click a button
time.sleep(5) #add implicit wait, if necessary
# //*[@id="_evidon-accept-button"]
# #_evidon-accept-button
# accept = driver.find_element_by_id('#_evidon-accept-button')
# /html/body/div[6]/button[1]
# //*[@id="_evidon-accept-button"]
# #_evidon-accept-button
accept = driver.find_element_by_xpath('//*[@id="_evidon-accept-button"]')
accept.click() # click on accept button

# Initialize your storage
teams = []
x12 = [] #3-way
odds_events = []

#scroll down to the bottom to load upcoming matches (update 2: not necessary anymore)
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#time.sleep(3) #add implicit wait to let the driver load the elements of the upcoming matches section.

#select only upcoming matches box
box = driver.find_element_by_xpath('//div[contains(@testid, "Program_SELECTION")]') #update 3
#Looking for 'sports titles'
sport_title = box.find_elements_by_class_name('SportTitle-styles-sport')

time.sleep(5) #add implicit wait, if necessary
driver.quit()