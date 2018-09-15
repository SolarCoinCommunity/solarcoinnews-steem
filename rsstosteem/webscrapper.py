#!/usr/env python

from rssparser import buildlist

import urllib.request as req

from bs4 import BeautifulSoup
from tomd import Tomd


# Function to scrap the content from the SolarCoin site

def DrupalScrap():
    links = buildlist()
    for item in links:
        get_site = req.Request(item)
        with req.urlopen(get_site) as response:
            site_content = response.read()
            soup = BeautifulSoup(site_content, 'html.parser')
            # Position on the article text box
            for img in soup.find_all('img'):
                img.decompose()
            header_box = soup.find('h1', attrs={'class': 'page-title'})
            article_box = soup.find('div', attrs={'class': 'node__content'})
            article_markdown = Tomd(str(article_box)).markdown
            page_title = Tomd(str(header_box)).markdown
            # permalink_nospace = header_box.replace(" ", "_")
            # permalink = permalink_nospace.lower()
            article = (page_title, article_markdown)
    return article
