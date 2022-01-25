# Dokumentation des Projektes - Deutsch

In diesem Projekt gibt es 2 Möglichkeiten sich Daten auszugeben. 
Die einfachste ist schon vorhandene berechnete Daten zu verwenden und dieser mittels einer Ausgabe Skriptes zu plotten. 
Die zweite Möglichkeit besteht im neuen Erzeugen dieser Daten mittels mehrere PubMed Anfragen.
Dies kann aufgrund von nicht unterstütztem Multithreading bei höheren Parametern sehr lange dauern.   

## Ausgabe von vorhanden Daten

Alle schon vorberechneten Daten befinden sich im Ordner *graphData*.
Um einen berechneten Datensatz zu verwenden, muss die Datei *data.py* im Ordner *graphData* ersetzt werden. 
Dafür muss nur eine Kopie aus einen der Ordner ausgewählt werden und die Ursprungsdatei ersetzen.
Die Struktur baut sie wie folgt auf:
```
project
│   data_plot.py
└─── graphData
│   │   data.py
│   └───data
│       └───<Krankheit>
│           └───<Parameter> (Falls diese gegeben sind)
│               │   data.py        
```
 Bevor nun data_plot.py ausgeführt werden kann, müssen noch die nötigen Anforderungen installiert werden. 
 Nur für die Ausgabe gibt das requirements.visual.txt .