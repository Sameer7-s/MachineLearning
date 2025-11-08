###Functions 

### use redonedency kam krne ke liye ( repeations of same line at multiple time )


## add of two number using function 
#### (1.)
# def calc_sum(a,b): 
#     sum = a+b
#     print(sum)
#     return sum 

# calc_sum(5 , 10)#funtion call (arguement )
# # a = 5
# # b = 10
# calc_sum(47,39)

# calc_sum(4,2)


####also we can write by this method
###(2.)


#function definition

# def calc_sum(a,b):# a,b parameter
#     return a+b
# sum = calc_sum(1,5)#function call : Arguements 
# # print(sum)

# def print_hello():
#     print("hello")

# print_hello()
# print_hello()
# print_hello()
# print_hello()
# print_hello()


# def print_hello():
#     print("hello")

# output = print_hello()
# print(output) ### output is NONE

### WAP TO PRINT AVG OF THE THREE NUMBERS IN FUNCTION

## M1
# def calc_avg(a,b,c):
#     sum = a + b + c
#     return a+b+c/3,"sum is :",sum


# avg = calc_avg(2,5,23)
# print(avg)
# print(sum)

##N2
# def calc_avg(x,y,z):
   
#     avg = x+y+z/3
#     return avg

# avg = calc_avg(2,2,2)
# print(avg)

###TYPES OF FUNCTION 

## (1ST  = BUILT IN FN )
## Print() , len() , type (), range()

## 2nd (User defined function)

## default parameters (assigining a default value to a parameter , which is used when no arguement is passed )

# def calc_prod(a ,b=2):
#     print (a*b)
#     return a*b
# calc_prod(1)




###WAP TO PRINT THE LENGTH OF THE LIST (LIST IS THE PARAMETER )

# cities = [ "delhi","noida","goa","chennai", "sam","sja"]
# heros = [ "akshay ", "rithik", "antman "]
# len(cities)
# def print_len(list):
#     print_len(list)

# print(len(cities))
# print(len(heros)) 


# #### WAP TO PRINT THE ELEMENT OF A LIST IN A SINGLE LINE (LIST is the parameter)


# cities = [ "delhi","noida","goa","chennai"]
# heros = [ "akshay ", "rithik", "antman "]


# def print_len(list):
#     print_len(list)

# def print_list(list):
#     for item in list:
#           print(item,end=" ")

# print_list(heros)
# print_list(cities)
# print()




# cities = input("enter the str: ")

# len(cities)
# def print_len(cities):
#     print_len(cities )

# print(len(cities))
# # print(len(heros)) 



# def length():
#     name = input("enter str: ")
#     n = len(name)
#     return n

# print("length of the str")
# str_len = length()
# print("length of the str  = ", str_len)




# def factorial(n):

#     if n < 0:
#         return 
#     if n == 0 or n == 1:
#         return 1
    

#     return n * factorial(n-1)

# number = int(input("Enter a positive number: "))
# result = factorial(number)
# print(f"Factorial of {number} is: {result}")



# def find_largest(num1, num2, num3):

#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))


# largest = find_largest(a, b, c)
# print(f"The largest number among {a}, {b}, and {c} is: {largest}")


# correct_password = "python"

# while True:
#     user_password = (input("enter your password : "))
#     if user_password == correct_password:
#         print("password is correct !congrats.")
#         break
#     else:
#         print("password is incorrect, try again")


# print("logged in succesfully")

0.
# import random

# print(random.random())### it will generate randomly num from the 0.0 to 0.1




# letter = input("Enter a letter: ")


# letter = letter.lower()

# if len(letter) != 1:
#     print("Please enter a single letter only")
# elif not letter.isalpha():
#     print("Please enter a letter, not a number or symbol")

# elif letter in 'aeiou':
#     print(f"{letter} is a Vowel")
# else:
#     print(f"{letter} is a Consonant")




# import random 
# nums = [1,2,3,4,5,6,67,8,89,9,87]

# print(random.choice(nums))


# def check_vowel_consonant(letter):

#     letter = letter.lower()
    
#     if len(letter) != 1:
#         return "Please enter a single letter only"
    
#     if not letter.isalpha():
#         return "Please enter a letter, not a number or symbol"
    
#     if letter in 'aeiou':
#         return f"{letter} is a Vowel"
#     else:
#         return f"{letter} is a Consonant"

# # Get input from user
# letter = input("Enter a letter: ")
# result = check_vowel_consonant(letter)
# print(result)

# # Palindrome checker function
# def is_palindrome(value):
	
# 	s = str(value)
# 	cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
# 	return cleaned == cleaned[::-1]

# user_input = input("Enter a string or number to check for palindrome: ")
# if is_palindrome(user_input):
# 	print(f"'{user_input}' is a palindrome")
# else:
# 	print(f"'{user_input}' is not a palindrome")
	

# # nums = 123452345


# ch = input("enter the ch :")

# vowel = 'a','i','e','o','u'

# if ch == vowel:
	# print("print ")




 

# letter = input("Enter a letter: ")


# letter = letter.lower()

# if len(letter) != 'aieou':
#     print("Please enter a single letter only")
# if letter.isalpha():
#     print("Please enter a letter, not a number or symbol")

# elif letter in 'aeiou':
#     print(f"{letter} is a Vowel")
# else:
#     print(f"{letter} is a Consonant")














# letter = input("Enter a letter: ").lower()

# if len(letter) != 1:
#     print("Please enter a single letter only")
# elif not letter.isalpha():
#     print("Please enter a letter, not a number or symbol")
# elif letter in 'aeiou':
#     print(f"{letter} is a Vowel")
# else:
#     print(f"{letter} is a Consonant")



# string = input("Enter the string: ")

# vowels = 0
# consonants = 0
# digits = 0
# special_chars = 0

# for ch in string:
#     if ch.isalpha():
#         if ch.lower() in "aeiou":
#             vowels += 1
#         else:
#             consonants += 1
#     elif ch.isdigit():
#         digits += 1
#     else:
#         special_chars += 1

# print("Vowels:", vowels)
# print("Consonants:", consonants)
# print("Digits:", digits)
# print("Special characters:", special_chars)




# s = input("Enter a string: ")


# clean = ''.join(ch.lower()
#  for ch in s if ch.isalnum())


# if clean == clean[::-1]:
#     print("Palindrome")
# else:
#     print("Not palindrome")

