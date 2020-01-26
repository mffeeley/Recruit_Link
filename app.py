import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from find_contact import *
from pyhunter import PyHunter
import pyperclip


def main():
    linkedin_username = "FILL"
    linkedin_passkey = "FILL"
    hunter_apikey = "FILL"
    chromedriver_dir = "FILL"

    listing_url = input("Welcome to Recruit_Link!  Please enter a job listing's LinkedIn url:\n")
    name, title, profile, company, company_website, job_title = \
        find_contact(listing_url, linkedin_username, linkedin_passkey, chromedriver_dir)
    print(f"Now searching for: {name.strip()}, {title.strip()}\n")

    message = f"Hi {name.split()[0]},\n" \
              f"\n" \
              f"I hope this email finds you well.  I just recently saw a posting for a {job_title} role at {company}" \
              f" and would love to learn more.  My experience SKILLS HERE feel like a great fit for the role.\n" \
              f"\n" \
              f"Could you tell me more about the data science team and what it's like to work for the company?  " \
              f"I believe you would have great insight as a {title.strip()} for {company}.\n" \
              f"\n" \
              f"I appreciate any information you could provide, looking forward to hearing from you!\n" \
              f"\n" \
              f"Thank you,\n" \
              f"\n"

    name = name.lower()
    company_email = company_website.replace("https://www.", "@").replace("http://www.", "@")
    patterns = ["finitiallast", "finitial.last", "firstlast", "first.last",
                "first", "last", "firstlinitial", "first.linitial"]
    patterns = [pattern
                    .replace("first", name.split()[0])
                    .replace("last", name.split()[1])
                    .replace("finitial", name.split()[0][0])
                    .replace("linitial", name.split()[1][0]) + company_email for pattern in patterns]

    hunter = PyHunter(hunter_apikey)  # Hunter API Key here
    hunter_email, confidence_score = hunter.email_finder(company_website, full_name=name)
    emails = [hunter_email] + patterns

    for email in emails:
        print(f"Checking {email}...")
        verification = hunter.email_verifier(email)
        if verification['result'] == 'deliverable':
            print("Success, found the following email:\n")
            print(email)
            pyperclip.copy(message)
            print("Message pasted to clipboard.")
            exit()
        elif email == emails[-1]:
            print(f"Email search failed, try to contact on LinkedIn:\n" 
                  f"{profile}")
            exit()
        else:
            continue


if __name__ == "__main__":
    main()
