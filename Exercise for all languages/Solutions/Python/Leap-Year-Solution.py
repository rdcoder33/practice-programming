# Question 1 Leap Year


# Solution


def is_leap_year(year):
    if year % 400 == 0 or year % 4 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return False


# Not there could be multiple answers to this problem,
# I have provided a beginner friendly answer
