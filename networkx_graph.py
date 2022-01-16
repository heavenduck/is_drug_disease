import networkx as nx
from fa2 import ForceAtlas2
import matplotlib.pyplot as plt

def graph( data):
    """ Erstellung des Graphen 
    :param data: Dict mit allen Daten der Kranheiten in Beziehung zu den Medikamenten { <Krankheit> : {<Med1>:<Anzahl> , ...}} 
    """
    graphX = nx.Graph()

    for disease in data:
        for drug in data[disease]:
            graphX.add_edge(disease , drug , weight=data[disease][drug])

    return graphX

def forceAtlas2Impl(G):
    """ Zeichnen des Graphen mittels fa2
    :param G: networkx Graph
    """
    forceatlas2 = ForceAtlas2(
        # Behavior alternatives
        outboundAttractionDistribution=True,  # Dissuade hubs
        linLogMode=False,  # NOT IMPLEMENTED
        adjustSizes=False,  # Prevent overlap (NOT IMPLEMENTED)
        edgeWeightInfluence=1.0,

        # Performance
        jitterTolerance=1.0,  # Tolerance
        barnesHutOptimize=True,
        barnesHutTheta=1.2,
        multiThreaded=False,  # NOT IMPLEMENTED

        # Tuning
        scalingRatio=2.0,
        strongGravityMode=False,
        gravity=1.0,

        # Log
        verbose=True)

    positions = forceatlas2.forceatlas2_networkx_layout(G, pos=None, iterations=2000)
    nx.draw_networkx_nodes(G, positions, node_size=20, node_color="black", alpha=0.4)
    nx.draw_networkx_edges(G, positions, edge_color="darkblue", alpha=0.1)
    plt.axis('off')
    plt.show()
