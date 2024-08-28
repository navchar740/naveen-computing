'''
Task 2 
You have been asked to write a program that will create a password for a user. 
Open the file RM_SP.py 
You will see the following function that: 
Takes the name of the user 
Returns a text string of the name without the spaces 
'''

def removesp(text): 
    newtext = "" 
    for char in text: 
        if char.isspace() != True: 
            newtext += char 
    return newtext
var1 = removesp("singapore is a fine city")
print(var1)
'''
6. In your program, write a function changecase() that: 
Takes a single character as a parameter 
Returns the following: 
The lowercase letter of the character if the character is a uppercase alphabet 
The uppercase letter of the character if the character is a lowercase alphabet 
The character if the character is not an alphabet 
Save your program as CHGCASE_<your name>_<class>_<index_number>.py [3] 
'''

##### check if alphabet >>> .isalpha()
##### check if upper case >>> .isupper() /// .islower()
##### change to upper case >>>> .upper()
def changecase(char):
    if char.isalpha():
        if char.isupper():
            return char.lower()
        #if char.islower():
        else:
            return char.upper()
    else:
        return char
    # if islower.text[count] == True:
    #     text[count] = text.upper()
    # if isupper.text[count] == True:
    #     text[count] = text.lower()
    # else:
    #     return text 
var1 = changecase('A')
var2 = changecase('b')
var3 = changecase('6')

print(var1)
print(var2)
print(var3)

            
    
'''
7. Extend the program by writing a function pwdgenerate() that: 
Takes the name of the user as a parameter 
Removes the spaces in the name using the removesp() function 
Creates a password by taking each alternate character in the name (without spaces) 
and changing the case of the character using changecase() function 
Appends a random digit of 0 to 9 inclusive at the end of the password 
Returns the generated password 

Sample Executions: 
>>> pwdgenerate(“John Tan”) 
‘jHtN2’ 

>>> pwdgenerate(“jOHN tAN”) 
‘JhTn9’ 

Save your program as PWDGEN_<your name>_<class>_<index_number>.py	[5] 
'''
import random
def pwdgenerate(name):
    new_name = removesp(name)
    password = ""
    new_name = new_name[::2]
    for i in new_name:
        letter = changecase(i)
        password += letter
    rannum = random.randint(0,9)
    return password + str(rannum)

N1 = pwdgenerate("John Tan")        
print(N1)
   
        
        
'''
8. Save your program as PASSWD_<your name>_<class>_<index_number>.py 
Extend your program to create a user interface. The program must: 
Allow the user to input the name of the user with a suitable prompt message 
Loop until the user enters a valid name that has at least 5 characters with a suitable error message 
Generate and display the generated password of the user with a suitable message. 

Save your program [4] 
'''
while True:
    name = input("Type your name:")
    if len(name) < 5:
        print("Name needs atleast 5 characters")
    else:
        pwd = pwdgenerate(name)
        print(pwd,"is your password")
        break

    
# name = ""
# while len(name) < 5:
#     name = input("What is your name? ")

# ######

    
