#from pubmed_connector import *
from networkx_graph import *  # Implementation der Darstellung
from data import get_data
# Erstellen des Graphen durch networkx 
g = graph(get_data())

# Zeichnen des Graphen mitels fa2
forceAtlas2Impl(g, get_data())


