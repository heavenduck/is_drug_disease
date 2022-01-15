from pubmed_connector import *

current_diseases = ["SARS-Cov-2"]
max_paper = 100
max_iterations = 1
dictResult = DictCreator()

for i in range(max_iterations):

    # Pubmed Anfragen über alle Krankheiten in current_diseases:
    # Top x der Medikamente aus erster Anfrage (max_paper = Anzahl Paper)
    resultDiseases = getDrugs(current_diseases, max_paper)

    # Filterung aller Medikamente in den Artikeln
    top_drugs = []
    for disease in resultDiseases:
        dictResult.addNewDisease(disease, resultDiseases[disease])
        # Rückgabe der Top x Medikamente für Krankheit x
        top_drugs += dictResult.getTopEntriesOfDict(disease, 10)
    

    # Pubmed Anfragen über alle Medikamente in top_drugs
    resultDrugs = getDiseases(top_drugs, max_paper)
    
    # Herausfinden aller Krankheiten in den Papern
    current_diseases = {}
    for drug in resultDrugs:
        current_diseases = addDict(current_diseases, dictResult.getNewDiseasesFromDrug(resultDrugs[drug]))
    

# TODO Pubmed Anfrage: Top 20-50 Krankheiten
# Knoten mit nur 1 Kante entfernen oder Threshold einbauen?
# Zeichnen der Knoten

# datadict = drug_dict.getDictNormalized(1)
# g = graph(datadict)
# forceAtlas2Impl(g)


def addDict(dict1, dict2):
    """
    :param dict1: Dictionary
    :param dict2: Dictionary
    :return: Dictionary mit addierte Values bei Shared Keys
    """
    result = {}
    for key in dict1:
        if key in dict2:
            result[key] = dict1[key]+dict2[key]
        else:
            result[key] = dict1[key]
    for key in dict2:
        if key not in dict1:
            result[key] = dict2[key]
    return result
