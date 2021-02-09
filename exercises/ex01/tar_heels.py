"""An exercise in remainders and boolean logic."""

__author__ = "730230843"


# Begin your solution here...


x: str = input("Enter an integer, please.")
if int(x) % 2 == 0 and int(x) % 7 == 0:
    print("TAR HEELS")
else:
    if int(x) % 2 == 0:
        print("TAR")
    else: 
        if int(x) % 7 == 0:
            print("HEELS")
        else: 
            print("CAROLINA")
