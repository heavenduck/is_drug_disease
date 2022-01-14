import networkx as nx
from fa2 import ForceAtlas2
import matplotlib.pyplot as plt

def graph(self,  dict ):
    G = nx.Graph()

    for disease in dict.keys():
        for drug in dict.get(disease).keys():
            G.add_edge(disease, drug, dict.get(disease).get(drug))

    return G

def forceAtlas2Impl(G):
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
    nx.draw_networkx_nodes(G, positions, node_size=20, with_labels=False, node_color="blue", alpha=0.4)
    nx.draw_networkx_edges(G, positions, edge_color="green", alpha=0.05)
    plt.axis('off')
    plt.show()
