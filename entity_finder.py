import spacy
from scispacy.abbreviation import AbbreviationDetector  # DO NOT DELETE THIS IMPORT IT IS IN USE !!!


class EntityFinder:
    nlp = spacy.load("en_ner_bc5cdr_md")
    nlp.add_pipe("abbreviation_detector")
    
    med7 = spacy.load("en_core_med7_lg")
    med7.add_pipe("abbreviation_detector")

    def spacy(self, text: str):
        doc = self.nlp(text)
        
        # replace acronyms with long form
        altered_tok = [tok.text for tok in doc]
        
        for abrv in doc._.abbreviations:
            altered_tok[abrv.start] = str(abrv._.long_form)
        
        text = (" ".join(altered_tok))

        doc = self.nlp(text)

        return doc


    def med7spacy(self, text: str, disease: str):
        """
        # Entfernt alle Sätze, in denen die Krankheit nicht vorkommt.
        # Dadurch wird die Kookkurrenz auf Satzebene ermittelt.
        doc = self.nlp(text)
        relevant_sentences = []

        for sent in doc.sents:
            tokens_in_sent = [ent.text.lower() for ent in sent.ents]
            if disease in tokens_in_sent:
                relevant_sentences += [ent.text for ent in sent]

        text = (" ".join(relevant_sentences))
        """

        doc = self.med7(text)

        # replace acronyms with long form
        altered_tok = [tok.text for tok in doc]

        for abrv in doc._.abbreviations:
            altered_tok[abrv.start] = str(abrv._.long_form)

        text = (" ".join(altered_tok))

        doc = self.med7(text)

        return doc
