# 13198061

def day_of_year(d, m):
    # d = day of month
    # m = month of year 2020
    # returns -1 if the date/month combination is not possible
    # first date is 1, 1

    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if days[m] >= d > 0:
        if m == 1:
            return d - 1
        else:
            total = -1
            for i in range(1, m):
                total += days[i]
            return total + d
    else:
        return -1
