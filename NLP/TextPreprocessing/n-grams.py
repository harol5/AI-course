import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
from nltk.corpus import stopwords

import pandas as pd
import matplotlib.pyplot as plt

data = "the quick brown fox jumps over the lazy dog, the dog is a lazy dog, and the brown fox is a incredibly fast animal"
en_stopwords = stopwords.words('english')
no_stopwords_sentence = ' '.join([word for word in data.split() if word not in en_stopwords])


tokens = word_tokenize(no_stopwords_sentence)
ngrams = nltk.ngrams(tokens,2)
ngrams_value_counts = pd.Series(ngrams).value_counts()
print(ngrams_value_counts)

# ngrams_value_counts[:10].sort_values().plot.barh(color='blue', width=9 ,figsize=(12, 8))
# plt.title("ngrams_value_counts")

for ngram in nltk.ngrams("this is a test".split(), 3):
    print(ngram)




