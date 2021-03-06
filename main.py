from pubmed_connector import *
from networkx_graph import *  # Implementation der Darstellung


def addDict(dict1, dict2):
    """
    :param dict1: Dictionary
    :param dict2: Dictionary
    :return: Dictionary mit addierte Values bei Shared Keys
    """
    result = {}
    for key in dict1:
        if key in dict2:
            result[key] = dict1[key] + dict2[key]
        else:
            result[key] = dict1[key]
    for key in dict2:
        if key not in dict1:
            result[key] = dict2[key]
    return result


def main():

    current_diseases = ["parkinson"]
    max_paper = 200
    max_iterations = 2
    top_drug_limit = 30
    top_disease_limit = 15
    dictResult = DictCreator()

    for i in range(max_iterations):

        print("==== begin sequence {i} ====".format(i=i))

        # Pubmed Anfragen über alle Krankheiten in current_diseases:
        # Top x der Medikamente aus erster Anfrage (max_paper = Anzahl Paper)
        resultDiseases = getDrugs(current_diseases, max_paper)

        # Filterung aller Medikamente in den Artikeln
        top_drugs = []
        for disease in resultDiseases:
            dictResult.addNewDisease(disease, resultDiseases[disease])
            # Rückgabe der Top x Medikamente für Krankheit x
            top_drugs += dictResult.getTopEntriesOfDict(disease, top_drug_limit)

        print(top_drugs)

        if i != max_iterations - 1:

            # Pubmed Anfragen über alle Medikamente in top_drugs
            resultDrugs = getDiseases(top_drugs, max_paper)

            # Herausfinden aller Krankheiten in den Papern
            temp_current_diseases = {}
            for drug in resultDrugs:
                temp_current_diseases = addDict(temp_current_diseases,
                                                dictResult.getNewDiseasesFromDrug(resultDrugs[drug]))

            current_diseases_sorted_asc = sorted(temp_current_diseases.items(), key=lambda x: x[1], reverse=True)

            # Rausfiltern von falschen Einträgen
            dictResult.filter_diseases(current_diseases_sorted_asc)

            # Ausgabe aller Krankheiten nach Auftreten sortiert
            print(current_diseases_sorted_asc)

            # Pubmed Anfrage: Top 20-50 Krankheiten
            current_diseases = [el[0] for el in current_diseases_sorted_asc[:top_disease_limit]]

    # Knoten mit nur 1 Kante entfernen oder Threshold einbauen?

    print(dictResult.dictStorage)

    # Entfernt alle einträge mit Kookkurrenz von 1
    for disease in dictResult.dictStorage:
        for drug in list(dictResult.dictStorage[disease].keys()):
            if dictResult.dictStorage[disease][drug] == 1:
                dictResult.dictStorage[disease].pop(drug)

    # Erstellen des Graphen durch networkx
    g = graph(dictResult.getDict())

    # Zeichnen des Graphen mitels fa2
    forceAtlas2Impl(g, dictResult.getDict())


if __name__ == "__main__":
    main()
