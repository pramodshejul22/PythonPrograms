#Day-9
from collections import Counter

# s='hello ram, \n this was nice'
# print(s)

# hello ram,
#  this was nice

# s='hello ram, \t this was nice'
# print(s)

# hello ram, 	 this was nice

# s='hello\bnice'
# print(s)

# hellnice

# s='hello ram, \"this\" was nice'
# print(s)

# hello ram, "this" was nice


# str='pramod','dna','a','p','s','p','pramod'
# a=0
# for i in str:
#     if 'pramod' in i:
#         # print("value present")
#         a = a+1
#     # else:
#         # print("not present")
# print("the count prmod is",a)

#the count prmod is 2

#program - duplicate string find

# # Sample list of strings
# strings = [
#     "apple", "banana", "apple", "orange", "banana",
#     "apple", "banana", "grape", "orange", "grape"
# ]
#
# # Use Counter to count occurrences of each string
# string_counts = Counter(strings)
#
# # Display the counts
# for string, count in string_counts.items():
#     print(f"{string}: {count}")

#using Dictionary

# Sample list of strings
# strings = [
#     "apple", "banana", "apple", "orange", "banana",
#     "apple", "banana", "grape", "orange", "grape"
# ]
#
# # Initialize an empty dictionary to store the counts
# string_counts = {}
#
# # Iterate over the list of strings
# for string in strings:
#     if string in string_counts:
#         # If the string is already in the dictionary, increment its count
#         string_counts[string] += 1
#     else:
#         # If the string is not in the dictionary, add it with a count of 1
#         string_counts[string] = 1
#
# # Display the counts
# for string, count in string_counts.items():
#     print(f"{string}: {count}")

# apple: 3
# banana: 3
# orange: 2
# grape: 2

#Program Reverse string
# str='pramodwelcome'
# print(str[::-1])

#emoclewdomarp




