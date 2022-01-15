from pubmed_impl import PubmedImpl
from drug_finder import DrugFinder
from networkx_graph import *  # Implementation der Darstellung
from dict_creator import DictCreator

med7 = spacy.load("en_core_med7_lg")
drug_finder = DrugFinder()

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


def getDrugs(disease_list , max_paper=100):
  """
  :param max_paper:
  :param disease_list:Array -
  """
  
  returnDict = {} # {<disease> : <doc result>}

  pubmed = PubmedImpl()

  for disease in disease_list:
  
    maxPapers = max_paper  # limit the number of papers retrieved
    myQuery = disease + "[tiab]"  # query in title and abstract
    records = pubmed.getPapers(myQuery, maxPapers, 'xxx.xxx@mailbox.tu-dresden.de')
    
    # TODO Bearbeitung der Paper einzeln ansonsten RAM Overflow bei mehr als 500 Papern

    # Concatenate Abstracts to one long string
    text: str = ''
    for r in records:
      if 'AB' in r:
        text += (r['AB'])
    
    doc = med7(text)

    returnDict = {disease : doc}
 
    # createSpacyPrintout(doc)
  return returnDict


def getDiseases(drug_list, max_paper):
  """
  :param drugs:Array -
  """

  returnDict = {}  # {<disease> : <doc result>}

  pubmed = PubmedImpl()

  for drug in drug_list:

    maxPapers = max_paper  # limit the number of papers retrieved
    myQuery = drug + "[tiab]"  # query in title and abstract
    records = pubmed.getPapers(myQuery, maxPapers, 'xxx.xxx@mailbox.tu-dresden.de')

    # TODO Bearbeitung der Paper einzeln ansonsten RAM Overflow bei mehr als 500 Papern

    # Concatenate Abstracts to one long string
    text: str = ''
    for r in records:
      if 'AB' in r:
        text += (r['AB'])

    doc = drug_finder.spacy(text)

    returnDict = {drug: doc}

  return returnDict

# datadict = drug_dict.getDictNormalized(1)
# g = graph(datadict)
# forceAtlas2Impl(g)

if __name__ == "__main__":
  
  start_disease = "SARS-Cov-2"
  max_paper = 100

  #Pubmed Anfrage: eine Krankheit (300-500 Paper)
  resultFistStep = getDrugs([start_disease] , max_paper)
  
  #Filterung aller Medikamente in den Artikeln
  dictFirstResult = DictCreator()
  dictFirstResult.addNewDisease(start_disease , resultFistStep[start_disease])
  top_disease = dictFirstResult.getTopEntriesOfDict(start_disease , 10) 

  #Pubmed Anfrage: Top 20 der Medikamente aus erster Anfrage (300-500 Paper)
  #Herausfinden aller Krankheiten in den Papern
  #Pubmed Anfrage: Top 20-50 Krankheiten
  #Erstellung Dict aus der Letzen Anfrage und deren Auswertung
  #Knoten mit nur 1 Kante entfernen oder Threshhold einbauen?
  #Zeichnen der Knoten 

