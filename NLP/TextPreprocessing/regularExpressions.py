import re

# the "r" stands for raw string. it makes sure to scape special character like '/'
my_folder = r"c:\desktop\notes\universe\outerspace"
result_search = re.search("space", my_folder); # searching for patterns
print(result_search)

result_search_two = re.search("dogs",my_folder);
print(result_search_two)

morning_message = r"good morning carl"
morning_message_updated = re.sub("carl", "john", morning_message) #replace
print(morning_message_updated)

customer_reviews = [
    "sam was great",
    "greg was rude",
    "james was awesome",
    "carl was terrible",
    "I had a great experience with Greg",
    "thanks to sam I was able to complete my tasks",
    "good customer service from james"
]

greg_reviews = []
patter_to_find = r"greg?" # the "?" makes the last "g" optional
for review in customer_reviews:
    if re.search(patter_to_find, review):
        greg_reviews.append(review)


print(greg_reviews)

reviews_with_good = []
pattern_to_find = r"^good" # the "^" matches the "good" word
for review in customer_reviews:
    if re.search(pattern_to_find, review):
        reviews_with_good.append(review)


print(reviews_with_good)
