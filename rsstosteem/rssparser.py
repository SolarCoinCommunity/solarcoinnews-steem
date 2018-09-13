
import config

import feedparser

parse = feedparser.parse(rssurl)

def buildlist:
    posts=parse.entries
    for post in posts:
        links.additem(post.link)

    return links


