Finally created 2.0 which now correctly scrapes and parses subRatings (finally) from the reviews. 

2.0 scrapes and loads results into a SQLite3 database. 

settings.py = Edit this file to choose site URL that you want to scrape, along setting the database name

To Do:
- Add CSV export option in CLI
- Use PhantomJS, or something else, to increase speed of scrape
- Fix UserAgent errors (note: occasionally the UserAgent will fail, and program won't work)... simply re-run
- At somepoint, apparently the code breaks when crawling a company with too many pages. If true, need to fix getPages() for larger companies
