# user  = {
#     "user_name " : "Sameer",
#     "password" : "syfer@6387",
#     "email" : "singhsameer80618@gmail.com",
#     "address":"SBC road 4500055",
#     "country": "INDIA"
# }
# sensitive_info = ["password","address"]

# for key in user:  
#####  this gives error bcs dict changed size during iteration in upper side the dictionaries has length of 5 
## so what you learn on this if you running a loop on dictionaries  and you trying to  change the same dictionary  So that  will not work on the python 
#     if key in sensitive_info:
#         user.pop(key)

# for i in sensitive_info:
#     user.pop(i)

# print(user)





### IF YOU WANT TO PRINT WHICH KEY VALUE PAIR GOT DELETED SO SHOULD WHAT YOU DO

# user  = {
#     "user_name " : "Sameer",
#     "password" : "syfer@6387",
#     "email" : "singhsameer80618@gmail.com",
#     "address":"SBC road 4500055",
#     "country": "INDIA"
# }
# sensitive_info = ["password","address"]

# for i in sensitive_info:
#     print(f"key:{i}, value:{user[i]}")
#     user.pop(i)

# print(user)


## what if we do if key is not present in dictionaries

user  = {
    "user_name " : "Sameer",
    "password" : "syfer@6387",
    "email" : "singhsameer80618@gmail.com",
    "address":"SBC road 4500055",
    "country": "INDIA"
}
sensitive_info = ["password","address","phone"]

for i in sensitive_info:

    if i in user:
        print(f"deleted => {i}, value:{user[i]}")
        user.pop(i)
    else:
        print(f"{i} not present")

print(user)

