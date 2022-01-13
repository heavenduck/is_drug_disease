from drug_finder import DrugFinder
from exporter import Exporter
from pubmed_impl import PubmedImpl
from spacy_impl import SpacyRecognizer
from drugs_for_disease_dict import DrugsForDiseaseDict


pubmed = PubmedImpl()

#disease_list_string = input("Enter a list of diseases to query for seperated by ', '")
disease_list_string = 'hepatitis, cancer, diabetes'

disease_list = disease_list_string.split(", ")

exporter = Exporter()

for disease in disease_list:
    diseaseQuery = disease  # will only work if the string is a single word because of tokenization

    # drugDict contains the name of the disease (.disease_name), the co-occurrence dictionary (.drug_dict)
    # and the odds ratio dictionary (.odds_ratio_dict)
    drugDict = DrugsForDiseaseDict(diseaseQuery)

    maxPapers = 100  # limit the number of papers retrieved
    myQuery = diseaseQuery + "[tiab]"  # query in title and abstract
    records = pubmed.getPapers(myQuery, maxPapers, 'xxx.xxx@mailbox.tu-dresden.de')

    # Concatenate Abstracts to one long string
    text: str = ''
    for r in records:
        if 'AB' in r:
            text += (r['AB'])

    # Named entity recognition by spacy
    # sp = SpacyRecognizer()
    # print(sp.qualify_text(text=text))

    # Fill drugDict with co-occurrences in text
    drug_finder = DrugFinder()
    drug_finder.qualify_text(text=text, drug_dict=drugDict)
    exporter.add_to_export(disease, drugDict.drug_dict)
    print(drugDict.drug_dict)

exporter.export(1)
