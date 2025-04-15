#this provide the basic understanding of the random module in python

import random
#Random integer generator.
num = random.randint(0,10)
print(num)

#it generate the floating number between 0 to 1.
print(random.random()*10)

#it generate the floating point number between the given number(including them).
print(random.uniform(1, 5))