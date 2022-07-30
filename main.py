import requests
import re
from bs4 import BeautifulSoup


def find_articles(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    articles_links = soup.find_all('a', href=re.compile(r'^.*news\/?(.*\/)?[(\d{5,})]'))
    articles_lst = []
    for link in articles_links:
        article_href = link.get('href')
        # print(link.get('href'))
        articles_lst.append(article_href)
    return articles_lst


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    find_articles('https://www.finews.com/')
