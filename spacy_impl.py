import scispacy
import spacy
import pandas as pd
from spacy import displacy
from scispacy.abbreviation import AbbreviationDetector


class SpacyRecognizer:
    nlp = spacy.load("en_ner_bc5cdr_md")
    # Abbrevaiation Detector
    nlp.add_pipe("abbreviation_detector")


    def qualify_text(self, text):
        doc = self.nlp(text)

        # replace acronyms with long form
        altered_tok = [tok.text for tok in doc]
        for abrv in doc._.abbreviations:
            altered_tok[abrv.start] = str(abrv._.long_form)
        text = (" ".join(altered_tok))

        doc = self.nlp(text)
        # now perform named entity recognition
        entities = []
        labels = []
        sentence_number = []
        sentence_counter = 0

        # Split text into sentences
        for sent in doc.sents:
            # Get labels from sentences
            for ent in sent.ents:
                # Filter out 'entity' label
                if ent.label_ != 'ENTITY':
                    # Build pandas dataframe with sentence_number
                    entities.append(ent)
                    sentence_number.append(sentence_counter)
                    labels.append(ent.label_)
            sentence_counter += 1

        df = pd.DataFrame({'Entities': entities, 'Labels': labels, 'Sentence Number': sentence_number})

        # Uncomment if you want to visualize labelling
        # displacy.serve(doc, style="ent")

        return df
