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


