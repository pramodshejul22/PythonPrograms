#D10 Nested string

# Nested_list = [[1,2,3,4,[5,6,7,[8,9,10]]]]
# print(Nested_list[3][1])


# nested_list = [[1, 2, 3,[4, 5, 6,[7, 8, 9]]]]
# #
# # for sublist in nested_list:
# #     print(sublist)
#
# print(nested_list)

#Approach 1
# list=[1,2,3,'abcd',5]
# print(list[3][3])
#o/p -->  d

#Approach 2
# list=[1,2,3,'abcd',5]
# print(list[-2][-1])
#
# #o/p -->  d

list=[1,2,3,4,5]
print(list[::-1])  #[5, 4, 3, 2, 1]
print(list)        #[1, 2, 3, 4, 5]
list.reverse()     #[5, 4, 3, 2, 1]
print(list)