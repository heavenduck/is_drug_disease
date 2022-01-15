class DictCreator():

  def __init__ (self):
    self.dictStorage = {}
    self.diseases = []

  def getDict(self):
    return self.dictStorage
  
  def getDictNormalized(self , threshhold=1):

    dictStorageNorm = self.dictStorage

    for key in dictStorageNorm:
      max_apperance = max(dictStorageNorm[key].values())
      dictStorageNorm[key] = {key:(val/max_apperance) for key, val in dictStorageNorm[key].items() if val > threshhold}   
    
    return dictStorageNorm  

  def addNewDisease(self , disease , doc_data):
    
    self.diseases.append(disease)
    self.dictStorage[disease] = {}

    for entity in doc_data.ents:
      if entity.label_ == 'DRUG':
        if entity.text in self.dictStorage[disease]:
          self.dictStorage[disease][entity.text] += 1
        else:
          self.dictStorage[disease].update({ entity.text : 1}) 

  def getAllDiseases(self):
    return self.diseases 

  def getTopEntriesOfDict(self , key , amount):
    
    # Umwandlung von Dict zu sortierter Liste
    dict_sorted_asc = sorted(self.dictStorage[key].items(), key=lambda x: x[1] , reverse=True)    
    
    # Array der ersten Elemente 
    cut_dict = dict_sorted_asc[:amount] 
    # letzes Element des abgeschnitten Array nehemen 
    last_ele = cut_dict[-1]
    
    # 
    if len(dict_sorted_asc) > amount:
      found_index = 0
      for ele in dict_sorted_asc[amount:]:
        if ele[1] == last_ele[1]:
          found_index += 1
        else:
          break
      
      newList = dict_sorted_asc[amount : amount + found_index]
      cut_dict += newList
    
    print(dict_sorted_asc)

    return cut_dict
