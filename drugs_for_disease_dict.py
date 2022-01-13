# this class consists of the name of a specific disease and
# a dictionary containing the names (as strings) of the drugs that appeared in same sentences as this disease,
# as well as the count of how often they appeared together
# also contains the odds ratios of the drugs and the disease
from math import log2


class DrugsForDiseaseDict:
    # disease_name: str = ""
    # drug_dict = dict()   # co-occurrence dictionary

    filtered_words = ["covid-19", "alcohol", "smoking"]  # terms that are explicitly excluded because they are not drugs

    # odds ratio
    #############################################
    # number_of_sentences = 0   # number of all examined sentences
    # disease_occurrences = 0   # is currently assigned by drug_finder.py but could also be incremented by add_to_dict
    # drug_occurrences_dict = dict()   # stores the overall occurrence number of drugs
    # odds_ratio_dict = dict()
    #############################################

    def __init__(self, disease_name: str):
        self.disease_name = disease_name
        self.drug_dict = dict()
        self.number_of_sentences = 0
        self.disease_occurrences = 0
        self.drug_occurrences_dict = dict()
        self.odds_ratio_dict = dict()

    # converts tokens to string and increases their count in the dictionary (the dictionary will be unsorted)
    # filters certain CHEMICALs that are not drugs
    def add_to_dict(self, drug_list):
        for ent in drug_list:
            ent_string = str(ent).lower()
            if ent_string not in self.filtered_words:
                self.drug_dict[ent_string] = self.drug_dict.get(ent_string, 0) + 1

    # sorts the dictionary (the highest count first)
    def sort_dict(self):
        self.drug_dict = dict(sorted(self.drug_dict.items(), key=lambda x: x[1], reverse=True))

    # for odds ratio calculations
    def add_to_drug_occurrences_dict(self, drug_list):
        for ent in drug_list:
            ent_string = str(ent).lower()
            if ent_string not in self.filtered_words:
                self.drug_occurrences_dict[ent_string] = self.drug_occurrences_dict.get(ent_string, 0) + 1

    # calculates odds ratio for a specific drug
    def calc_odds_ratio(self, drug: str):
        if drug not in self.drug_dict:
            return 0
        # unnecessary overhead but easier to comprehend
        n = self.number_of_sentences
        n_ab = self.drug_dict[drug]
        n_a = self.disease_occurrences
        n_b = self.drug_occurrences_dict[drug]

        if n_ab <= 0:
            return 0
        return log2((n * n_ab) / (n_a * n_b))

    # creates an ordered dictionary of drugs and their corresponding odds ratios
    # based on the entries in drug_dict
    def create_odds_ratio_dict(self):
        for entry in self.drug_dict:
            self.odds_ratio_dict[entry] = self.calc_odds_ratio(entry)

        # sorts the entries in odds_ratio_dict in descending order (they will have another order than drug_dict)
        self.odds_ratio_dict = dict(sorted(self.odds_ratio_dict.items(), key=lambda x: x[1], reverse=True))
        # print(len(self.drug_dict))
