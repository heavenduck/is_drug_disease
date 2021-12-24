from pubmed_impl import PubmedImpl
from spacy_impl import SpacyRecognizer


pubmed = PubmedImpl()

maxPapers = 30  # limit the number of papers retrieved
myQuery = "cancer" + "[tiab]"  # query in title and abstract
records = pubmed.getPapers(myQuery, maxPapers, 'franz.rodestock@mailbox.tu-dresden.de')

# Concatenate Abstracts to one long string
text: str = ''
for r in records:
    if 'AB' in r:
        text += (r['AB'])

# Named entity recognition by spacy
sp = SpacyRecognizer()
print(sp.qualify_text(text=text))
