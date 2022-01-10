from datetime import datetime
import spacy
from drugs_for_disease_dict import DrugsForDiseaseDict
from scispacy.abbreviation import AbbreviationDetector


# this class is a modified version of the spacy_impl
# it finds the co-occurrences of drugs and a specific disease (drug_dict)
# it does not differentiate between positive and negative sentences (yet)
class DrugFinder:
    nlp = spacy.load("en_ner_bc5cdr_md")
    # Abbreviation Detector
    nlp.add_pipe("abbreviation_detector")

    def qualify_text(self, text: str, drug_dict: DrugsForDiseaseDict):
        print("get ents " + str(datetime.now()))   # time measurement: start of entity recognition
        doc = self.nlp(text)

        print("get abrv " + str(datetime.now()))   # time measurement: start of abbreviation replacement
        # replace acronyms with long form
        altered_tok = [tok.text for tok in doc]
        for abrv in doc._.abbreviations:
            altered_tok[abrv.start] = str(abrv._.long_form)
        text = (" ".join(altered_tok))

        doc = self.nlp(text)
        # now perform named entity recognition

        drugs_in_sentence = []
        sentence_contains_disease = False

        # for odds ratio calculations
        sentence_counter = 0
        disease_sentence_counter = 0

        print("get cooc " + str(datetime.now()))   # time measurement: start of co-occurrence detection and odds ratio
        # Split text into sentences
        for sent in doc.sents:
            sentence_counter += 1
            # Get labels from sentences
            for ent in sent.ents:
                # Filter out 'entity' label
                if ent.label_ != 'ENTITY':
                    # Aggregate all Chemicals of the sentence
                    if ent.label_ == 'CHEMICAL':
                        drugs_in_sentence.append(ent)
                    # Check if the sentence contains the queried disease
                    if not sentence_contains_disease and drug_dict.disease_name in [str(token).lower() for token in ent]:
                        sentence_contains_disease = True
                        disease_sentence_counter += 1

            if sentence_contains_disease:
                drug_dict.add_to_dict(drugs_in_sentence)

            # for odds ratio calculations
            drug_dict.add_to_drug_occurrences_dict(drugs_in_sentence)

            # Reset for next sentence
            drugs_in_sentence = []
            sentence_contains_disease = False

        # for odds ratio calculations
        drug_dict.number_of_sentences = sentence_counter
        drug_dict.disease_occurrences = disease_sentence_counter

        # Sort the dictionary in descending order
        drug_dict.sort_dict()
        drug_dict.create_odds_ratio_dict()

        print("end      " + str(datetime.now()))   # time measurement: end

    # does not return anything since the drug_dict is already a parameter
