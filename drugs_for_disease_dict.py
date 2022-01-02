# this class consists of the name of a specific disease and
# a dictionary containing the names (as strings) of the drugs that appeared in same sentences as this disease,
# as well as the count of how often they appeared together
class DrugsForDiseaseDict:
    disease_name: str = ""
    drug_dict = dict()

    def __init__(self, disease_name: str):
        self.disease_name = disease_name

    # converts tokens to string and increases their count in the dictionary (the dictionary will be unsorted)
    def add_to_dict(self, drug_list):
        for ent in drug_list:
            self.drug_dict[str(ent).lower()] = self.drug_dict.get(str(ent).lower(), 0) + 1

    # sorts the dictionary (the highest count first)
    def sort_dict(self):
        self.drug_dict = dict(sorted(self.drug_dict.items(), key=lambda x: x[1], reverse=True))
