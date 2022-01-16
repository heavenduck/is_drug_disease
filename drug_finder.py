from datetime import datetime
import spacy
from scispacy.abbreviation import AbbreviationDetector


# this class is a modified version of the spacy_impl
# it finds the co-occurrences of drugs and a specific disease (drug_dict)
# it does not differentiate between positive and negative sentences (yet)
class DrugFinder:
    nlp = spacy.load("en_ner_bc5cdr_md")
    # Abbreviation Detector
    nlp.add_pipe("abbreviation_detector")

    def spacy(self, text: str):
        
        doc = self.nlp(text)
        
        # replace acronyms with long form
        altered_tok = [tok.text for tok in doc]
        
        for abrv in doc._.abbreviations:
            altered_tok[abrv.start] = str(abrv._.long_form)
        
        text = (" ".join(altered_tok))

        doc = self.nlp(text)

        return doc
