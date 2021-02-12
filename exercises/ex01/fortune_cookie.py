"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730230843"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

print("Your fortune cookie says...")

a: str = "You will have a good day"
b: str = "UNC will beat Duke forever!"
c: str = "You will crush the souls of those that dare defy you."
d: str = "You will meet someone important today!"

x: int = randint(1, 4)
if x == 1:
    print(a)
else:
    if x == 2: 
        print(b)
    else:
        if x == 3:
            print(c)
        else: 
            print(d)


print("Now, go spread positive vibes!")
