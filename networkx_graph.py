import networkx as nx
from fa2 import ForceAtlas2
import matplotlib.pyplot as plt

def graph( data , threshold=0):
    graphX = nx.Graph()

    for disease in data:
        for drug in data[disease]:
            if data[disease][drug] > threshold:
                graphX.add_edge(disease , drug , weight=data[disease][drug])

    return graphX

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
    nx.draw_networkx_nodes(G, positions, node_size=20, node_color="black", alpha=0.4)
    nx.draw_networkx_edges(G, positions, edge_color="darkblue", alpha=0.1)
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    dic = {'influenza': {'gallate': 0.14285714285714285, 'antibiotic': 1.0, 'antibacterials': 0.14285714285714285, 'antibiotics': 0.2857142857142857, 'RTIs': 0.14285714285714285, 'Lachnospiraceae': 0.14285714285714285, 'Ruminococcaceae': 0.14285714285714285, 'Ruminococcus': 0.14285714285714285, 'Capsaicin': 0.14285714285714285, 'oseltamivir': 0.5714285714285714, 'Tamiflu': 0.14285714285714285, 'zanamivir': 0.14285714285714285, 'January': 0.2857142857142857, 'diuretics': 0.14285714285714285, 'vasodilators': 0.14285714285714285, 'potato dextrose agar (PDA)': 0.14285714285714285, 'subglobose': 0.14285714285714285, 'ITS4': 0.14285714285714285, 'conidial': 0.14285714285714285, 'LSL3f2': 0.14285714285714285, 'hexylthiol': 0.14285714285714285, 'malachite green isothiocyanate (MGITC)': 0.14285714285714285, 'November': 0.14285714285714285, 'sialic acid receptor analogues': 0.14285714285714285, 'vRNPs': 0.42857142857142855, 'IAV antivirals targeting': 0.14285714285714285, 'September': 0.14285714285714285, 'Cyrillicnubis': 0.14285714285714285, 'diphenyltetrazolium bromide (MTT)': 0.14285714285714285, 'intratumoral': 0.14285714285714285, 'PD-1 inhibitors': 0.14285714285714285, 'October': 0.14285714285714285, 'Amparo': 0.14285714285714285, 'Pesquisa': 0.14285714285714285, 'December': 0.14285714285714285, 'February': 0.42857142857142855}}

    forceAtlas2Impl(graph(dic))
