# get the entity label of a sentence

import spacy
from spacy import displacy
from spacy import tokenizer
import re

nlp = spacy.load("en_core_web_sm")
sentence = "Google was founded on September 4, 1998, by computer scientists Larry Page and Sergey Brin while they were PhD students at Stanford University in California. Together they own about 14% of its publicly listed shares and control 56% of its stockholder voting power through super-voting stock. The company went public via an initial public offering (IPO) in 2004. In 2015, Google was reorganized as a wholly owned subsidiary of Alphabet Inc. Google is Alphabet's largest subsidiary and is a holding company for Alphabet's internet properties and interests. Sundar Pichai was appointed CEO of Google on October 24, 2015, replacing Larry Page, who became the CEO of Alphabet. On December 3, 2019, Pichai also became the CEO of Alphabet."
spacy_doc = nlp(sentence)

print('------------- DISPLAY ENTITIES (NOT CLEANED) --------------------')
for entity in spacy_doc.ents:
    print(entity.text, entity.label_)

displacy.render(spacy_doc, style='ent')

clean_sentence = re.sub(r'[^\w\s]','',sentence).lower() # remove punctuation and lower case the sentence
spacy_doc_clean = nlp(clean_sentence)

print('------------- DISPLAY ENTITIES (CLEANED, NO PUNCTUATION) --------------------')
for entity in spacy_doc_clean.ents:
    print(entity.text, entity.label_)