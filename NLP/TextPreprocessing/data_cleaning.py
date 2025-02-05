import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

#always use lower case
sentence_list = [
    'I like Dogs',
    'My Favorite Dish is Pizza',
    'My favorite Programming Language Is C++'
]

lower_sentence_list = [sentence.lower() for sentence in sentence_list] # list comprehension syntax
print(lower_sentence_list)

#remove stop words - words that are common but do not add meaning
en_stopwords = stopwords.words('english')
sentence = "I want to become a master in AI engineering by the end of the year"
no_stopwords_sentence = ' '.join([word for word in sentence.split() if word not in en_stopwords])
print(no_stopwords_sentence)



