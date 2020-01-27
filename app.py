import time, re, pyperclip
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from find_contact import *
from pyhunter import PyHunter


def main():
    linkedin_username = "rdan689@gmail.com"
    linkedin_passkey = "sidious6"
    hunter_apikey = "2fff6266c0128bb9a02a365efd5c661dbe6fc90a"
    chromedriver_dir = "/home/danrothdsp/chromedriver"

    listing_url = input("Welcome to Recruit_Link!  Please enter a job listing's LinkedIn url:\n")
    name, title, profile, company, company_website, job_title = \
        find_contact(listing_url, linkedin_username, linkedin_passkey, chromedriver_dir)
    company_website = company_website.replace("bit.ly", f"{company}.com")
    print(f"Now searching for: {name.strip()}, {title.strip()}\n")

    email_message = f"Hi {name.split()[0]},\n" \
              f"\n" \
              f"I hope this email finds you well.  I just recently saw a posting for a {job_title} position at {company}" \
              f" and would love to learn more.  My experience SKILLS HERE feel like a great fit for the role.\n" \
              f"\n" \
              f"Could you tell me more about the data science team and what it's like to work for the company?  " \
              f"I believe you would have great insight as a {title.strip()} for {company}.\n" \
              f"\n" \
              f"I appreciate any information you could provide, looking forward to hearing from you!\n" \
              f"\n" \
              f"Thank you,\n" \
              f"\n"

    linkedin_message = f"Hi {name.split()[0]}, I recently saw a {job_title} position at {company} and I wanted " \
                       f"to learn more about your company! My experience with FILL feels like a great fit for the " \
                       f"role. Would love any more information you have, thanks!"

    name = name.lower()
    company_email = company_website.replace("https://www.", "@")\
                                   .replace("http://www.", "@")\
                                   .replace("http:", "@")\
                                   .replace(r"\.com.*$", ".com")\
                                   .replace("/", "")
    print(company_email)
    patterns = ["finitiallast", "finitial.last", "firstlast", "first.last",
                "first", "last", "firstlinitial", "first.linitial"]
    patterns = [pattern
                    .replace("first", name.split()[0])
                    .replace("last", name.split()[1])
                    .replace("finitial", name.split()[0][0])
                    .replace("linitial", name.split()[1][0]) + company_email for pattern in patterns]

    hunter = PyHunter(hunter_apikey)  # Hunter API Key here
    hunter_email, confidence_score = hunter.email_finder(company_website, full_name=name)
    if hunter_email:
        emails = [hunter_email] + patterns
    else:
        emails = patterns

    for email in emails:
        print(f"Checking {email}...")
        try:
            verification = hunter.email_verifier(email)
        except:
            continue
        if verification['result'] == 'deliverable':
            print("Success, found the following email:\n")
            print(email)
            pyperclip.copy(email_message)
            print("Message pasted to clipboard.")
            exit()
        elif email == emails[-1]:
            print(f"Email search failed, try to contact on LinkedIn:\n" 
                  f"{profile}")
            pyperclip.copy(linkedin_message)
            print("Message pasted to clipboard.")
            exit()
            exit()
        else:
            continue


if __name__ == "__main__":
    main()
