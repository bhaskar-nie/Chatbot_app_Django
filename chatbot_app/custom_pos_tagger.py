# custom_pos_tagger.py

import spacy

class CustomPOSTagger:
    def __init__(self, model_name='en_core_web_sm'):
        self.nlp = spacy.load(model_name)
        
    def get_tags(self, text):
        doc = self.nlp(text)
        return [(token.text, token.pos_, token.lemma_) for token in doc]
