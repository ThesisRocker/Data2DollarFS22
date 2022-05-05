import twint

#configuration
c = twint.Config()
c.Username = "ABack"
c.Since = "2010-01-01"
c.Until = "2022-03-09"
c.Output = "ZbindenPatrick.json"

#running search
twint.run.Search(c)