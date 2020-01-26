import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def find_contact(listing_url, username, passkey, chromedriver):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chromedriver, options=chrome_options)  # load chromedriver

    driver.get(listing_url)
    listing_soup = BeautifulSoup(driver.page_source, 'html.parser')
    company = listing_soup.find("a", class_="topcard__org-name-link topcard__flavor--black-link").text
    job_title = listing_soup.find("div", class_="topcard__content-left").h1.text
    if listing_soup:
        print(f"Listing found for {job_title} at {company}, just a moment...")

    signin_url = listing_soup.find("a", class_="nav__button-secondary")['href']
    driver.get(signin_url)
    email = username  # LinkedIn username
    passkey = passkey  # LinkedIn pass
    username = driver.find_element_by_xpath("//input[@id='username']")
    username.send_keys(email)
    password = driver.find_element_by_xpath("//input[@id='password']")
    password.send_keys(passkey)
    signin = driver.find_element_by_xpath("//button[@class='btn__primary--large from__button--floating']")
    signin.click()

    company_url = listing_soup.find("a", class_="topcard__org-name-link topcard__flavor--black-link")['href']
    driver.get(company_url)
    company_soup = BeautifulSoup(driver.page_source, 'html.parser')
    people_url = "https://www.linkedin.com" + \
                 company_soup.find("li", class_="org-page-navigation__item ember-view").a['href'] +\
                 "people/?facetGeoRegion=us%3A70&keywords=recruiter"
    driver.get(people_url)

    scroll_time = 0.5
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(scroll_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    time.sleep(1)

    people_soup = BeautifulSoup(driver.page_source, 'html.parser')
    names = people_soup.\
        find_all("div", class_=
            "org-people-profile-card__profile-title t-black lt-line-clamp lt-line-clamp--single-line ember-view")
    titles = people_soup. \
        find_all("div",
                 class_="lt-line-clamp lt-line-clamp--multi-line ember-view")
    profiles = [people['href'] for people in people_soup.find_all("a",
                                                                  {"data-control-name": "people_profile_card_name_link"})]
    company_website = people_soup.find("a", class_="org-top-card-primary-actions__action ember-view")['href']
    contacts = list(zip(names, titles, profiles))

    print("Found the following contacts:\n")
    for idx, (name, title, profile) in enumerate(contacts[:20]):
        print(f"{idx+1} -  {name.text.strip()}, {title.text.strip()}")
    contact = int(input("\nChoose a contact from the list above.\n")) - 1
    name, title, profile = contacts[contact][0].text, contacts[contact][1].text, contacts[contact][2]
    profile = "https://www.linkedin.com" + profile

    return name, title, profile, company, company_website, job_title
