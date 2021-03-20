__author__ = "aliyousuuf@gmail.com"

"""Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.
Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime
import calendar


def days_in_month(year, month):

    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    if year > datetime.MAXYEAR or year < datetime.MINYEAR:
        return 0
    elif month < 1 or month > 12:
        return 0
    else:
        cal = calendar.monthcalendar(year, month)
        return max(cal[len(cal) - 1])


def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    try:
        datetime.date(year, month, day)
        return True
    except ValueError:
        return False


def days_between(year1, month1, day1, year2, month2, day2):

    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    if is_valid_date(year1, month1, day1) is False:
        return 0
    elif is_valid_date(year2, month2, day2) is False:
        return 0
    else:
        d1 = datetime.date(year1, month1, day1)
        d2 = datetime.date(year2, month2, day2)
        time_diff = d1 - d2
        if time_diff.days < 0:
            return abs(time_diff.days)
        else:
            return 0


def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    if is_valid_date(year, month, day) is False:
        return 0
    else:
        given_date = datetime.date(year, month, day)
        today_date = datetime.date.today()
        time_diff = given_date - today_date
        if time_diff.days < 0:
            return abs(time_diff.days)
        else:
            return 0
