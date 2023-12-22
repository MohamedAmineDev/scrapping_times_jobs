import requests
from bs4 import BeautifulSoup
import time
from fetch_job import fetch_job
from entities.technology import  Technology
def fetch_website(skill):
    sleeping_time=1
    link = f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords={skill}&txtLocation='
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    print(len(jobs))
    for job in jobs:
        current_item=job.find('h2').find('a').get('href')
        the_id=current_item.split('jobid-')[1].split('__PLUS')[0].replace('_','')
        #print(f'Item(link={current_item},id={the_id})')
        current_job=fetch_job(current_item,Technology(1,f'{skill}'),the_id)
        print(current_job)
        time.sleep(sleeping_time)

