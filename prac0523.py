# Pre ####
# Generate a list of 100 unique random numbers, each number is a range from 1 to 1000
import random
list = []
for i in range(100):
  num = random.randint(1,1000)
  if num not in list:
    list.append(num)
  
print(list)  
  