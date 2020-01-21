# import Algorithmia
# from django.shortcuts import render,redirect
# from apps.customers.models import Customer
# import re

# user = Customer.objects.get(pk=1)
# All = Customer.objects.exclude(pk=user.pk) 
# user_profile = [
#     {
#         'name' : str(user.id),
#         'age'  : user.age(),
#         'interests' : re.split("; | , | . | \\ | // | \n  | \s",user.hobby),
#         'fav_book' : re.split("; | , | . | \\ | // | \n  | \s",user.favorite_book)
#     }
# ]
# matching_list = []
# for match in All:
#     profile = {
#         'name' : str(match.id),
#         'age'  : match.age(),
#         'interests' : re.split("; | , | . | \\ | // | \n  | \s",match.hobby),
#         'fav_book' : re.split("; | , | . | \\ | // | \n  | \s",match.favorite_book),
#     }
#     matching_list.append(profile)
# result = {
#     'scoring_weights' : {
#         'age':0.3,
#         'gender':0.6,
#         'interests':0.4,
#         'fav_book':0.4,
#     },
#     'group1' : user_profile,
#     'group2' : matching_list,
# }

# client = Algorithmia.client('simWgOx7ABiLTOAxABjYTbiRrma1')
# algo = client.algo('matching/DatingAlgorithm/0.1.3')
# algo.set_options(timeout=300) # optional
# matched = algo.pipe(result).result
# print(matched)
