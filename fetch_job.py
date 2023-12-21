from bs4 import BeautifulSoup
import requests
from fetch_attributes import *
from entities.job import Job


def fetch_job(link):
    job = Job()
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'lxml')
    head = soup.find('div', class_='jd-header wht-shd-bx')
    job.address = fetch_address(head)
    job.experience = fetch_experience(head)
    post_owner_data = soup.find('div', class_='jd-sec jd-hiring-comp')
    job.enterprise_name = fetch_enterprise_name(post_owner_data)
    print(job)
