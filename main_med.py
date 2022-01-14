from pubmed_impl import PubmedImpl
import spacy

class DictCreator():

  def __init__ (self):
    self.dictStorage = {}

  def getDict(self):
    return self.dictStorage
  
  def getDictNormalized(self , threshhold=0):

    dictStorageNorm = self.dictStorage

    for key in dictStorageNorm:
      max_apperance = max(dictStorageNorm[key].values())
      dictStorageNorm[key] = {key:(val/max_apperance) for key, val in dictStorageNorm[key].items() if val > threshhold}   
    
    return dictStorageNorm


  def addNewDisease(self , disease , doc_data):
    
    self.dictStorage[disease] = {}

    for entity in doc_data.ents:
      if entity.label_ == 'DRUG':
        if entity.text in self.dictStorage[disease]:
          self.dictStorage[disease][entity.text] += 1
        else:
          self.dictStorage[disease].update({ entity.text : 1}) 




pubmed = PubmedImpl()
drug_dict = DictCreator()

med7 = spacy.load("en_core_med7_lg")

diseaseQuery = 'influenza'


maxPapers = 50  # limit the number of papers retrieved
myQuery = diseaseQuery + "[tiab]"  # query in title and abstract
records = pubmed.getPapers(myQuery, maxPapers, 'xxx.xxx@mailbox.tu-dresden.de')

# Concatenate Abstracts to one long string
text: str = ''
for r in records:
  if 'AB' in r:
    text += (r['AB'])

# create distinct colours for labels
col_dict = {}
seven_colours = ['#e6194B', '#3cb44b', '#ffe119', '#ffd8b1', '#f58231', '#f032e6', '#42d4f4']
for label, colour in zip(med7.pipe_labels['ner'], seven_colours):
    col_dict[label] = colour

options = {'ents': med7.pipe_labels['ner'], 'colors':col_dict}

doc = med7(text)

# spacy.displacy.serve(doc, style='ent', options=options)

drug_dict.addNewDisease(diseaseQuery , doc)
print(drug_dict.getDictNormalized())
# print([(ent.text, ent.label_) for ent in doc.ents ])


