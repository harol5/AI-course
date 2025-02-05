# keeps the context when transforming text to numbers
# Term Frequency-Inverse Document Frequency (TF-IDF)
# it calculates the importance of the word for each string or document in our dataset by
# how often it occurs generally.

# Term Frequency: number of times a word appears in a document.
# Inverse Document Frequency: measure of the importance of each term in each document

# common terms = less important meaning less score

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

data = ['Most shark attacks occur about 10 feet from the beach since that is where the people are',
        'the efficiency with which he paired the socks in the drawer was quite admirable',
        'carol drank the blood as if she were a vampire',
        'giving directions that the mountains are to the west only works when you can see them',
        'the sign said there was road work ahead so he decided to speed up',
        'the gruff old man sat in the back of the bait shop grumbling to himself as he scooped out a handful of worms']

tfidf = TfidfVectorizer()
tfidf_fit = tfidf.fit_transform(data)
tfidf_df = pd.DataFrame(tfidf_fit.toarray(), columns=tfidf.get_feature_names_out())
print(tfidf_df)