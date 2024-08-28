'''
The following program allows the weights of 15 bags of rice to be input. 
The correct weight for each bag of rice must be 
between 4.9 kg and 5.1 kg inclusive.
'''
bags_rice = int(input("Enter number of bags")) #1
upper_bound = 5.1
lower_bound = 4.9
count_under = 0
count_over = 0
count_correct = 0
for count in range(bags_rice):
    bag_weight = float(input("Enter the weight of the bag of rice "))
    if bag_weight <= upper_bound and bag_weight >= lower_bound:#2
        print("The bag of rice is the correct weight")
        count_correct += 1
    if bag_weight > upper_bound:
        print("The bag of rice is overweight")
        count_over += 1#3
    if bag_weight < lower_bound:
        print("The bag of rice is underweight")
        count_under += 1#3
print("There were",count_over,"rice bags overweight")
print("There were",count_under,"rice bags underweight")
print("There were",count_correct,"rice bags with the correct weight")
'''
Open the file RICEBAGS.py
Save the file as MYBAGS_<your name>_<center number>_<index number>.py

1.	Edit the program so that it:
a.	Accepts the weights for only 10 bags of rice.
[1]
'''

'''
b.	Prints out the message “The bag of rice is the correct weight” 
when a weight entered is between 4.9kg and 5.1 kg inclusive.
[2]
'''

'''
c.	Prints out the number of bags of rice that were underweight, 
as well as the number that were overweight, after the weights of 
all the bags have been entered.
[5]
'''

'''
Save your program.
2.	Save your program as VARBAGS_<your name>_<center number>_<index number>.py
Edit your program so that it works for any number of bags of rice.
Save your program.
[2]
'''