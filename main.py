from drug_finder import DrugFinder
from pubmed_impl import PubmedImpl
from spacy_impl import SpacyRecognizer
from drugs_for_disease_dict import DrugsForDiseaseDict


pubmed = PubmedImpl()

diseaseQuery = "hepatitis"  # will only work if the string is a single word because of tokenization
drugDict = DrugsForDiseaseDict(diseaseQuery)

maxPapers = 200  # limit the number of papers retrieved
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
