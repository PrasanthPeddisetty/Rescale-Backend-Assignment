
# Importing all the libraries for crawling
import sys
import requests
from queue import Queue, Empty
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup


# Setting up WebScraper class
class WebScraper:

    def __init__(self, base_url):

        self.base_url = base_url
        self.root_url = '{}://{}'.format(urlparse(self.base_url).scheme, urlparse(self.base_url).netloc)
        self.pool = ThreadPoolExecutor(max_workers=20)
        self.scraped_pages = set([])
        self.to_crawl = Queue()
        self.to_crawl.put(self.base_url)

# Writing link parser to extract all of a sites internal links
    def parsing_links(self, html):
        b_soup = BeautifulSoup(html, 'html.parser')
        links = b_soup.find_all('a', href=True)
        for link in links:
            url = link['href']
            if url.startswith('/') or url.startswith(self.root_url):
                url = urljoin(self.root_url, url)
                if url not in self.scraped_pages:
                    self.to_crawl.put(url)

# Writing a method to extract the data we want from the site you are crawling.
    def scrape_data(self, html):
        return

# Defining the call back function
    def post_scrape_callback(self, res):
        result = res.result()
        if result and result.status_code == 200:
            self.parsing_links(result.text)
            self.scrape_data(result.text)

# Scraping the page
    def scrape_page(self, url):
        try:
            res = requests.get(url, timeout=(3, 30))
            return res
        except requests.RequestException:
            return

# Run scraper function that brings all of the previous work together and manage the thread pool.
    def run_scraper(self):
        while True:
            try:
                target_url = self.to_crawl.get(timeout=60)
                if target_url not in self.scraped_pages:
                    print("Structured URL crawling: {}".format(target_url))
                    self.scraped_pages.add(target_url)
                    job = self.pool.submit(self.scrape_page, target_url)
                    job.add_done_callback(self.post_scrape_callback)
            except Empty:
                return
            except Exception as e:
                print(e)
                continue


if __name__ == '__main__':
    s = WebScraper("https://www.rescale.com")
    s.run_scraper()



