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
