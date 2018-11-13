import sys
from datetime import datetime
import time
from bs4 import  BeautifulSoup as bs

import settings
from userAgents import user_agents, randomUserAgents
from models import ReviewRecord, establish_table, close_database
from helpers import soup, getPages
from extractors import *


def fetch_reviews(bs):
    for reviewTable in bs.findAll('li',{'class',' empReview cf '}):
        reviewNumber = get_revNumber(reviewTable)
        overallRating = get_overallRating(reviewTable)
        date = get_date(reviewTable)
        summary = get_summary(reviewTable)
        pros = get_pros(reviewTable)
        cons = get_cons(reviewTable)
        advice = get_adviceToManagement(reviewTable)
        employee = get_employeeType(reviewTable)
        position = get_positionAndLocation(reviewTable)
        reviewExtension = get_reviewLink(reviewTable)
        reviewLink = 'https://www.glassdoor.com{}'.format(reviewExtension)
        subRatings = get_subRatings(reviewTable)
                  
        try:
            workLife = subRatings['Work/Life Balance'] 
        except:
            workLife = 'Null'
        try:
            culture = subRatings['Culture & Values'] 
        except:
            culture = 'Null'
        try:
            careerOpps = subRatings['Career Opportunities'] 
        except:
            careerOpps = 'Null'
        try:
            compBenefits = subRatings['Comp & Benefits'] 
        except:
            compBenefits = 'Null'
        try:
            management = subRatings['Senior Management'] 
        except:
            management = 'Null'

 
        review = ReviewRecord(reviewNumber, overallRating, date, summary, pros, cons, advice, employee, position, reviewLink, workLife, culture, careerOpps, compBenefits, management)
        review.save()
    

if __name__ == '__main__':
    url = settings.url
    head = randomUserAgents()
    pages = getPages(url, head)
    establish_table()
    count = 1
    for page in pages:
        print('starting page {} of {}'.format(count, len(pages)))
        bs = soup(page,head)
        fetch_reviews(bs)
        count += 1
    close_database()