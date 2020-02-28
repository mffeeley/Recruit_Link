import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def verify_email(email, chromedriver_dir):
	chrome_options = Options()
	chrome_options.add_argument("--headless")

	# Initiate the Chrome driver with the path argument
	driver = webdriver.Chrome(chromedriver_dir, options = chrome_options)

	# Email Checker URL, and email address to search
	url = "https://tools.verifyemailaddress.io/"

	# Get the email verification website
	driver.get(url)

	# Find the search bar
	search_bar = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/form/div/div[2]/div/input")

	# Enter the query
	search_bar.send_keys(email)

	# Click the search button
	search_button = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/form/div/div[2]/div/div[2]/button").click()

	# Let it load
	time.sleep(1)

	# Email address soup
	status_soup = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/div[2]/div[2]/div/table/tbody/tr/td[2]")

	# Coverted into text
	status = status_soup.text

	# Return verification status
	if status == 'Ok':
		return True
	else:
		return False