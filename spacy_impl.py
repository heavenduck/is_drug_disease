import scispacy
import spacy
import pandas as pd
from spacy import displacy


class SpacyRecognizer:
    nlp = spacy.load("en_ner_bc5cdr_md")

    def qualify_text(self, text):
        doc = self.nlp(text)

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

# currently, this class is not required since its functionality was transferred to the DrugFinder class
# might still be useful for visualisation
