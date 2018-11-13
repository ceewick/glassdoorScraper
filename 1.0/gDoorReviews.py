#!/usr/bin/env python
import time
import requests
from bs4 import  BeautifulSoup
import pandas as pd
from urllib.request import urlopen
from userAgents import user_agents, randomUserAgents
import lxml

url = 'https://www.glassdoor.com/Reviews/Snap-Reviews-E671946.htm'
head = randomUserAgents()
start = time.time()

def soup(url,headers):
    ''' url = full glassdoor.com/reviews url'''
    session = requests.Session()
    req = session.get(url, headers=headers)
    bs = BeautifulSoup(req.text, 'lxml')
    return bs

pages = set()
def getPages(url, head):
    ''' Gets a set of ALL "Next Page" hrefs '''
    global pages
    bs = soup(url, head)
    nextPage = bs.find('div',{'class',"flex-grid tbl margTop"})
    for link in nextPage.findAll('a'):
        if 'href' in link.attrs:
            url = 'https://glassdoor.com{}'.format(link.attrs['href'])
            if url not in pages:
            #new page
                pages.add(url)
    #get last page
    for lastPage in nextPage.findAll('li',{'class':'page last'}):
        lastPage = 'https://glassdoor.com{}'.format(lastPage.a['href'])
        getPages(lastPage, head)
    return pages

startTime = start - time.time()

a=[]
date=[]
revNo=[]
employee=[]
position = []
summ=[]
pro=[]
con=[]
advice=[]
review = []
subReviews = []
workLife = []
culture = []
careerOpp = []
compBenefits = []
srManagement = []
# recommend=[]
# outlook=[]
# ceo=[]
link=[]

pages = getPages(url, head)
count = 1
for page in pages:
    bs = soup(page,head)
    for x in bs.findAll('li',{'class',' empReview cf '}):

    # ## PK
        a.append(count)
        count += 1

    ## Rev Number
        try:
            revNo.append(x.attrs['id'])
            # revNo.append(x.find('li',{'class':' empReview cf '}).attrs[' id'])
            # for emp in x.find(':
            #     print(emp.attrs[' id'])
        except:
            revNo.append('None')

        ## overall rating
        try:
            rating = x.find('span',{'class':'rating'})
            for y in rating:
                review.append(rating.find('span',{'class':'value-title'})\
                              .attrs['title'])
        except:
            review.append('None')

    ## subRatings list
        try:
            for rate in x.findAll('span',{'class':'gdBars gdRatings med '}):
                z = rate.attrs['title']
                subReviews.append(z)
        except:
            subReviews.append('None')

    ## Date
        try:
            date.append(x.find('time',{'class':'date subtle small'}).text)
        except:
            date.append('None')
    # Summary
        try:
            summar = x.a.text
            summar = summar.split('"')
            summ.append(summar[1])
        except:
            summ.append('None')
    ## Pros
        try:
            pro.append(x.find('p',{'class':' pros mainText truncateThis'\
                            ' wrapToggleStr'}).text)
        except:
            pro.append('None')
    ## Cons
        try:
            con.append(x.find('p',{'class':' cons mainText truncateThis'\
                            ' wrapToggleStr'}).text)
        except:
            con.append('None')
    ## Advice to Management
        try:
            advice.append(x.find('p',{'class':' adviceMgmt mainText truncateThis'\
                            ' wrapToggleStr'}).text)
        except:
            advice.append('None')

    ## Employee Type
        try:
            employee.append(x.find('span',{'class':"authorJobTitle"}).text)
        except:
            employee.append('None')
    ## Position and Location
        try:
            position.append(x.find('p',{'class':' tightBot mainText'}).text)
        except:
            position.append('None')
    ## Review Link
        link.append(url+(x.find('a',{'class':'reviewLink'}).attrs['href']))

    for x in range(len(subReviews)):
        if x==0 or x%5==0:
            workLife.append(subReviews[x])
        if x==1 or x%5==1:
            culture.append(subReviews[x])
        if x==2 or x%5==2:
            careerOpp.append(subReviews[x])
        if x==3 or x%5==3:
            compBenefits.append(subReviews[x])
        if x==4 or x%5==4:
            srManagement.append(subReviews[x])

df=pd.DataFrame(index=a)
df['date']=date
df['reviewNo']=revNo
df['employeeType']=employee
df['position']=position
df['summary']=summ
df['pro']=pro
df['con']=con
df['advice']=advice
df['overallStar']=review
df['workLifeStar']=review
df['cultureStar']=review
df['careerOppStar']=review
df['comBenefitsStar']=review
df['srManagementStar']=review
df['reviewLink']=link

csvName = input('What do you want to call the csv?')
df.to_csv('{}.csv'.format(csvName), sep=',')
print('StartTime = {}\nEnd Time = {}'.format(startTime, start - time.time()))
