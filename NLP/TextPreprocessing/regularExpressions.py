import re

my_folder = r"c:\desktop\notes\universe\outerspace" # the "r" makes sure to scape special character like '/'
result_search = re.search("space", my_folder); # searching for patterns
print(result_search)

result_search_two = re.search("dogs",my_folder);
print(result_search_two)