# converting text to small units
import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize, sent_tokenize

sentences = "Her cat's name is Luna. Her dog's name is Bolt."
print(sent_tokenize(sentences)) # get sentences.

sentence = "her cat's name is Luna"
print(word_tokenize(sentence)) # get words

