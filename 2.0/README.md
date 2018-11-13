Create 2.0 which now (finally) correctly scrapes and parses subRatings from reviews. 

2.0 scrapes and loads them into a SQLite3 database. 

In settings.py = Edit the aite URL that you want to scrape, along with database name

To Do:
- Add CSV export option in CLI
- Use PhantomJS, or something else, to increase speed of scrape
- Fix UserAgent errors (note: occasionally the UserAgent will fail, and program won't work)... simply re-run
- At somepoint the getPages function (or something) breaks (apparently). Need to fix for huge companies
