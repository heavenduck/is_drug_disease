from pubmed_impl import PubmedImpl
import spacy
from entity_finder import EntityFinder
from dict_creator import DictCreator

entity_finder = EntityFinder()

def getDrugs(disease_list , max_paper):
  """ Routine zur Abfrage von Pubmed Paper über die Krankheiten
  :param max_paper: Anzahl der anzufragenden Paper
  :param disease_list:Array mit allen Krankheiten
  """
  
  returnDict = {} # {<disease> : <doc result>}

  pubmed = PubmedImpl()

  for disease in disease_list:
  
    maxPapers = max_paper  # limit the number of papers retrieved
    myQuery = disease + "[tiab]"  # query in title and abstract
    records = pubmed.getPapers(myQuery, maxPapers, 'xxx.xxx@mailbox.tu-dresden.de')

    # Concatenate Abstracts to one long string
    text: str = ''
    for r in records:
      if 'AB' in r:
        text += (r['AB'])
    
    doc = entity_finder.med7spacy(text, disease)

    returnDict[disease] = doc
 
    # createSpacyPrintout(doc)
  return returnDict


def getDiseases(drug_list, max_paper):
  """ Routine zur Abfrage von Pubmed Paper über die Medikamente
  :param max_paper: Anzahl der anzufragenden Paper
  :param drug_list:Array mit allen Medikamenten
  """

  returnDict = {}  # {<disease> : <doc result>}

  pubmed = PubmedImpl()

  for drug in drug_list:

    maxPapers = max_paper  # limit the number of papers retrieved
    myQuery = drug + "[tiab]"  # query in title and abstract
    records = pubmed.getPapers(myQuery, maxPapers, 'xxx.xxx@mailbox.tu-dresden.de')

    # Concatenate Abstracts to one long string
    text: str = ''
    for r in records:
      if 'AB' in r:
        text += (r['AB'])

    doc = entity_finder.spacy(text)
    
    returnDict[drug] = doc
  
  return returnDict


