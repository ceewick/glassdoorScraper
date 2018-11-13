Web scraper or crawler to extract glassdoor (glassdoor.com) reviews for a company. You'll need to change the payload with your username and password. 

gDoorReviews.py is my first "major" (still elementary but I'm happy with it) scraping project. It should be able to scrape any reviews pages. 

Currently, you do have to put in the last part of the URL manually (that represents review page being scraped).

When opening the CSV.. better to not delineate with ';' because some answers have that

** Subrviews are not accurate, at all. Cannot figure out how to account for when a subreview is missing, while still keeping it's place. Help appreciated with that. 

todo:
    - Add automatic page traversal
    - Add the "Recommends", "Company Outlook", "Approves of CEO" section
    - Sentiment analysis

Initial commit 2x months ago, deleted and repushed, added randomUserAgents.py and getPages().
