class DictCreator():

  def __init__ (self):
    self.dictStorage = {}
    self.diseases = []

  def getDict(self):
    return self.dictStorage
  
  def getAllDiseases(self):
    return self.diseases 
  
  def addNewDisease(self, disease, doc_data):
    
    self.diseases.append(disease)
    self.dictStorage[disease] = {}

    for entity in doc_data.ents:
      if entity.label_ == 'DRUG':
        if entity.text in self.dictStorage[disease]:
          self.dictStorage[disease][entity.text] += 1
        else:
          self.dictStorage[disease].update({ entity.text : 1}) 

  def getNewDiseasesFromDrug(self, doc_data):
    result = {}
    for entity in doc_data.ents:

      if entity.label_ == 'DISEASE' and entity.text not in self.dictStorage.keys():
        if entity.text in result:
          result[entity.text] += 1
        else:
          result.update({ entity.text : 1}) 
        
    return result


  def getTopEntriesOfDict(self , key , amount):
    
    if "December" in self.dictStorage[key]:
      del self.dictStorage[key]["December"]

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
