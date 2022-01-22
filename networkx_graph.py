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
    
    # remove all nodes with a degree lower or equal 1
    to_be_removed = [x for x in graphX.nodes() if graphX.degree(x) <= 1]

    for x in to_be_removed:
        graphX.remove_node(x)

    return graphX

def forceAtlas2Impl(G, diseases):
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
    val_map = {}
    name = {}
    for d in diseases:
        val_map[d] = 'red'
        name[d] = d
    values = [val_map.get(node, '#3587a0') for node in G.nodes()]
    
    fig = plt.figure()
    
    edges,weights = zip(*nx.get_edge_attributes(G,'weight').items())
    nx.draw_networkx_edges(G, positions, edge_color="#D6F599", edge_cmap=plt.get_cmap('plasma'), alpha=0.1)
    nx.draw_networkx_nodes(G, positions, node_size=15, node_color=values, alpha=0.5)
    
    for label in positions:
      positions[label] = (positions[label][0] , positions[label][1] + 3 )

    nx.draw_networkx_labels(G, positions, labels=name,  font_size=8, font_color="#AAA")
    
    fig.set_facecolor("black")
    plt.axis('off')
    


    #plt.savefig('books_read.png', dpi=5000)
    plt.show()
