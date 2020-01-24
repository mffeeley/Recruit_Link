# Recruit_Link

This repository includes code for Recruit_Link, a command-line utility that can find a recruiter contact at a company based on a job posting url.  

## Getting Started

Fill in the code where it says "FILL".  The 3 locations that much be filled in are the chromedriver local directory, LinkedIn credentials, and Hunter.io API key.  Once that has been done, you can run the app using:

'''python
python app.py
'''

Then just follow the instructions in the command-line.  Make choices using the given number keys and then hit "enter."

### Prerequisites

Install all libraries by using pip install -r requirements.txt in the repository directory.  Requires LinkedIn and Hunter.io accounts and a chromedriver for selenium.   

## Built With

* Python 3.7.6
* Hunter.io
* LinkedIn.com
* BeautifulSoup4
* Selenium
* Pyperclip
  
## Versioning

Version 1.0

### Current Concerns/Issues

* Dependent on Hunter.io and LinkedIn accounts
* May need more email permutations.

## Authors

* **Dan Roth** - *Initial Work*
* **Mike Feeley** - *Email checker alt script*

## Acknowledgments

* Thanks to Mike Feeley for his collaboration.

