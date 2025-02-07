import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

if __name__ == '__main__':
    data = pd.DataFrame([
            ("i love spending time with my friends and family", "positive"),
            ("that was the best meal i've ever had in my life", "positive"),
            ("i feel so grateful for everything i have in my life", "positive"),
            ("i received a promotion at work and i couldn't be happier", "positive"),
            ("watching a beautiful sunset always fills me with joy", "positive"),
            ("my partner surprised me with a thoughtful gift and it made my day", "positive"),
            ("i am so proud of my daughter for graduating with honors", "positive"),
            ("listening to my favorite music always puts me in a good mood", "positive"),
            ("i love the feeling of accomplishment after completing a challenging task", "positive"),
            ("i am excited to go on vacation next week", "positive"),
            ("i feel so overwhelmed with work and responsibilities", "negative"),
            ("the traffic during my commute is always so frustrating", "negative"),
            ("i received a parking ticket and it ruined my day", "negative"),
            ("i got into an argument with my partner and we're not speaking", "negative"),
            ("i have a headache and i feel terrible", "negative"),
            ("i received a rejection letter for the job i really wanted", "negative"),
            ("my car broke down and it's going to be expensive to fix", "negative"),
            ("i'm feeling sad because i miss my friends who live far away", "negative"),
            ("i'm frustrated because i can't seem to make progress on my project", "negative"),
            ("i'm disappointed because my team lost the game", "negative")
        ],
        columns=['text', 'sentiment'])

    data = data.sample(frac=1).reset_index(drop=True)
    x=data['text']
    y=data['sentiment']

    countvec = CountVectorizer()
    countvec_fit = countvec.fit_transform(x)
    bag_of_words = pd.DataFrame(countvec_fit.toarray(), columns=countvec.get_feature_names_out())
    print(bag_of_words)

    x_train, x_text, y_train, y_test = train_test_split(bag_of_words, y, test_size=0.3, random_state=7)
    lr = LogisticRegression(random_state=1).fit(x_train, y_train)
    y_pred_lr = lr.predict(x_text)
    print(accuracy_score(y_pred_lr, y_test))
    print(classification_report(y_test, y_pred_lr, zero_division=0))

    print("----------------------  Naive Bayes -----------------------")
    from sklearn.naive_bayes import MultinomialNB
    nb = MultinomialNB().fit(x_train, y_train)
    y_pred_nb = nb.predict(x_text)
    print(accuracy_score(y_pred_nb, y_test))
    print(classification_report(y_test, y_pred_nb, zero_division=0))