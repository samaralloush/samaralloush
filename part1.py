'''
def is_leap_year(year):

 

In this function, you should apply the following rules for determining whether the year is a leap year, as follows:

    If the year is divisible by 4, it is likely to be a leap year... but:
        If those years are evenly divisible by 100 but not 400, it is not a leap year.
        If those years are evenly divisible by 100 and 400, then it is a leap year.
        All remaining years divisible by 4 are leap years
    If the year is not divisible by 4, it is not a leap year.


If the year is a leap year. return True. Otherwise, return False.

Invoke (call) this function in your code and store the result in a variable.

Print your assigned variable to the console window.
Attach your python file as a solution to this question.
'''


def is_leap_year(year):
    if year %4 != 0:
        return False
    else:
        while year %4==0:
            if year %100==0 and year %400==0
               return true 
            elif year %100==0 and year% 400 != 0
               return False
            else 
            return true 

    return

print is_leap_year(2000)
