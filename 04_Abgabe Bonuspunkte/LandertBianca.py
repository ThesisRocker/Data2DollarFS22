import twint

c = twint.Config()
c.Username = "ABack"
c.Since = '2010-01-01'
c.Output = "ABack.json"

twint.run.Search(c)
