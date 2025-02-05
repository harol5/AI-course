# does not used machine learning, only rule.

sentence_1 = "i had a great time at the movie it was really funny"
sentence_2 = "i had a great time at the movie but the parking was terrible"
sentence_3 = "i had a great time at the movie but the parking wasn't great"
sentence_4 = "i went to see a movie"

from textblob import TextBlob
print("------------- textblob ---------------------")
sentiment_score_1 = TextBlob(sentence_1)
score = sentiment_score_1.sentiment.polarity
print(sentence_1)
print(score)

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
print("------------- SentimentIntensityAnalyzer ---------------------")
analyzer = SentimentIntensityAnalyzer()
sentiment_score_2 = analyzer.polarity_scores(sentence_1)
print(sentence_2)
print(sentiment_score_2)