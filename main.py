import time

from fetch_website import fetch_website
from db_configuration.db_connection import DbConnection
from db_configuration.db_technology import DbTechnology
from entities.technology import Technology
from db_configuration.db_job import DbJob
from entities.job import Job


def main():
    db_connection = DbConnection()
    db_technology = DbTechnology(db_connection)
    db_job = DbJob(db_connection)
    db_technology.create_table()
    db_technology.create_index()
    db_job.create_table()
    db_job.create_index()
    technologies = db_technology.select_technology()
    if not technologies:
        db_technology.insert_technology(Technology(1, 'html'))
        db_technology.insert_technology(Technology(1, 'css'))
        db_technology.insert_technology(Technology(1, 'java'))
        db_technology.insert_technology(Technology(1, 'python'))
        db_technology.insert_technology(Technology(1, 'c'))
        db_technology.insert_technology(Technology(1, 'c#'))
        db_technology.insert_technology(Technology(1, 'react js'))
        db_technology.insert_technology(Technology(1, 'angular'))
        db_technology.insert_technology(Technology(1, 'flutter'))
        db_technology.insert_technology(Technology(1, 'react native'))
        db_technology.insert_technology(Technology(1, 'spring boot'))
        db_technology.insert_technology(Technology(1, 'asp.net core'))
        db_technology.insert_technology(Technology(1, 'devops'))
        db_technology.insert_technology(Technology(1, 'scrum master'))
        db_technology.insert_technology(Technology(1, 'php'))
        db_technology.insert_technology(Technology(1, 'symfony'))
        db_technology.insert_technology(Technology(1, 'laravel'))
        db_technology.insert_technology(Technology(1, 'ruby'))
        db_technology.insert_technology(Technology(1, 'node js'))
        db_technology.insert_technology(Technology(1, 'vus js'))
        db_technology.insert_technology(Technology(1, 'postgresql'))
        db_technology.insert_technology(Technology(1, 'mysql'))
        db_technology.insert_technology(Technology(1, 'mongo db'))
        db_technology.insert_technology(Technology(1, 'hbase'))
        db_technology.insert_technology(Technology(1, 'neo4j'))
        db_technology.insert_technology(Technology(1, 'hadoop'))
        db_technology.insert_technology(Technology(1, 'spark'))
        db_technology.insert_technology(Technology(1, 'pig'))
        db_technology.insert_technology(Technology(1, 'hive'))
        db_technology.insert_technology(Technology(1, 'sql'))
        db_technology.insert_technology(Technology(1, 'wordpress'))
        db_technology.insert_technology(Technology(1, 'sql server'))
        db_technology.insert_technology(Technology(1, 'oracle'))
        db_technology.insert_technology(Technology(1, 'power bi'))
        db_technology.insert_technology(Technology(1, 'codeigniter'))
        db_technology.insert_technology(Technology(1, 'bootstrap'))
        db_technology.insert_technology(Technology(1, 'go'))
        db_technology.insert_technology(Technology(1, 'r'))
        db_technology.insert_technology(Technology(1, 'c++'))
        db_technology.insert_technology(Technology(1, 'xml'))
        db_technology.insert_technology(Technology(1, 'sonarqube'))
        db_technology.insert_technology(Technology(1, 'linux'))
        db_technology.insert_technology(Technology(1, 'selenium'))
        db_technology.insert_technology(Technology(1, 'jira'))
        technologies = db_technology.select_technology()
    sleeping_time = 10
    while True:
        for technology in technologies:
            fetch_website(technology, db_connection)
            print('\n\n\n')
            print(f'Now sleeping for {sleeping_time}')
            time.sleep(sleeping_time)


if __name__ == "__main__":
    """db_job=DbJob(DbConnection())
    jobs=db_job.select_job()
    with open('test.txt', 'w') as file:
        for job in jobs:
            file.write(job.__str__())
    file.close()
    print("Content has been written to the file successfully.")
    """
    main()
