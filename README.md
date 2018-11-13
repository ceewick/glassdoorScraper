# glassdoorScraper
1.0 is simple, but the subRatings do not work
2.0 is a little more complex, but subRatings work, and it utilizes SQLite database for storing

To Do:
- Add CSV export option in CLI
- Use PhantomJS, or something else, to increase speed of scrape
- Fix UserAgent errors (note: occasionally the UserAgent will fail, and program won't work)... simply re-run
- At somepoint the getPages function (or something) breaks (apparently). Need to fix for huge companies
