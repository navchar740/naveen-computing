'''
2018 - Task 4 [20]
You have been asked to create a guessing game program.
The program should:
-	Allow player 1 to input a whole number between 1 and 50 inclusive, 
for player 2 to guess. There must be validation present to check that the 
number entered is between 1 and 50 inclusive.

-	Allow player 2 to have 5 guesses to correctly guess the number input by player 1. 
You do not need to validate the input for player 2.

-	Output “You guessed the correct number.” When player 2 inputs the same number 
as player 1. The game must end if the correct number is guessed.

-	Output “You did not guess the correct number.” When player 2 does not input 
the same number as player 1.

-	Output “Game over!” when player 2 has five incorrect guesses.
'''

'''
10.	Write your program and test that it works.
Save your program as MYGUESS1_<your name>_<center number>_<index number>.py
[10]
'''
# Write and test your code here
# count = 0
# while True:
#     player_1 = int(input("input a whole number between 1 and 50 inclusive: "))
    
#     if player_1 >= 1 and player_1 <= 50:
#         print("player 1 accepted")
#         break
#     else:
#         print("Try again")

# for i in range(5):
#     player_2 = int(input("Enter player 1's number"))
#     if player_2 == player_1:
#         print("You guessed the correct number")
#         break
#     else:
#         print("You did not guess the correct number")
#         count += 1
#         if count >= 5:
#             print("Game over!")
# # else:
#     # will run after the code in the for loop is complete
#     print("Game over!")
'''
11.	When your program is complete, test it for the following:
a.	Test 1 – Player 1 inputs the number 55
b.	Test 2 – Player 1 inputs the number 0
c.	Test 3 – Player 1 inputs the number 10 and player 2 guesses 
    the numbers 15 and 10
d.	Test 4 – Player 1 inputs the number 20 and player 2 guesses 
    the numbers 30, 35, 22, 15, 49
Take a screenshot of :
-	Test 1, 2 and 3. Save this single screenshot as: 
o	TEST123_<your name>_<center number>_<index number>
-	Test 4. Save this screenshot as:
o	Test4_<your name>_<center number>_<index number>
-	Save your files in either .png or .jpg format
[4]
'''
# Write and test your code here
           
'''
12.	Save your program as MYGUESS2_<your name>_<center number>_<index number>.py

Extend your program to identify if player 2’s guess is lower or higher 
than the number input by player 1. A suitable message must then be output.

Save your program.
[2]
'''
# Copy your code from above. Write and test your code here
# count = 0
# while True:
#     player_1 = int(input("input a whole number between 1 and 50 inclusive: "))

#     if player_1 >= 1 and player_1 <= 50:
#         print("player 1 accepted")
#         break
#     else:
#         print("Try again")

# for i in range(5):
#     player_2 = int(input("Enter player 1's number "))
#     if player_2 == player_1:
#         print("You guessed the correct number")
#         break
#     if player_2 > player_1:
#         print("You did not guess the correct number")
#         print("player 2 guess is higher than player 1")
   
#     if player_2 < player_1:
#         print("You did not guess the correct number")
#         print("player 2 guess is lower than player 1")
# else:
#     print("Game over")
    

'''
13.	Save your program as MYGUESS3_<your name>_<center number>_<index number>.py

Extend your program to allow player 2 to choose an easy, medium or hard game. 
An easy game allows eight guesses, a medium game allows six guesses and a 
hard game allows four guesses.

If player 2 inputs a correct guess, the program must output the 
number of guesses made.

You are not required to validate the input for player 2.

Save your program.
[4]
'''
count = 0
while True:
    player_1 = int(input("input a whole number between 1 and 50 inclusive: "))

    if player_1 >= 1 and player_1 <= 50:
        print("player 1 accepted")
        break
    else:
        print("Try again")

game = input("Enter game level ")
if game == "easy":
    n = 8
elif game == "medium":
    n = 6
elif game == "hard":
    n = 8
    
for i in range(n):
    player_2 = int(input("Enter player 1's number "))
    if player_2 == player_1:
        print("You guessed the correct number")
    
        break
    if player_2 > player_1:
        print("You did not guess the correct number")
        print("player 2 guess is higher than player 1")

    if player_2 < player_1:
        print("You did not guess the correct number")
        print("player 2 guess is lower than player 1")
else:
    print("Game over")


# Copy your code from above. Write and test your code here