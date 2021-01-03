import requests
from bs4 import BeautifulSoup as soup


it_engineering_gigs_link = "https://www.brightermonday.co.ke/jobs/engineering-technology/nairobi?industry=it-telecoms"
response  = requests.get(it_engineering_gigs_link)
raw_page_data = response.text
parsed_data = soup(raw_page_data, "html.parser")

def get_brightermonday_jobs():
    raw_jobs_extract = parsed_data.findAll("div", {"class": "customer-card--row"})
    found_jobs = parsed_data.findAll("h2", {"class": "search-main__header__sub-title--faded"})

    total_found_jobs = found_jobs[0].span.string

    print(f'Total found jobs: {total_found_jobs}')


def get_featured_jobs():
    featured_jobs = parsed_data.findAll("div", {"class":"wrapper--inline-flex direction--column card-content__listing"})
    print(featured_jobs.__len__())
    # print(featured_jobs['wrapper--inline-flex justify--space-between align--center padding-top--5'])

def get_searched_jobs():
    searched_jobs = parsed_data.findAll("div", {"class": "customer-card--column"})
    print(searched_jobs.div)


def extract_junior_roles():
    junior_roles = []
    pass                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            

def extract_mid_level_roles():
    # intermediate_roles = []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               q]
    pass

def extract_pro_roles():
    pass


get_brightermonday_jobs()

get_featured_jobs()
get_searched_jobs()