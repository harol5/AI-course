import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# relevant packages for this topic
import gensim
import gensim.corpora as corpora

data = pd.read_csv('./NLP/TopicModeling/news_articles.csv')
print("-------------- Original articles ------------------")
print(data.head())

# get the column 'content' as a panda Series obj
articles = data['content']
# lower case strings and remove punctuation
articles = articles.str.lower().apply(lambda x: re.sub(r'[^\w\s]','',x))
# stop word removal
en_stopwords = stopwords.words('english')
articles = articles.apply(lambda x: ' '.join([word for word in x.split() if word not in (en_stopwords)]))
#tokenize
articles = articles.apply(lambda x: word_tokenize(x))
#stemming (done for speed as we have a lot of text)
ps = PorterStemmer()
articles = articles.apply(lambda tokens: [ps.stem(token) for token in tokens])

print("-------------- Cleaned articles ------------------")
print(articles)

print("-------------- Dictionary with unique words ------------------")
# dictionary of every unique word in our dataset
dictionary = corpora.Dictionary(articles)
print(dictionary)

print("-------------- vectorizing ------------------")
# vectorizing -> bag-of-words (to feed our LDA Model)
doc_term = [dictionary.doc2bow(text) for text in articles]
# print(doc_term)

num_topics = 2
print("-------------- LDA Model ------------------")
lda_model = gensim.models.LdaModel(corpus=doc_term, id2word=dictionary, num_topics=num_topics)
print(lda_model.print_topics(num_topics=num_topics, num_words=5))

print("-------------- LSA Model ------------------")
from gensim.models import LsiModel
lsa_model = LsiModel(corpus=doc_term, id2word=dictionary, num_topics=num_topics)
print(lsa_model.print_topics(num_topics=num_topics, num_words=5))