import twint
# Configure Data
c = twint.Config()
c.Username = "ABack"
c.Since = "2010-01-01"
# Store Data
c.Store_json = True
c.Output = "BienzCornel.json"
# Run Programm
twint.run.Search(c)
