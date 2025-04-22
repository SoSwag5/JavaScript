from bs4 import BeautifulSoup
import requests

# Fetch the HTML content from the URL
url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation='
response = requests.get(url)
html_text = response.text #to display the text results or textify the url

# Parse the HTML content using BeautifulSoup with lxml parser
soup = BeautifulSoup(html_text, 'lxml') #just memorise the stuff inside

# Find all job listings
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

# Iterate over each job listing
for job in jobs:
    date = job.find('span', class_='sim-posted').span.text #memorise the span.text
    if 'Posted 3 days ago' in date:  # Filter jobs posted
        company_name = job.find('h3', class_='joblist-comp-name').text.strip()  # Use strip() to remove leading/trailing whitespaces
        skills = job.find('span', class_='srp-skills').text.strip()  # Use strip() to remove leading/trailing whitespaces

        # Print job details
        print(f"Company Name: {company_name}")
        print(f"Skills Required: {skills}")
        print(f"Posted: {date}")
        print('___' * 20)
