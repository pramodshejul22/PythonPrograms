#string slicing

# #Q print only hello out of Hello world
# s='Hello world'
# print(s[:5])  #Hello
#
# str='Python Programming'  #print only programming
# print(str[7:]) #Programming

#Q- Negative slicing
#Q print only world out of Hello world!   - Negative slicing
# s='Hello world!'
# print(s[-6:-1])  #Hello
#
# str='Python Programming'  #print only Python
# print(str[-18:-12]) #Python


#Skipping value   - always start with 1

# s='pramods'
# print(s[::1])  #pramods
#
# print(s[1::2])  #rmd
#
# print(s[0::3])  #pms
#
# print(s[::4])   #po


# s='shubham'   #
# print(s[1:5:2])   #hb   #start from 1, end 5 means h, and skip 2-1=1  output-->hb


# #Q  - write positive slicing 'abcdefg' and return only 'aceg'     #code optimization means don't write one extra word
# sli='abcdefg'
# print(sli[::2])   #aceg

#Q write code in string '123456789' and skip every third value and print 147 output.
# no='123456789'
# print(no[::3])  #147