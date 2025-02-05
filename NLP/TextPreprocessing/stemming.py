# standardize and normalization approach used in text (reducing the word to their base form)
# less accurate than lemmatization but fewer data to deal with and faster.

from nltk.stem import PorterStemmer
ps = PorterStemmer()

connect_tokens = ['connecting', 'connected', 'connectivity', 'connect', 'connects']
for token in connect_tokens:
    print(token, ": ", ps.stem(token))

print("----------------------------------------")

learn_tokens = ['learned', 'learning', 'learns', 'learn', 'learner', 'learners']
for token in learn_tokens:
    print(token, ": ", ps.stem(token))


# ------------- EXAMPLES OF STEMMING WHERE THE OUTPUT IS WRONG
print("------------- EXAMPLES OF STEMMING WHERE THE OUTPUT IS WRONG")
other_tokens = ['likes', 'better', 'worse']
for token in other_tokens:
    print(token, ": ", ps.stem(token))

print("----------------------------------------")

change_tokens = ['change', 'changed', 'changes', 'changing']
for token in change_tokens:
    print(token, ": ", ps.stem(token))


