# Themen
- Startkrankheit: Cancer oder SARS-CoV-2 oder Epstein-Barr

# Algorithmen
- Pubmed 
- Kranheitserkennung über spacy
- Medikamenterkennung über med7
- Wie viele BSP brauchen wir?


# Methode
- Kookurrenz als Hauptmethode 
- Idee: In der Zusammenfassung auf die Schwierigkeit des Regex Ausdruckes eingehen und einen einfachen Ausdruck als Bsp. zeigen
  - erleichert uns die Aufgabe
  - scheint als hätten wir viel Zeit damit verbracht

# Arbeitsschritte:
- Datenbasis abrufen (Done: Arndt und Franz)
- Text nach Drugs und Disease klassifizieren (Done: Franz)
- Präsentation:
  - Vorstellung unserer Pipeline
  - Nettes Ergebnis präsentieren
  - Metriken auswerten

# Pipline
- Pubmed Anfrage: eine Krankheit (300-500 Paiper)
- Filterung aller Medikamente in den Artikeln
- Pubmed Anfrage: Top 20 der Medikamente aus erster Anfrage (300-500 Paiper)
- Herausfinden aller Krankheiten in den Paipern
- Pubmed Anfrage: Top 20-50 Krankheiten
- Erstellung Dict aus der Letzen Anfrage und deren Auswertung
- Knoten mit nur 1 Kante entfernen oder Threshhold einbauen?
- Zeichnen der Knoten 


# Aufbau des Dicts zur Darstellung
- 2 Listen: nodes + links
- Bsp:

``` javascript
var nodes = [
	{ id: <name:str> , group: <groupnummer:int> , label : <Bezeichnung im Graphen>}
]

var links = [
	{ target: <link nach id> , source: < link von id> , strength : <Häufigkeit normiert>} 
]
```

- id 	- Name von der Krankheit oder der Arzenei (unique)
- group - 0 = Krankheit , 1 = Arzenei
- label - Bezeichnung im Graphen

- target 	- ID des Knotens zu dem die Kante hin führt
- source 	- ID des Knotens von dem die Kante kommt
- strength 	- normierte Anzahl der Auftritte zwischen 0 und 1


  
