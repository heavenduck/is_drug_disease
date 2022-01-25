import networkx as nx
from fa2 import ForceAtlas2
import matplotlib.pyplot as plt
import matplotlib.colors as colors


def graph(data):
    """ Erstellung des Graphen 
    :param data: Dict mit allen Daten der Kranheiten in Beziehung zu den Medikamenten { <Krankheit> : {<Med1>:<Anzahl> , ...}} 
    """
    graphX = nx.Graph()

    for disease in data:
        for drug in data[disease]:
            graphX.add_edge(disease, drug, weight=data[disease][drug])

    # remove all nodes with a degree lower or equal 1
    to_be_removed = [x for x in graphX.nodes() if graphX.degree(x) <= 1]

    for x in to_be_removed:
        graphX.remove_node(x)

    return graphX


def forceAtlas2Impl(G, diseases, show_all_labels=False):
    """ Zeichnen des Graphen mittels fa2
    :param G: networkx Graph
    :param diseases: Dict von allen Krankheiten und Medizin
    :param show_all_labels: anzeigen aller Labels oder nur der Krankheiten
    """

    forceatlas2 = ForceAtlas2(
        # Behavior alternatives
        outboundAttractionDistribution=True,  # Dissuade hubs
        linLogMode=False,
        adjustSizes=False,
        edgeWeightInfluence=1.0,

        # Performance
        jitterTolerance=1.0,  # Tolerance
        barnesHutOptimize=True,
        barnesHutTheta=1.2,
        multiThreaded=False,

        # Tuning
        scalingRatio=2.0,
        strongGravityMode=False,
        gravity=1.0,

        # Log
        verbose=True)

    positions = forceatlas2.forceatlas2_networkx_layout(G, pos=None, iterations=2000)

    # Erstellung des Label Dicts
    name = {}
    if show_all_labels:
        for key in positions:
            name[key] = key
    else:
        for d in diseases:
            name[d] = d

    # Speicher für die Farben der Knoten
    values = [get_color_dict_for_disease(G, diseases).get(node, '#b3e6c3') for node in G.nodes()]

    fig = plt.figure()

    nx.draw_networkx_edges(G, positions, edge_color="#2a7e7b", edge_cmap=plt.get_cmap('plasma'), alpha=0.5)
    nx.draw_networkx_nodes(G, positions, node_size=15, node_color=values, alpha=1)

    # Setzt ein Offset an die Labels somit nicht direkt auf dem Knoten
    for label in positions:
        positions[label] = (positions[label][0], positions[label][1] + 1)

    nx.draw_networkx_labels(G, positions, labels=name, font_size=8, font_color="#AAA")

    # Hintergrundfarbe auf Schwarz setzen
    fig.set_facecolor("black")
    plt.axis('off')

    plt.show()


def get_color_dict_for_disease(G, disease):
    dmax = 0
    dmin = 999999999

    for node in G.nodes():
        if node in disease:
            dmax = max(G.degree(node), dmax)
            dmin = min(G.degree(node), dmin)

    norm = colors.Normalize(vmin=dmin, vmax=dmax)

    node_colors = {}
    cmap = plt.get_cmap('autumn')
    for node in G.nodes():
        if node in disease:
            node_colors[node] = colors.to_hex(cmap(1 - norm(G.degree(node))))
        else:
            node_colors[node] = "#61b33c"
    return node_colors
