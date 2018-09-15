import rsstosteem.config as config
import rsstosteem.webscrapping

from steem import Steem

# Connect to Solarcoin
steemaccount=Steem(keys=[config.steemaccount, config.steemkey])

Scrap = DrupalScrap()
try:
    Steem.post(title=article[0], body=article[1], tags=['solarcoin'], self_vote=True )
except:
    print("An exception ocurred")


