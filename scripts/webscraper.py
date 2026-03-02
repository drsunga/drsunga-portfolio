import requests
from bs4 import BeautifulSoup as bs
import json
from datetime import datetime
import random
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s [%(module)s] [%(funcName)s]: %(message)s')
console_handler.setFormatter(formatter)
log.addHandler(console_handler)

sourcename = "Hybrid War Tracker (HWT)"

def view_as_json(source, title, author, date, link, content):
    article_info = {
        "Source": source,
        "Title": title,
        "Author": author,
        "Date": date,
        "Link": link,
        "Content": content
    }
    article_json = json.dumps(article_info, ensure_ascii=False, indent=4)
    log.info(article_json)

def delay_scraping():
    global delay_counter
    delay_counter += 1
    rand = random.randint(2, 4)
    time.sleep(rand)
    return rand

def main_scraper():
    
    url = "https://hwt.lv/api/public/signals?limit=20"
    home_link = "https://hwt.lv/signals/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0^"
        }

    log.info("Fetching URL: %s", url)
    res = requests.get(url, headers=headers)
    page_data = res.json()
    if not page_data['signals']:
        log.warning("No data found at URL: %s", url)
        return
    
    all_scraped = True

    for idx, hwt_data in enumerate(page_data['signals']):
        log.info('Extracting contents...')

        # Title in json
        title_html = hwt_data['headline']
        if title_html is None:
            title_html = hwt_data['summary_short']
        title_soup = bs(title_html, 'html.parser')
        hwt_title = title_soup.get_text(strip=True)

        # Published date in json
        date_html = hwt_data['created_at']
        date_soup = bs(date_html, 'html.parser')
        hwt_date = date_soup.get_text(strip=True)

        # Author in json
        hwt_author = ''

        # Link in json
        hwt_id = str(hwt_data['id'])
        hwt_link =f'{home_link}{hwt_id}'

        # Content in json
        raw_content = {
            'category': hwt_data['category'],
            'subcategory': hwt_data['subcategory'],
            'summary_short': hwt_data['summary_short'],
            'description': hwt_data['description'],
            'country': hwt_data['country']
        },
        hwt_content = str(raw_content).replace("'", "").replace("({", "").replace("})", "").replace("},)", "")

        # Display the extracted information in JSON format
        view_as_json(sourcename, hwt_title, hwt_author, hwt_date, hwt_link, hwt_content)

        log.info('Collecting the next article in %s seconds...', delay_scraping())
        delay_scraping()

    if all_scraped:
        log.info("All data in the JSON file has been collected successfully.")
        delay_scraping()
        log.info("Closing...")
        delay_scraping()

if __name__ == "__main__":
    main_scraper()
