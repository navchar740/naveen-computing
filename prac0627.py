# Write a function to validate that a string is a valid postal code
#              Valid postal code only contains numbers and only have 6 digits
# Test case 1: example input: 319191, example output: True
# Test case 2: example input: 3564a, example output: False
############ Write your code here #####################
def postcode(code):
    if len(code) == 6 and code.isdigit() == True:
        return True
    else:
        return False
        
# while True:
#     new_code = input("Enter new code:")
#     is_valid = postcode(new_code)
#     if is_valid == True:
#         print(f'{new_code} is valid')
#         break
#     else:
#         print(f'{new_code} is invalid. Try again')


    
# Easy Questions
# Question 1: Write a function to check if the length of a string is exactly 5 characters
# Test case 1: example input: hello, example output: True
# Test case 2: example input: python, example output: False
# Challenge: Keep asking for input until True
############ Write your code here #####################
def characters(num):
    if len(num) == 5:
        return True
    else:
        return False

#while True:
    #new_num = input("Enter new characters:")
    #is_valid = characters(new_num)
    # if new_num == True:
    #     print("True")
    #     break
    # else:
    #     print("False")



# Question 2: Write a function to check if the length of a list is greater than 3
# Test case 1: example input: [1, 2, 3, 4], example output: True
# Test case 2: example input: [1, 2], example output: False
test1 = [1, 2, 3, 4]
test2 = [1, 2]
############ Write your code here #####################
# def length(list):
#     if len(list) > 3:
#         return True
#     else:
#         return False
    
# print(length(test1))  
# print(length(test2)) 

# Question 3: Write a function to check if the length of a string is less than or equal to 8 characters
# Test case 1: example input: computer, example output: True
# Test case 2: example input: programming, example output: False
# Challenge: Keep asking for input until True
############ Write your code here #####################
# def length_1(string_1):
#     if len(string_1) <= 8:
#         return True
#     else:
#         return False
        
# while True:
#     new_string = input("Enter new code:")
#     is_valid = length_1(new_string)
#     if is_valid == True:
#         print("True")
#         break
#     else:
#         print("False")
        
    
    



# Normal Questions
# Question 4: Write a function to validate a password to be at least 8 characters long, 
#             and contains numbers and alphabets
# Test case 1: example input: password, example output: True
# Test case 2: example input: pass, example output: False
# Challenge: Keep asking for input until True
############ Write your code here #####################
# def length_1(string_1):
#     if len(string_1) >= 8 and string.isalnum():
#         return True
#     else:
#         return False

# while True:
#     new_string = input("Enter new code:")
#     is_valid = length_1(new_string)
#     if is_valid == True:
#         print("True")
#         break
#     else:
#         print("False")

# Question 5: Write a function to validate a username to be between 5 and 10 characters long
# Test case 1: example input: user123, example output: True
# Test case 2: example input: longusername, example output: False
# Challenge: Keep asking for input until True
############ Write your code here #####################
# def user_name(string_1):
#     if len(string_1) >= 5 and len(string_1) <= 10:
#         return True
#     else:
#         return False

# while True:
#     new_string = input("Enter new code:")
#     is_valid = user_name(new_string)
#     if is_valid == True:
#         print("True")
#         break
#     else:
#         print("False")

# Question 6:  Write a function to Check if a string has an even number of characters
# Test case 1: example input: even, example output: True
# Test case 2: example input: odd, example output: False
############ Write your code here #####################
# def even_number(string_1):
#     if len(string_1) % 2 == 0:
#          return True
#     else:
#         return False

# while True:
#     new_string = input("Enter new code:")
#     is_valid = even_number(new_string)
#     if is_valid == True:
#         print("True")
#         break
#     else:
#         print("False")

# Question 7:  Write a function to validate that a string is a valid postal code
#              Valid postal code only contains numbers and only have 6 digits
# Test case 1: example input: 319191, example output: True
# Test case 2: example input: 3564a, example output: False
############ Write your code here #####################
# def postal_code(string_1):
    
#     if len(string_1) == 6:
#         return True
#     else:
#          return False

# while True:
#      new_string = input("Enter new code:")
#      is_valid = postal_code(new_string)
#      if is_valid == True:
#          print("True")
#          break
#      else:
#          print("False")
         
# Question 8: Check if a number is a prime number
# Test case 1: example input: hello, example output: True
# Test case 2: example input: python, example output: False
############ Write your code here #####################


# Write a function for the below
# Question 9: Validate an email to be at least 10 characters long and contain an '@'
# Test case 1: example input: test@example.com, example output: True
# Test case 2: example input: user@, example output: False
############ Write your code here #####################



# Hard Questions
# Write a function for the below
# Question 10: Validate an NRIC number to be valid
# length of NRIC must be 9, Starts with S or T, followed by 7 digits, followed by an alphabet
# Test case 1: example input: S9956532Z, example output: True
# Test case 2: example input: Z3215642@, example output: False
############ Write your code here #####################



    

    