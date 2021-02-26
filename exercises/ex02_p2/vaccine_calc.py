"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730230843"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))

    # TODO 2: Call days_to_target and store result in a variable.

    days: int = days_to_target(population, doses, doses_per_day, target)

    # TODO 4: Call future_date and store result in a variable.

    date_call: str = future_date(int(days)) 

    # TODO 5: Print the expected output using the variables above.

    a: str = "We will reach "
    b: str = str(target)
    c: str = "% vaccination in "
    d: str = str(days)
    e: str = " days, which falls on "
    f: str = str(date_call)
   
    print(a + b + c + d + e + f)


# TODO 1: Define days_to_target function

def days_to_target(a: int, b: int, c: int, d: int) -> int:
    """Returns days."""
    decimal_target: float = ((int(d)) / 100)
    needed_pop_vaccinated: int = round(a * decimal_target)
    actual_population: int = int(needed_pop_vaccinated) * 2
    return (round((actual_population - b) / c))


# TODO 3: Define future_date function

def future_date(x: int) -> str:
    """Gives Future Date."""
    today: datetime = datetime.today()
    days_from_equation: timedelta = timedelta(x)
    printed_date: datetime = today + days_from_equation 
    return((printed_date.strftime("%B %d, %Y")))


if __name__ == "__main__":
    main()
