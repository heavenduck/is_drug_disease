""" Dieses Skript nutzt die Daten aus einem schon berechneten Dict und erstellt den Graphen"""

from networkx_graph import *  # Implementation der Darstellung
from graphData.data import get_data
from dict_creator import DictCreator


def main(labels_activ=False):
    dict_result = DictCreator()
    dict_result.dictStorage = get_data()

    for disease in dict_result.dictStorage:
        for drug in list(dict_result.dictStorage[disease].keys()):
            if dict_result.dictStorage[disease][drug] == 1:
                dict_result.dictStorage[disease].pop(drug)

    # Erstellen des Graphen durch networkx
    g = graph(dict_result.dictStorage)

    # Zeichnen des Graphen mittels fa2
    forceAtlas2Impl(g, dict_result.dictStorage, labels_activ)


if __name__ == "__main__":
    main(False)


