# Script that retreives all Hearthstone news articles that mentions Youtube or Twitch Drops

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import requests

# Variables
# path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
base_url = 'https://news.blizzard.com/'


def grab_links():
    temp = []
    url = base_url + 'en-us/hearthstone'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    text = soup.findAll('li', {'class': 'ArticleListItem'})
    for x in text[:2]:
        temp.append(x.findChild("a")['href'])
    return temp


def search_info(link):
    r = requests.get(base_url + link)
    soup = BeautifulSoup(r.content, "html.parser")
    text = soup.find('div', {'class': 'ArticleDetail-content'})

    if ("drops" in text.text) or ("Drops" in text.text):
        drops = True
    else:
        drops = False

    title = soup.find('h1', {'class': 'Heading Heading--articleHeadline ArticleDetail-title'}).text
    publish_date = soup.find('time', {'class': 'ArticleDetail-bylineDate'}).text

    return {'title': title,
            'link': base_url+link,
            'publish_date': publish_date,
            'active': drops
            }


def get_info():
    # Setup selenium
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--headless')
    # options.add_extension('block.crx')
    driver = webdriver.Chrome("chromedriver", options=options)
    driver.get(base_url + 'en-us/hearthstone')

    # Load more articles
    for i in range(3):
        # Random chance for it to be intercepted
        try:
            WebDriverWait(driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Load More')]"))).click()
        except TimeoutException:
            break
        except Exception as e:
            print(repr(e))
            print('Elements may not have loaded correctly, and some links may not have been caught.')
            print('Please rerun script to try again if any are missing.')

    soup = BeautifulSoup(driver.page_source, "html.parser")
    articles = soup.find_all('a', {'class': 'ArticleLink ArticleListItem-linkOverlay'})
    links = []

    driver.quit()

    # Grab links of individual articles and go through them

    for article in articles:
        links.append(article.get("href"))

    for link in links:
        print(search_info(link))


if __name__ == "__main__":
    # get_info()
    print(grab_links())
    pass