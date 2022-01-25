# Documentation of the project - English
In this project there are 2 ways to output data. 
The simplest is to use already calculated data and plot it using an output script. 
The second way is to generate new data using multiple PubMed queries.
This can take a long time due to unsupported multithreading with higher parameters. 

## Output of existing data

All already precalculated data is located in the *graphData* folder.
To use a calculated data set, the *data.py* file in the *graphData* folder must be replaced. 
To do this, just select a copy from one of the folders and replace the original file.

The structure is as follows:
```
project
│   data_plot.py
└─── graphData
│   │   data.py
│   └───data
│       └───<disease>
│           └───<parameter> (if known)
│               │   data.py        
```
! Note ! The Python library fa2 can only be used with Python 3.8.
 
Before *data_plot.py* can be executed, the necessary requirements have to be installed. 
The requirements.visual.txt includes necessary libraries.

## Output of self-requested data

Under Construction



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
! Hinweis ! Die Python Bibliothek fa2 ist nur bei Python 3.8 verwendbar
 
Bevor nun data_plot.py ausgeführt werden kann, müssen noch die nötigen Anforderungen installiert werden. 
Nur für die Ausgabe gibt das requirements.visual.txt.


## Ausgabe von selbst angefragten Daten

Under Construction