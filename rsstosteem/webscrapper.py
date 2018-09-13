import config
import urllib.request as req

from bs4 import BeautifulSoup

from rsstosteem.rssparser import buildlist

# Function to scrap the content from the SolarCoin site

def DrupalScrap:
    for item in links:
        get_site= req.Request(links[item])
        with req.urlopen(get_site) as response:
            site_content = response.read()
            soup = BeautifulSoup(site_content, 'html.parser')
            # Position on the article text box
            article_box= soup.find('div', attrs={'class': 'node__content'})
return article_box

