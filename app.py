import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from find_contact import find_contact


def main():
    name, title, profile, company, company_website = find_contact()
    print(f"Now searching for:\n\n"
          f"{name}{title}")

    # copy company url, send to hunter.io, try name chosen
    # copy hunter output to email checker

    # if pass, output email and metadata
    # if fail, attempt other variations until ok
    # if total fail, error message


if __name__ == "__main__":
    main()
