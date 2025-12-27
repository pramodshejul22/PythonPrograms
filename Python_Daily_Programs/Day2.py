#Program 1 - WAPP to fetch all words from string which starts and end with vowels.
# st="Australiya won more word cup than india"
# s1=st.split()
# Newlist=[]
# for i in s1:
#     if i[0] in 'aeiou' and i[-1] in 'aeiou':
#         Newlist.append(i)
#         print(Newlist)

#o/p
#['india']

#Program 2 - WAPP to fetch all words from string which starts vowels and end with consonant.
# st='python is simple and easy language'
# st1=st.split()
# v='aeiou'
# newstring=[]
# for i in st1:
#     if i[0] in v and i[-1] not in v:
#         newstring.append(i)
# print(newstring)

#o/p
#['is', 'and', 'easy']

#Program 3 - WAPP to fetch all words from string which starts consonant and end with vowels.

# st='python is simple and easy language'
# st1=st.split()
# v='aeiou'
# newstring=[]
# for i in st1:
#     if i[0] not in v and i[-1] in v:
#         newstring.append(i)
# print(newstring)

#o/p
# ['simple', 'language']

#Program 4 - WAPP to fetch all words from string which starts consonant and end with vowels.
# Using Comprehension
# st='python is simple and easy language'
# st1=st.split()
# v='aeiou'
#
# print([i for i in st.split() if i[0] not in v and i[-1] in v])

#o/p
# ['simple', 'language']

#program 5 - WAPP fo fetch all vowels from string

st="Hyderabad"
v='aeiou'
newlist=[]
for i in st:
    if i in v:
        newlist.append(i)
print(newlist)

#Using List comprehension
print([i for i in st if i in v])

#o/p
# ['e', 'a', 'a']
# ['e', 'a', 'a']