import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Email Checker URL, and email address to search
url = "https://tools.verifyemailaddress.io/"
email = input("What email address would you like to verify?\n")

# Path to the chromedriver executable
chromedriver = "/Applications/chromedriver"

# Initiate the Chrome driver with the path argument
driver = webdriver.Chrome(chromedriver)

# Get the email verification website
driver.get(url)

# Find the search bar
searchBar = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/form/div/div[2]/div/input")

# Enter the query
searchBar.send_keys(email)

# Click the search button
searchButton = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/form/div/div[2]/div/div[2]/button").click()

# Let it load
time.sleep(1)

# Result soup
result_soup = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/div[2]/div[2]/div/table/tbody/tr/td[2]")

# Coverted into text
result = result_soup.text

# Output
if result == 'Ok':
    print(f"{email} is a valid email. Yay!")
else:
    print(f"{email} is not a valid email.  Sorry!")