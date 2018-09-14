import rsstosteem.config as config
import rsstosteem.webscrapping

from steem import Steem

# Connect to Solarcoin
steemaccount=Steem(keys=[config.steemaccount, config.steemkey])

Scrap = DrupalScrap()
Steem.post(article)

