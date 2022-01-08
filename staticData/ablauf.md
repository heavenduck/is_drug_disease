# Themen
- blood-cancer
- diabetic

# Datengrundlage für das "lernen" des Algorithmus
- Pubmed 
- Klassifizieren nach Disease und Drug
- Wie viele BSP brauchen wir?

# Methode
- Kookurrenz als Hauptmethode 
- Idee: In der Zusammenfassung auf die Schwierigkeit des Regex Ausdruckes eingehen und einen einfachen Ausdruck als Bsp. zeigen
  - erleichert uns die Aufgabe
  - scheint als hätten wir viel Zeit damit verbracht

# Metriken
- (dafür muss man manuell klassifizieren, eventuell relativ aufwendig)
- Recall
- prec
- F-maß

# Arbeitsschritte:
- Datenbasis abrufen (Done: Arndt und Franz)
- Text nach Drugs und Disease klassifizieren (Done: Franz)
- Duplicate entfernen
- Satzweise kookurrenz??
- Threshhold festlegen, dann die größten Relationen visuell (per Graph?) darstellen
- Präsentation:
  - Vorstellung unserer Pipeline
  - Nettes Ergebnis präsentieren
  - Metriken auswerten

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


  
