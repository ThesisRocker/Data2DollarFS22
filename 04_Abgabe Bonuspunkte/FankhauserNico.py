import twint

# Configure Data (was soll heruntergeladen werden)
c = twint.Config()
c.Username = "ABack"
c.Since = "2010-01-01"

# Store Data (Format und Dateiname)
c.Store_json = True
c.Output = "FankhauserNico.json"

# Run
twint.run.Search(c)
