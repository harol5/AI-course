# counts which words appear in which document, but we lose context
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

data = ['Most shark attacks occur about 10 feet from the beach since that is where the people are',
        'the efficiency with which he paired the socks in the drawer was quite admirable',
        'carol drank the blood as if she were a vampire',
        'giving directions that the mountains are to the west only works when you can see them',
        'the sign said there was road work ahead so he decided to speed up',
        'the gruff old man sat in the back of the bait shop grumbling to himself as he scooped out a handful of worms']

vectorizer = CountVectorizer()
vectorizer_fit = vectorizer.fit_transform(data)
bag_of_words = pd.DataFrame(vectorizer_fit.toarray(), columns=vectorizer.get_feature_names_out())
print(bag_of_words)

data2 = {
    'sales': [100000,222000,1000000,522000,111111,222222,1111111,20000,75000,90000,1000000,10000],
    'city': ['Tampa','Tampa','Orlando','Jacksonville','Miami','Jacksonville','Miami','Miami','Orlando','Orlando','Orlando','Orlando'],
    'size': ['Small', 'Medium','Large','Large','Small','Medium','Large','Small','Medium','Medium','Medium','Small',]
}
vectorizer_fit_2 = vectorizer.fit_transform(data2['city'])
bag_of_words_2 = pd.DataFrame(vectorizer_fit_2.toarray(), columns=vectorizer.get_feature_names_out())
print(bag_of_words_2)
