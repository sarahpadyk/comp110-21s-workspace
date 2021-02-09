"""A vaccination calculator."""

__author__ = "730230843"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...

original_population_question: int = int(input("population:"))
doses_administered_question: int = int(input("doses administered:"))
doses_per_day_question: int = int(input("doses per day:"))
target_percent_vaccinated_question: int = int(input("Target percent vaccinated:"))

# trying to convert 50% to 0.5 here but having hard time 
decimal_target_percent: float = int(target_percent_vaccinated_question) / 100

# is this the correct way to change back into an integer using round function?
needed_pop_vaccinated: int = round(original_population_question * decimal_target_percent)

actual_population: int = int(needed_pop_vaccinated) * 2
amount_of_days: int = int(round((actual_population - doses_administered_question) / doses_per_day_question))


# then call datetime and timedelta stuff?
today: datetime = datetime.today()
one_day: timedelta = timedelta(1)
days_from_equation: timedelta = timedelta(amount_of_days)
printed_date: datetime = today + days_from_equation


# Concatenated string
a: str = "We will reach "
b: str = str(target_percent_vaccinated_question)
c: str = "% vaccination in "
d: str = str(amount_of_days)
e: str = " days, which falls on "
f: str = str(printed_date.strftime("%B %d, %Y."))
print(a + b + c + d + e + f)
