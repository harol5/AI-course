# standardize and normalization approach used in text (reducing the word to their base form)
# more accurate than stemming but more data to deal with and slower.

import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

connect_tokens = ['connecting', 'connected', 'connectivity', 'connect', 'connects']
for token in connect_tokens:
    print(token, ": ", lemmatizer.lemmatize(token))

print("----------------------------------------")

learn_tokens = ['learned', 'learning', 'learns', 'learn', 'learner', 'learners']
for token in learn_tokens:
    print(token, ": ", lemmatizer.lemmatize(token))


# ------------- EXAMPLES OF STEMMING WHERE THE OUTPUT IS RIGHT
print("------------- EXAMPLES OF STEMMING WHERE THE OUTPUT IS RIGHT")
other_tokens = ['likes', 'better', 'worse']
for token in other_tokens:
    print(token, ": ", lemmatizer.lemmatize(token))

print("----------------------------------------")

change_tokens = ['change', 'changed', 'changes', 'changing']
for token in change_tokens:
    print(token, ": ", lemmatizer.lemmatize(token))