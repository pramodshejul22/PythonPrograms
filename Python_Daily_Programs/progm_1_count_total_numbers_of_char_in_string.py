#Youtube channel - Narayana 100 programs
#1 - WAPP to count the total numbers of characters in the given strings.

#Narayana

# st=input("Enter any string :")     ##Narayana
# count=0
# for i in st:
#     count=count+1
# print(count)

#output
# Enter any string :Narayana
# 8


#program :- 2  - write python program to remove spaces from string and count string

# st=input("Enter any string:")     #my name is pramod shejul
# count=0
# for i in st:
#     if i==' ':
#         continue
#     count=count+1
# print(count)

#0/p
# Enter any string:my name is pramod shejul
# 20

#Practice Program :- Remove space from string and print in same line output like
#input = my name is pramod shejul
#output = mynameispramodshejul

# st=input("Enter any string:")
# for i in st:
#     if i!=' ':
#         print(i, end="")

#Program 2 - WAPP to count total number of words in given string.
# st=input("Enter any string:")
# count=0
# st1=st.split()
# for i in st1:
#     count=count+1
# print(count)

#o/p
# Enter any string:my name is pramod
# 4

#Program 3 - WAPP to count all upper case character in the given string.

# st=input("Enter any string:")
# count=0
# for i in st:
#     if i.isupper():
#         count=count+1
# print(count)

#o/p
# Enter any string:PrAmOd ShEjUl
# 6

#Program 4 - WAPP to count vowels in given string.
# st=input("Enter any string:")
# count=0
# vowels='aeiou'
# for i in st:
#     if i in vowels:
#         count=count+1
# print(count)

#o/p
# Enter any string:my name is pramod shejul
# 7

#Program 5 - WAPP to count total number of special characters in the given string.
# st=input("Enter any string:-")
# import string
# lower=string.ascii_lowercase
# count=0
# for i in st:
#     if i not in lower:
#         count=count+1
# print(count)

#o/p
# Enter any string:-my@name#is&pramod%$
# 5

#program 6 - WAPP to count occurances of each vowel in the given string.
#narayana tech house hyderabad
# st=input("Enter any string:-")
# v='aeiou'
# d={}.fromkeys(v,0)
# for i in st:
#     if i in d:
#         d[i]=d[i]+1
# print(d)

#o/p
# Enter any string:-narayana tech house hyderabad
# {'a': 6, 'e': 3, 'i': 0, 'o': 1, 'u': 1}

#program 7 - WAPP to count the occurence of each unique character in the given string.

# st=input("Enter any string:-")
# st1=set(st)
# d={}.fromkeys(st1,0)
#
# for i in st:
#     d[i]=d[i]+1
# print(d)

#o/p
# Enter any string:-narayana
# {'y': 1, 'n': 2, 'a': 4, 'r': 1}

#program 8 - WAPP to fetch all words which contain even number of characters?
# python narayana tech house hyd
# st="python narayana tech house hyd"
# st1=st.split()
# newList=[]
# for i in st1:
#     if len(i)%2==0:
#         newList.append(i)
# print(newList)

#o/p
# ['python', 'narayana', 'tech']

#program - 9 - WAPP to fetch all words which starts with an vowel.
# st="Python is simple and easy language"
# st1=st.split()
# for i in st1:
#     if i[0].lower()in 'aeiou':
#      print(i)
#o/p
# is
# and
# easy

#program 10 - WAPP to fetch all words which start and end with consonant.

st='python is simple and easy language'
st1=st.split()
v=[]

for i in st1:
    if i[0].lower() not in 'aeiou' and i[-1].lower() not in 'aeiou':
        print(i)

#o/p
#python