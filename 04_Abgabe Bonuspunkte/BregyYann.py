import twint

# Konfigurieren der Abfrage
c = twint.Config()
c.Username = 'ABack'
c.Since = '2010-01-01'

# Daten im json format speichern (leider nur 20-40 Resultate je nach Abfrage)
c.Store_json = True
c.Output = "BregyYann.json"

# Ausführen der Suche
twint.run.Search(c)