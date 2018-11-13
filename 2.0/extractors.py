def get_revNumber(review):
    ## Rev Number
    try:
        revNumber = review.attrs['id']
        return revNumber
        # revNo.append(x.find('li',{'class':' empReview cf '}).attrs[' id'])
        # for emp in x.find(':
        #     print(emp.attrs[' id'])
    except:
        return 'ERR: No revNumber'


def get_overallRating(review):
    ## overall rating
    try:
        overallRating = review.find('span',{'class':'value-title'})\
                    .attrs['title']
        return overallRating 
    
    except:
        return ('Null')


def get_date(review):
    ## Date
    try:
        date = review.find('time',{'class':'date subtle small'}).text
        return date
    except:
        return 'Null'

def get_summary(review):
    # Summary
    try:
        summar = review.a.text
        summar = summar.split('"')
        summary = summar[1]
        return summary
    except:
        return 'Null'

def get_pros(review):
    ## Pros
    try:
        pro = review.find('p',{'class':' pros mainText truncateThis wrapToggleStr'}).text
        return pro    
    except:
        return 'Null'

def get_cons(review):
    ## Cons
    try:
        con = review.find('p',{'class':' cons mainText truncateThis wrapToggleStr'}).text
        return con
    except:
        return 'Null'

def get_adviceToManagement(review):
    ## Advice to Management
    try:
        advice = review.find('p',{'class':' adviceMgmt mainText truncateThis wrapToggleStr'}).text
        return advice
    except:
        return 'Null'

def get_employeeType(review):
    ## Employee Type
    try:
        employeeType = review.find('span',{'class':"authorJobTitle"}).text
        return employeeType
    except:
        return 'Null'
    
def get_positionAndLocation(review):
    ## Position and Location
    try:
        positionAndLocation = review.find('p',{'class':' tightBot mainText'}).text
        return positionAndLocation
    except:
        return 'Null'

def get_reviewLink(review):
## Review Link
    try:
        reviewLink = review.find('a',{'class':'reviewLink'}).attrs['href']
        return reviewLink
    except:
        return 'Null'

def get_subRatings(review):
    subs = {}
    # subRatings = review.find('div',{'class':'subRatings module'})
    for subRating in review.findAll('li'):
        try:
            for x in range(0,3):
                title = subRating.text
                score = subRating.find('span',{'class':'gdBars gdRatings med '}).attrs['title']
                subs[title] = score
        except:
                subs['missing'] = 'idk - missing'
                continue
    subs.pop('missing')
    if len(subs.keys()) > 1:
        return subs

