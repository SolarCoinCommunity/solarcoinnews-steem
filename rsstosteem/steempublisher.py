import rsstosteem.config as config

from steem import Steem

# Connect to Solarcoin
steemaccount=Steem(keys=[config.steemaccount, config.steemkey])

# Format from html to markdown
# info: https://github.com/gaojiuli/tomd
from tomd import Tomd

# Filter images and reformat for steemit


# Publish document

