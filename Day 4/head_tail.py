# generating the head and tail using the random module

import random

num = random.randint(0,1)
print(num)
if num == 0:
    print("Head")
else:
    print("Tail")