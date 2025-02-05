#this uses the transformer architecture to determine the sentiment of text
sentence_1 = "i had a great time at the movie it was really funny"
sentence_2 = "i had a great time at the movie but the parking was terrible"
sentence_3 = "i had a great time at the movie but the parking wasn't great"
sentence_4 = "i went to see a movie"

from transformers import pipeline
classifier = pipeline("sentiment-analysis")

print(sentence_1)
print(classifier(sentence_1))
