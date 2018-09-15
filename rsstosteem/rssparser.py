import config

import feedparser

parse = feedparser.parse(config.rssurl)


def buildlist():
    links = []
    posts = parse.entries
    for post in posts:
        links.append(post.link)

    return links
