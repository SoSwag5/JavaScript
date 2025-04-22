from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text #.text so we can only accept text variales inside our code
soup = BeautifulSoup(html_text, 'lxml') #this is a must
jobs = soup.find_all('li', class_ ='clearfix job-bx wht-shd-bx')# _all searches for all jobs \ soup.find gives us the first match only
for job in jobs : #to make jobs varialbe work as the job.find variable so we need a for loop to make that work
    date = job.find('span', class_ = 'sim-posted').span.text
    if 'Posted today' in date: #to filter the results to one day ago only
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','') # we use the job.find not soup to give us a singluar match
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')



        print(f"the company name is {company_name} "
            f"and the skills required are {skills}"
              f"and it was  {date}")
        print('___'* 20)