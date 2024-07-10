import requests
from bs4 import BeautifulSoup

def marketwatch():
    url = 'https://www.marketwatch.com/latest-news'
    headers = {
    'user-agent': 'Mozilla/5.0 (WIndows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.select('[class^="element element--article"]')
    for article in articles:
        if not article.select_one('h3') or not article.select_one('.article__timestamp'):
            continue
        
        headline = article.select_one('h3').text
        timestamp = article.select_one('.article__timestamp').text.strip()
        
        print(headline, timestamp)

marketwatch()
