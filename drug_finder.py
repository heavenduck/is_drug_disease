import spacy
from drugs_for_disease_dict import DrugsForDiseaseDict


# this class is a modified version of the spacy_impl
# it finds the co-occurrences of drugs and a specific disease (drug_dict)
# it does not differentiate between positive and negative sentences (yet)
class DrugFinder:
    nlp = spacy.load("en_ner_bc5cdr_md")

    def qualify_text(self, text: str, drug_dict: DrugsForDiseaseDict):
        doc = self.nlp(text)

        drugs_in_sentence = []
        sentence_contains_disease = False

        # Split text into sentences
        for sent in doc.sents:
            # Get labels from sentences
            for ent in sent.ents:
                # Filter out 'entity' label
                if ent.label_ != 'ENTITY':
                    # Aggregate all Chemicals of the sentence
                    if ent.label_ == 'CHEMICAL':
                        drugs_in_sentence.append(ent)
                    # Check if the sentence contains the queried disease
                    if drug_dict.disease_name in [str(token).lower() for token in ent]:
                        sentence_contains_disease = True

            if sentence_contains_disease:
                drug_dict.add_to_dict(drugs_in_sentence)

            # Reset for next sentence
            drugs_in_sentence = []
            sentence_contains_disease = False

        # Sort the dictionary in descending order
        drug_dict.sort_dict()
        print(drug_dict.drug_dict)

    # does not return anything since the drug_dict is already a parameter
