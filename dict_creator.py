class DictCreator:

  def __init__ (self):
    self.dictStorage = {}
    self.diseases = []

  def getDict(self):
    return self.dictStorage
  
  def getAllDiseases(self):
    return self.diseases 
    
  def addNewDisease(self, disease, doc_data):
    """ Hinzufügen einer neuen Krankheit mit deren Medikamenten
    :param disease: hinzuzufügende Krankheit 
    :param doc_data: Ergebnis eines Entitäten Erkenners von Spacy (noch nicht nach Drugs gefiltert)
    """

    self.diseases.append(disease)
    self.dictStorage[disease] = {}

    # Iteration über die Entitäten von doc_data -> Filterung nach DRUG + Auftreten des Medikamentes
    for entity in doc_data.ents:
      if entity.label_ == 'DRUG':
        if entity.text.lower() in self.dictStorage[disease]:
          self.dictStorage[disease][entity.text.lower()] += 1
        else:
          self.dictStorage[disease].update({ entity.text.lower() : 1})

    # Rausfiltern von falschen Einträgen
    self.filter_drugs(disease)

  def getNewDiseasesFromDrug(self, doc_data):
    """ Ermittlung neuer Krankheiten aus den Entitäten eines Medikamentes 
    :param doc_data: Ergebnis eines Entitäten Erkenners von Spacy (noch nicht nach DISEASE gefiltert)
    :return : Dict {<Krankheit> : <Häufigkeit des Auftretens>}
    """

    result = {}
    for entity in doc_data.ents:

      if entity.label_ == 'DISEASE' and entity.text not in self.dictStorage.keys():
        if entity.text.lower() in result:
          result[entity.text.lower()] += 1
        else:
          result.update({ entity.text.lower() : 1})
        
    return result


  def getTopEntriesOfDict(self , key , amount):
    """ Ermittlung der ersten N Elemente 
    :param key: die ausgewählte Krankheit
    :param amount: Anzahl der zu bestimmenden Elemente
    """

    # Umwandlung von Dict zu sortierter Liste
    dict_sorted_asc = sorted(self.dictStorage[key].items(), key=lambda x: x[1] , reverse=True)    
    
    # Array der ersten Elemente 
    cut_dict = dict_sorted_asc[:amount] 
    # letztes Element des abgeschnittenen Arrays nehmen
    last_ele = cut_dict[-1]
    
    # alle Elemente über amount hinaus anhängen, solange sie die gleiche Kookkurrenz haben wie last_ele
    if len(dict_sorted_asc) > amount:
      found_index = 0
      for ele in dict_sorted_asc[amount:]:
        if ele[1] == last_ele[1]:
          found_index += 1
        else:
          break
      
      newList = dict_sorted_asc[amount : amount + found_index]
      cut_dict += newList
    
    returnArray = []
    for ele in cut_dict:
      returnArray.append(ele[0]) 

    return returnArray

  # Entfernen die Begriffe, die in der jeweiligen Liste eingetragen sind
  def filter_drugs(self, disease):
    for drug in list(self.dictStorage[disease]):
      if drug in self.drug_filter_list:
        self.dictStorage[disease].pop(drug)

  def filter_diseases(self, disease_list):
    for disease in disease_list:
      if disease[0] in self.disease_filter_list:
        disease_list.remove(disease)

  drug_filter_list = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september',
                      'october', 'november', 'december',
                      'kyoto', 'coronaviridae', 'latinx']

  disease_filter_list = ['death', 'puberty', 'clay', 'sexual behavior', 'increase in mood', 'us-born',
                         'sexual dimorphism', 'sexual maturity', 'bias', 'muscle mass', 'minerals']

