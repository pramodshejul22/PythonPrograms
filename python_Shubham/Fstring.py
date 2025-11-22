#day-8 fstring
#
# name = "Pramod"
# age = 29
# greet = f"Hello {name}, you are {age} years old"
#
# print(greet)   #Hello Pramod, you are 29 years old


#Q-write a program that ask user to enter name and age, then print msg saying Hello{name}, you are {30} years old.

# str = input("Enter the name:-")
# age = input("Enter the age:-")
# msg = f"Hello {str}, you are {age} years old"
#
# print(msg)

#output
# Enter the name:-sai
# Enter the age:-11
# Hello sai, you are 11 years old

#Q-write a program that takes two numbers from users and adds them and print result.
#here require type casting to print sum of all no.
# num1 = int(input("Enter the first number:"))
# num2 = int(input("Enter the second number:"))
# sum = num1+num2
# num3 = f"User first numer: {num1}, and User second number: {num2} and sum of all: {sum}"
# print(num3)

#without typecasting output
# Enter the first number:2
# Enter the second number2
# User first numer: 2, and User second number: 2 and sum of all: 22

#With type casting output (use int func only for type casting)
# Enter the first number:5
# Enter the second number:10
# User first numer: 5, and User second number: 10 and sum of all: 15

#need to check how to addition do of user numbers



#prog 3 - write the program that defines three variables a,b,c and assign values them 5,10,15 respectivelly and print sum.
# a = int(input("Enter first numer:"))
# b = int(input("Enter the second number:"))
# c = int(input("Enter the thired number:"))
# sum = a+b+c
# print(sum)  #30

#Approach second
# numa=5
# numb=10
# numc=15
# sumall=numa+numb+numc
# print(sumall)


#Program - Write a program that converts a given temperature from celsius to farhenheit.
#The formula is  F=C*9/5+32
#
# celsius = int(input("Enter a temp in celcius:"))
# print(type(celsius))
# farheneit = celsius * 9/5+32
# print(type(farheneit))
