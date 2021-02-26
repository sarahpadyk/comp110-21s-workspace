"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730230843"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    # TODO 2: Print the result of calling your fortune_cookie function.
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


a: str = "You will have a good day"
b: str = "UNC will beat Duke forever!"
c: str = "You will crush the souls of those that dare defy you."
d: str = "You will meet someone important today!"

# TODO 1: Define your fortune_cookie function here.


def fortune_cookie() -> str:
    """Fortune Cookie random return."""
    x: int = randint(1, 4)
    if x == 1:
        return(a)
    else:
        if x == 2: 
            return(b)
        else:
            if x == 3:
                return(c)
            else: 
                return(d)


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
