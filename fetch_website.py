import requests
from bs4 import BeautifulSoup
import time
from fetch_job import fetch_job
from entities.technology import Technology
from db_configuration.db_job import DbJob


# link = (f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit'
#            f'&searchTextSrc=&searchTextText=&txtKeywords={technology.name}&txtLocation=')
def fetch_website(technology, db_connection):
    sleeping_time = 1
    for i in range(0, 10):
        print(f'Scrapping page {i + 1}')
        link = f'https://www.timesjobs.com/candidate/job-search.html?from=submit&luceneResultSize=25&txtKeywords=python&postWeek=60&searchType=personalizedSearch&actualTxtKeywords={technology.name}&searchBy=0&rdoOperator=OR&pDate=I&sequence=2&startPage={i}'
        html_text = requests.get(link).text
        soup = BeautifulSoup(html_text, 'lxml')
        jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
        print(len(jobs))
        j = 0
        db_job = DbJob(db_connection)
        for job in jobs:
            current_item = job.find('h2').find('a').get('href')
            the_id = current_item.split('jobid-')[1].split('__PLUS')[0].replace('_', '')
            print(f'Item(link={current_item},id={the_id})')
            current_job = fetch_job(current_item, technology, the_id)
            found_job = db_job.select_one_job_by_unique_id(the_id)
            if found_job is None:
                db_job.insert_offer(current_job)
                j = j + 1
            time.sleep(sleeping_time)
        print(f'{j} jobs where added ')
