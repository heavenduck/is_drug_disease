from drug_finder import DrugFinder
from exporter import Exporter
from pubmed_impl import PubmedImpl
from spacy_impl import SpacyRecognizer
from drugs_for_disease_dict import DrugsForDiseaseDict
from main_med import *

current_diseases = ["SARS-Cov-2"]
max_paper = 100
max_iterations = 2
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
    current_diseases = []
    for drug in resultDrugs:
        current_diseases += dictResult.getNewDiseasesFromDrug(result[drug])

# TODO Pubmed Anfrage: Top 20-50 Krankheiten
# Knoten mit nur 1 Kante entfernen oder Threshold einbauen?
# Zeichnen der Knoten
