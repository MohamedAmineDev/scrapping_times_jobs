from bs4 import BeautifulSoup
import requests
from fetch_attributes import *
from entities.job import Job


def fetch_job(link,technology,job_id):
    job = Job()
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'lxml')
    head = soup.find('div', class_='jd-header wht-shd-bx')
    job.address = fetch_address(head)
    job.experience = fetch_experience(head)
    post_owner_data = soup.find('div', class_='jd-sec jd-hiring-comp')
    job.enterprise_name = fetch_enterprise_name(post_owner_data)
    job.title = fetch_title(soup)
    job.date = fetch_date(soup)
    profile_date = soup.find('ul', class_='clearfix', id='applyFlowHideDetails_1')
    job.qualification=fetch_qualification(profile_date)
    job.contract_type='Unknown'
    job.languages='English'
    job.skills=fetch_skills(soup)
    job.technology=technology
    job.unique_id=job_id
    return job
