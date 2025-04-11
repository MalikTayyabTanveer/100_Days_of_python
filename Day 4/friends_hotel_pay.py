import random 

friends =  ["bawa","Tayyab","Umair","Obaid","Qudoos"]

#first way
number =  random.randint(0,4)
print(friends[number])

#second way 
#choice takes the sequence as an input
print(random.choice(friends))