# import psycopg2
import sqlite3

import settings

conn = sqlite3.connect(settings.database) #database=settings.database, host=settings.host, user=settings.user)
cur = conn.cursor()

class ReviewRecord(object):
    ''' docstring for ReviewRecord'''
    def __init__(self,reviewNumber,overallRating,date,summary,pros,cons,adviceToManagement,employeeType,position,reviewLink, workLife, culture, careerOpps, compBenefits, management):
        super(ReviewRecord, self).__init__()
        self.reviewNumber = reviewNumber
        self.overallRating = overallRating
        self.date = date
        self.summary = summary
        self.pros = pros
        self.cons = cons
        self.adviceToManagement = adviceToManagement
        self.employeeType = employeeType
        self.position = position
        self.reviewLink = reviewLink
        self.workLife = workLife
        self.culture = culture
        self.careerOpps = careerOpps
        self.compBenefits = compBenefits
        self.management = management

    def save(self):
        cur.execute('INSERT INTO reviews (reviewNumber, overallRating, date, summary, pros, cons,adviceToManagement, employeeType, position, reviewLink, workLife, culture, careerOpps, compBenefits, management) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (self.reviewNumber, self.overallRating, self.date, self.summary, self.pros, self.cons, self.adviceToManagement, self.employeeType, self.position, self.reviewLink, self.workLife, self.culture, self.careerOpps, self.compBenefits, self.management))
        conn.commit()
        return cur.fetchall()
    

def establish_table():
    # setup tables
    cur.execute("DROP TABLE IF EXISTS reviews")
    cur.execute("""CREATE TABLE reviews (
        id INTEGER PRIMARY KEY ASC,
        reviewNumber INTEGER,
        overallRating REAL,
        date TEXT,
        summary TEXT,
        pros TEXT,
        cons TEXT,
        adviceToManagement TEXT,
        employeeType TEXT,
        position TEXT,
        reviewLink TEXT,
        workLife REAL, 
        culture REAL, 
        careerOpps REAL, 
        compBenefits REAL,
        management REAL
    );""")
    conn.commit()

def close_database():
    conn.close()

# if __name__ == '__main__':
#     conn = sqlite3.connect(settings.database) #database=settings.database, host=settings.host, user=settings.user)
#     cur = conn.cursor()
#     # setup tables
#     cur.execute("DROP TABLE IF EXISTS reviews")
#     cur.execute("""CREATE TABLE reviews (
#         id INTEGER PRIMARY KEY ASC,
#         reviewNumber INTEGER,
#         overallRating REAL,
#         date TEXT,
#         summary TEXT,
#         pros TEXT,
#         cons TEXT,
#         adviceToManagement TEXT,
#         employeeType TEXT,
#         position TEXT,
#         reviewLink TEXT
#     );""")
#     conn.commit()
#     conn.close()