from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
import re

email = 'secret'
password = 'evenmroesecret'

browser = webdriver.Chrome()

browser.get('http://gradescope.com/')
time.sleep(5)

# Logging in
loginbutton = browser.find_element_by_xpath('/html/body/div/main/div[2]/div/header/nav/div[2]/span[3]/button')
loginbutton.click()

time.sleep(1)

emailbox = browser.find_element_by_xpath('//*[@id="session_email"]')
emailbox.click()
emailbox.send_keys('gambasz@terpmail.umd.edu')

time.sleep(1)

passwordbox = browser.find_element_by_xpath('//*[@id="session_password"]')
passwordbox.click()
passwordbox.send_keys(password)
passwordbox.send_keys(Keys.RETURN)

time.sleep(3)

# Get course box
#ourse = browser.find_element_by_xpath('//*[@id="account-show"]/div[1]/div[1]/a[1]')
#course.click()

# Goto Assignment link (easier)
browser.get('https://www.gradescope.com/courses/298347/assignments/1627770/review_grades')

time.sleep(5)

all_students = browser.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody')
#print(all_students[0])

odds = all_students.find_elements_by_class_name('odd')
evens = all_students.find_elements_by_class_name('even')

#for line in odds:
#    element = line.find_element_by_tag_name('a')
#    link = element.get_attribute('href')
#    print(link)

#for line in evens:
#    element = line.find_element_by_tag_name('a')
#    link = element.get_attribute('href')
#    print(link)

# Test link
testlink = odds[0].find_element_by_tag_name('a')
testlink = testlink.get_attribute('href')

time.sleep(3)

browser.get(testlink)

time.sleep(3)

# Get submission history
submission_history_button = browser.find_element_by_xpath('//*[@id="main-content"]/section/ul/li[4]/button')
submission_history_button.click()

# Printing it
table = browser.find_element_by_xpath('//*[@id="submission-history-modal"]/div/div[1]/div/table/tbody')
fixed = table.text.split('\n')
print(fixed)

stuff = []

skip = 1

for i, e in enumerate(fixed):
    if i != skip:
        stuff.append(e)
    else:
        skip += 3

regex = re.compile(r"[0-9]+ (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) ([0-9]+)")

print(f'stuff: {stuff}')

for i, e in enumerate(stuff):
    if i % 2 == 0:
        print(e)
        matchobj = re.match(regex, e)
        print(f'On {matchobj.group(1)} {matchobj.group(2)}')
    else:
        print(f'Got grade: {e}')

#dateobj = datetime.datetime.strptime(fixed[0], '%d %B')