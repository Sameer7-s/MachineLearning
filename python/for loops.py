# age = int(input("Enter age: "))
# income = int(input("Enter income: "))

# if age >= 18 or age <=60:
#     print("yes")
# elif income > 30000:
#     print("yes")
# else:
#     print("no")

# str = "apnacollege"

# for char in str:
#         if(char == 'o'):
#             print("o found")
#             break
#         print(char)
# print("END")

### print the element of the following list using a loop :

# nums = [1,4 , 9 , 16 , 25 , 36 , 49, ]
# for el in nums :
#       print(el)


###search for a number x in this tuple using loop


# nums = [1,4 , 9 , 16 , 25 , 36 , 49, 49 ]
# x = 49
# idx = 0
# for el in nums :
#       if( el == x):
#             print ("number found at idx : ",idx)
#       idx += 1



###RANGE FUNCTION IN PYTHON 

# seq = range(20)
# for i in  seq:
#     print(i)

### or we can write as also :
# for i in range(20):
#     print(i)


# ######### range 

####MODULE 5 OF THE TUTEDUDE LECTURE 



# name = ["sameer","sourabh","raj"]
# print(len(name))



## print total number 

# a = [1,3,4,5,2,53,52,54,63,32]
# total = 0
# for A in a:
#     total = total + A
#     print(f"total num is {total}")


#     num = [ 12,3,45,65,65,33,53,67,43,78,32]
# total = 0
# for nums in num:
#     total = total+nums
# print(f"total number is {total}")




# a = [1,2,3,4]
# total = 0
# for A in a:
#     total = total+A
# print(f"sum  is {total}")



# num = [ 12,3,45,65,65,33,53,67,43,78,32]
# print(sum(num))


### PRINT HIGHEST SCORE FROM THE TABLE 

# scores = [ 12,3,45,65,65,33,53,67,43,78,32]
# highest = scores[0]
# for score in scores:
#     if highest <score :
#        highest = score
# highest = max(scores)
# print(f"highest score is {highest}")




# nums = [ 12 , 43,53,66,2224,31]
# highest = nums[0]
# for num in nums:
#     highest < num
#     highest = num
# highest = max(nums)
# print(f"highest num is {highest}")




## PRINT HIGHEST SCORE FROM THE TABLE 

# scores = [ 12,3,45,65,65,33,53,67,43,78,32]
# lowest = scores[0]
# for score in scores:
#     if lowest >score :
#        lowest = score
# lowest = min(scores)
# print(f"lowest score is {lowest}")




# nums = [1, 2,3,4,5,22,55,333,5]
# lowest = nums[0]

# for num in nums:
#      if lowest > num:
#         lowest = num
# lowest = min(nums)
# print(f"lowest number is {lowest}")




###skipppiing num which is div by 3
# for num in range(10): 
#     if num%3 == 0:
#         continue
#     print(num)



# ### even number  2 4 6 8 
# for num in range(10):
#     if num%2 != 0:
        # continue
#     print(num)




### skip number which is div by 2 

# for num in range(10):
#     if num%2 == 0:
#         continue
#     print(num)




#### BREAK FUNCTION  


# for num in range(1,10):
#     if num ==5:
        
#         break
#     print(num)
    





#####


# n = int(input("Enter a number: "))
# if n <= 1:
#     print("not prime")
# elif n == 2:
#     print("prime")
# else:
#     is_prime = True
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print("prime")
#     else:
#         print("not prime")






        # Here are **simpler versions** of the prime number checker:



# n = int(input("Enter a number: "))

# if n <= 1:
#     print("not prime")
# else:
#     is_prime = True
#     for i in range(2, n):
#         if n % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print("prime")
#     else:
#         print("not prime")








# def check_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# n = int(input("Enter a number: "))
# if check_prime(n):
#     print("prime")
# else:
#     print("not prime")










## **Version 3: One-Line Logic (Compact)**
# ```python
# n = int(input("Enter a number: "))

# if n <= 1:
#     print("not prime")
# elif all(n % i != 0 for i in range(2, n)):
#     print("prime")
# else:
#     print("not prime")



## **Version 4: Simplified with Comments (Educational)**
# # ```python
# # Get input
# n = int(input("Enter a number: "))

# # Numbers less than 2 are not prime
# if n < 2:
#     print("not prime")
# else:
#     # Check if n is divisible by any number from 2 to n-1
#     for i in range(2, n):
#         if n % i == 0:
#             print("not prime")
#             break
#     else:  # This else belongs to for loop
#         print("prime")










n = int(input("Enter a number: "))
count = 0


for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1


if count == 2:
    print("prime")
else:
    print("not prime")





































































