


#Task 1: Create a function that says hello in 4 languages
#parameters: none
#return: none

def sayhello():
  print("Hello")
  print("Konnichiwa!")
  print("Salut")
  print("Bonjour")
sayhello()

'''
Example output:
Hello!
Konnichiwa!
Salut!
Bonjour
'''


#Task 2: Create a function that says hello in 4 languages
#parameters: name
#return: none
def sayhello(name):
  print("Hello", name)
  print("Konnichiwa!", name)
  print("Salut", name)
  print("Bonjour", name)
sayhello("Naveen")

'''
Example output:
Hello, John
Konnichiwa, John
'''


#Task 3: Create a function that introduces yourself to a friend
#parameters: yourname, myname
#return: none
def sayhello(my_name,name):
  # hello David, my name is Naveen
  print("Hello", my_name , ",my name is" ,name)
  print("Konnichiwa!", my_name, ",my name is " , name)
  print("Salut", my_name , ",my name is" , name)
  print("Bonjour", my_name ,",my name is" , name)
sayhello("Eddy","Naveen")
'''
Example output:
Hello, John, my name is Malcolm.
'''


#Task 4: Create a function that adds 3 numbers and returns the result
#parameters: num1, num2, num3
#return: answer
def sixnum(num_1,num_2,num_3,num_4,num_5,num_6):
  total=int(num_1)+int(num_2)+int(num_3)+int(num_4)+int(num_5)+int(num_6)
  
  return total
  
sixnum(6,87,45,33,21,11)
''''
Use this function to add 6 numbers together. i.e. call the function 2 times
the 6 numbers are 6, 87, 45, 33, 21, 11
'''


#Task 5: Create a function that calculates the area of a triangle
#parameters: base, height
#return: answer
def calcu(base, height):
  formula = 1/2 * base * height
  return formula
calcu(20, 34)
calcu(30, 87)
calcu(44, 99)
  
'''
Use this function to add up 3 triangle's areas
triangle1 is base 20, height 34
triangle2 is base 30, height 87
triangle3 is base 44, height 99
'''


#Task 6: Create a function that converts temperatures from Fahrenheit to Celsius.
#Parameters: temperature_f (float)
#Return: temperature_c (float)
def converter(temperature_f):
  temperature_c = (temperature_f - 32) * (9/5)
  print("The convertion of",temperature_f,"farenheit to degrees is", temperature_c)
converter(200)

  


#Task 7: Write a function that calculates the total cost
#after tax for a list of prices.

#[20084, 45000, 660000, 93938, 737362, 8373628]
#10% tax
list = [20084, 45000, 660000, 93938, 737362, 8373628]
def total_cost(prices,tax_rate):
  count = 0
while count < len(list):
  total += list[count]
  count += 1
return total *1.1

'''
Parameters: prices (list of floats), tax_rate (float)
Return: total_cost (float)
'''

'''
Task 8: Construct a function that reverses the items in a list.
You are not allowed to use list slicing or reverse

Parameters: inarray(list)
Return: modified_list

inarray = [1,2,3,4,5]
outarray = [5,4,3,2,1]
'''

'''
Task 9: Construct a function that reverses the characters in a string.
You are not allowed to use list slicing or reverse.
convert the output into lowercase

Parameters: instring(string)
Return: outstring(string)

instring = "BAZOOKA"
outstring = akoozab
'''

'''
Task 10: Create a function that continuously asks the user to 
input a valid email address until one is entered.

Parameters: 
Return: email (str)
'''

'''
Task 11: Create a function to calculate the sum of 
all even numbers in a given list.
Parameters: numbers (list of integers)
Return: sum_of_evens (int)

Example:
numbers = [1, 2, 3, 4, 5, 6]
sum_of_evens = 12
'''

'''
Task 12: Write a function that finds the smallest number in a list.
Parameters: numbers (list of integers)
Return: smallest (int)

Example:
numbers = [34, 79, 23, 54, 12]
smallest = 12
'''

'''
Task 13: Develop a function that determines if a word is a palindrome.
Parameters: word (str)
Return: is_palindrome (bool)

Example:
word = "radar"
is_palindrome = True
'''

'''
Task 14: Create a function that takes a list of words and 
returns a list of their lengths.
Parameters: words (list of str)
Return: lengths (list of int)

Example:
words = ["hello", "world", "python", "excellent"]
lengths = [5, 5, 6, 9]
'''

'''
Task 15: Write a function that multiplies all numbers in a list together.
Parameters: numbers (list of floats)
Return: product (float)

Example:
numbers = [1.5, 2.0, 4.0]
product = 12.0
'''

'''
Task 16: Develop a function that formats a date from YYYYMMDD to "DD/MM/YYYY" format.
Parameters: datestr (str)
Return: formatted_date (str)

Example:
datestr = "20230424"
formatted_date = "24/04/2023"
'''

'''
Task 17: Create a function that checks if a given year is a leap year.
FUNCTION is_leap_year(year)
    IF year MOD 4 EQUALS 0 THEN
        IF year MOD 100 EQUALS 0 THEN
            IF year MOD 400 EQUALS 0 THEN
                RETURN True  // It is a leap year
            ELSE
                RETURN False  // It is a century year but not divisible by 400
            ENDIF
        ELSE
            RETURN True  // Divisible by 4 but not a century year
        ENDIF
    ELSE
        RETURN False  // Not divisible by 4
    ENDIF
END FUNCTION

Parameters: year (int)
Return: is_leap_year (bool)

Example:
year = 2024
is_leap_year = True
'''

'''
Task 18: Write a function that returns the nth Fibonacci number.
FUNCTION fibonacci(n)
    IF n EQUALS 0 THEN
        RETURN 0
    ELSEIF n EQUALS 1 THEN
        RETURN 1
    ENDIF

    SET previous TO 0
    SET current TO 1
    FOR i FROM 2 TO n
        SET temp TO current
        SET current TO previous + current
        SET previous TO temp
    ENDFOR
    RETURN current
END FUNCTION

Parameters: n (int)
Return: fib_n (int)

Example:
n = 7
fib_n = 13
'''

'''
Task 19: Develop a function that replaces every letter in a string with the next letter in the alphabet.
Parameters: input_string (str)
Return: modified_string (str)

Example:
input_string = "abc"
modified_string = "bcd"
'''

'''
Task 20: Create a function that calculates the average of a list of numbers, excluding the highest and lowest values.
Parameters: numbers (list of floats)
Return: average (float)

Example:
numbers = [2, 3, 5, 7, 11]
average = 5.0
'''