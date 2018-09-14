#!/usr/env python

import rsstosteem.config as config
from rsstosteem.rssparser import buildlist

import urllib.request as req

from bs4 import BeautifulSoup
from tmod import Tmod


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
            header_box = soup.find('div', attrs={'class': 'page-title'})
            article_box = soup.find('div', attrs={'class': 'node__content'})
            article_markdown = Tmod(article_box).markdown
            header_box = Tmod(header_box).markdown
            permalink_nospace =header_box.replace(" ", "_")
            permalink = permalink_nospace.lowercase()
            article = (header_box, article_box, permalink)
    return article

