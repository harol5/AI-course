# (POS) -> part of sentences such as verbs, adjective, nouns, etc...
import spacy
import pandas as pd
import re

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
en_stopwords = stopwords.words('english')

sentence = "N-grams are used for a variety of different task. For example, when developing a language model, n-grams are used to develop not just unigram models but also bigram and trigram models. Google and Microsoft have developed web scale n-gram models that can be used in a variety of tasks such as spelling correction, word breaking and text summarization"
# lower case the sentence, remove stop words and replace punctuation with empty strings
cleaned_sentence = re.sub(r'[^\w\s]','',
                        ' '.join([word for word in sentence.lower().split() if word not in en_stopwords]))

nlp = spacy.load("en_core_web_sm") # load model
spacy_doc = nlp(cleaned_sentence) # create spacy DOC
pos_df = pd.DataFrame(columns = ['token','pos_tag'])

for token in spacy_doc:
    pos_df = pd.concat([
        pos_df,
        pd.DataFrame.from_records([{'token':token.text,'pos_tag':token.pos_}])
    ], ignore_index=True)

print('------------- DISPLAY FIRST 15 TOKENS AND POS TAGS --------------------')
print(pos_df.head(15))

print('------------- MOST COMMON WORDS AND POS TAGS --------------------')
pos_df_counts = pos_df.groupby(['token','pos_tag']).size().reset_index(name='counts').sort_values(by='counts',ascending=False)
print(pos_df_counts.head(10))

print('------------- MOST COMMON POS TAGS --------------------')
pos_df_poscounts = pos_df_counts.groupby(['pos_tag'])['token'].count().sort_values(ascending=False)
print(pos_df_poscounts.head(10))

print('-------------- MOST COMMON NOUNS -------------------')
nouns = pos_df_counts[pos_df_counts.pos_tag=='NOUN'][:10]
print(nouns)