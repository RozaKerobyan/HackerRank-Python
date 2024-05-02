def is_leap(year):
    leap = True
    not_leap = False

    if year in (1800, 1900, 2100, 2200, 2300):
        return not_leap
    elif year % 4 == 0:
        return leap
    else:
        return not_leap
