import twint

# Configure Data
c = twint.Config()
c.Username = "ABack"
c.Since = "2010-01-01"

# Store Data as json file
c.Store_json = True
c.Output = "VoegeliDaniel.json"

# Run the Program
twint.run.Search(c)
