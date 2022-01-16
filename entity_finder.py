from datetime import datetime
import spacy
from scispacy.abbreviation import AbbreviationDetector


# this class is a modified version of the spacy_impl
# it finds the co-occurrences of drugs and a specific disease (drug_dict)
# it does not differentiate between positive and negative sentences (yet)
class EntityFinder:
    nlp = spacy.load("en_ner_bc5cdr_md")
    med7 = spacy.load("en_core_med7_lg")
    # Abbreviation Detector


    def spacy(self, text: str):
        nlp.add_pipe("abbreviation_detector")
        doc = self.nlp(text)
        
        # replace acronyms with long form
        altered_tok = [tok.text for tok in doc]
        
        for abrv in doc._.abbreviations:
            altered_tok[abrv.start] = str(abrv._.long_form)
        
        text = (" ".join(altered_tok))

        doc = self.nlp(text)

        return doc

    def med7spacy(self, text: str):
        med7.add_pipe("abbreviation_detector")
        doc = self.med7(text)

        # replace acronyms with long form
        altered_tok = [tok.text for tok in doc]

        for abrv in doc._.abbreviations:
            altered_tok[abrv.start] = str(abrv._.long_form)

        text = (" ".join(altered_tok))

        doc = self.medy(text)

        return doc