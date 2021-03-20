__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com'



food_list = ['spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'eggs', 'spam']
from collections import defaultdict

food_count = defaultdict(int)
for i in food_list:
    food_count[i] +=1
print(food_count)