import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def main():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome('/home/danrothdsp/chromedriver', options=chrome_options)

    company_url = input("Welcome to RecruitLink!  Please enter a company's LinkedIn url:\n")
    driver.get(company_url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    if soup:
        print('Company found')
    else:
        print('Sorry, try again?')
        sys.exit()




if __name__ == "__main__":
    main()
