from pubmed_impl import PubmedImpl
import spacy
from networkx_graph import *
from dict_creator import DictCreator


pubmed = PubmedImpl()
drug_dict = DictCreator()

med7 = spacy.load("en_core_med7_lg")
med7.max_length = 2000000

disease_list_string = 'hepatitis, cancer'
disease_list = disease_list_string.split(", ")

for disease in disease_list:
  
  diseaseQuery = disease  # will only work if the string is a single word because of tokenization

  maxPapers = 600  # limit the number of papers retrieved
  myQuery = diseaseQuery + "[tiab]"  # query in title and abstract
  records = pubmed.getPapers(myQuery, maxPapers, 'xxx.xxx@mailbox.tu-dresden.de')

  # Concatenate Abstracts to one long string
  text: str = ''
  for r in records:
    if 'AB' in r:
      text += (r['AB'])


  doc = med7(text)
  drug_dict.addNewDisease(diseaseQuery , doc)
  
  #createSpacyPrintout(doc)



datadict = drug_dict.getDictNormalized(1)
g = graph(datadict)
forceAtlas2Impl(g)


def createSpacyPrintout(doc):
  """
  create a colored print out of the labes in the text via spacy
  :param doc: solution of a med7() function
  """

  # create distinct colours for labels
  col_dict = {}
  seven_colours = ['#e6194B', '#3cb44b', '#ffe119', '#ffd8b1', '#f58231', '#f032e6', '#42d4f4']
  for label, colour in zip(med7.pipe_labels['ner'], seven_colours):
    col_dict[label] = colour

  options = {'ents': med7.pipe_labels['ner'], 'colors':col_dict}
  
  spacy.displacy.serve(doc, style='ent', options=options)
