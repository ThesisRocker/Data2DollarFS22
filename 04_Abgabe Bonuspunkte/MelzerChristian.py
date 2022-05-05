# Importing necessary libaries
import twint

# Creating scraper
c = twint.Config()
c.Username = "ABack"
c.Since = "2010-01-01"
c.Until = "2022-03-09"

c.Store_json = True
c.Output = "MelzerChristian.json"

twint.run.Search(c)
