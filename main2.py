#from pubmed_connector import *
from networkx_graph import *  # Implementation der Darstellung
from graphData.data_2 import get_data
# Erstellen des Graphen durch networkx 
g = graph(get_data())

# Zeichnen des Graphen mitels fa2
forceAtlas2Impl(g, get_data())


