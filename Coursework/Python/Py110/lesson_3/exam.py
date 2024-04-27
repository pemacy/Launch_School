# def swap_ends(lst):
#     first = lst[0]
#     last = lst[-1]

#     lst[0] = last
#     lst[-1] = first
#     return lst
# famous_authors = ["Kurt Vonnegut", "Virginia Woolf", "Jane Austen"]

# author = famous_authors.pop(1)

# print(famous_authors)
# print(author)

def high_scores_in_round(rounds):
    return [ scores for scores in rounds if all([score > 4 for score in scores ]) ]
    # return [ scores for scores in rounds if all( round_analysis for round_analysis in [ score > 4 for score in scores ]) ]

rounds = [[6, 8], [2, 9], [15, 11], [4, 100]]
print(high_scores_in_round(rounds)) # [[6, 8], [15, 11]]



# lst1 = [5, 4, 7, 9, 1, 3]
# lst2 = [15, 16, 1, 245, 8, 11]
# lst3 = [1, 2, 4, 9, 100]

# def custom_sort(lst):
#     odd_ints = [ el for el in lst if el % 2 != 0 ]
#     even_ints = [ el for el in lst if el % 2 == 0 ]
#     return sorted(even_ints, reverse=True) + sorted(odd_ints, reverse=True)

# print(custom_sort(lst1) == [4, 9, 7, 5, 3, 1])  # True
# print(lst1 == [5, 4, 7, 9, 1, 3])  # True

# print(custom_sort(lst2) == [16, 8, 245, 15, 11, 1])  # True
# print(lst2 == [15, 16, 1, 245, 8, 11])  # True

# print(custom_sort(lst3) == [100, 4, 2, 9, 1])  # True
# print(lst3 == [1, 2, 4, 9, 100])  # True


# my_pets = {
#     "dogs": [
#         {"name": "phanouris", "breed": "english setter"},
#         {"name": "luna", "breed": "mongrel"},
#     ],
#     "birds": [
#         {"name": "lot", "breed": "yellow-faced parrot"}
#     ],
#     "fish": [
#         {"name": "goldin", "breed": "goldfish"}
#     ],
#     "cats": [
#         {"name": "louie", "breed": "british shorthair"},
#         {"name": "zuzu", "breed": "moggie"}
#     ]
# }

# my_pets = {
#     "dogs": [
#         {"name": "phanouris", "breed": "english setter"},
#         {"name": "luna", "breed": "mongrel"},
#     ],
#     "birds": [
#         {"name": "lot", "breed": "yellow-faced parrot"}
#     ],
#     "fish": [
#         {"name": "goldin", "breed": "goldfish"}
#     ],
#     "cats": [
#         {"name": "louie", "breed": "british shorthair"},
#         {"name": "zuzu", "breed": "moggie"}
#     ]
# }


# pets_list = [ { 'type': pet_type, 'pets': pet_list } for pet_type, pet_list in my_pets.items() ]

# expected_pets_list = [
#     {
#         "type": "dogs",
#         "pets": [
#             {"name": "phanouris", "breed": "english setter"},
#             {"name": "luna", "breed": "mongrel"},
#         ],
#     },
#     {"type": "birds", "pets": [{"name": "lot", "breed": "yellow-faced parrot"}]},
#     {"type": "fish", "pets": [{"name": "goldin", "breed": "goldfish"}]},
#     {
#         "type": "cats",
#         "pets": [
#             {"name": "louie", "breed": "british shorthair"},
#             {"name": "zuzu", "breed": "moggie"},
#         ],
#     },
# ]

# print(pets_list == expected_pets_list) # True

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}

# result_set = set1.difference(set2)
# result_set = set1 - set2
# print(result_set)

# numbers = [1, 2, 3, 2, 1, 4, 5, 5]

# unique_numbers = set(numbers)

# # concatenated_string = ''.join(unique_numbers)
# concatenated_string = ''.join([ str(num) for num in unique_numbers])
# print(concatenated_string)

# original_numbers = (1, 2, 3, 4)
# squared_numbers = []

# for number in original_numbers:
#     squared_numbers.append(number * number)

# squared_numbers = tuple(squared_numbers)
# print(squared_numbers)


