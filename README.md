# Rescale-Backend-Assignment

##Build Your Own Web Crawler

## Description
- `web_crawler.py`: Source code file for the main application
- `test.py`: The file that shows it works as expected.

## Usage
- `web_crawler.py`: $ python3 web_crawler.py https://www.rescale.com
- `test.py`: $ python3 test.py

## Design
- First we import all the libraries for crawling. 
- We then set up a WebScraper class to create our web crawler. 
- Next, we write a basic link parser function i.e parsing_links. The goal here is to extract all of a sites internal links and not to pull out any external links. 
- Now we define the call back function i.e post_scrape_callback. 
- Now, we define a function which will be used to scrape the page i.e scrape_page. 
- Finally, The run_scraper function brings all of our previous work together and manages our thread pool.


##Performance
When testing this script on several sites with efficient servers, I was able to crawl several thousand URLs a minute. 

### Comment
Thank you for taking time to review the code and giving me this opportunity. 
