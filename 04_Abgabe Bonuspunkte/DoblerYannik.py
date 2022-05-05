import twint

# Configure
c = twint.Config()
c.Username = "ABack"
c.Since = "2010-01-01"
c.Until = "2022-03-08"

# Store
c.Store_json = True
c.Output = "DoblerYannik.json"

# Run
twint.run.Search(c)