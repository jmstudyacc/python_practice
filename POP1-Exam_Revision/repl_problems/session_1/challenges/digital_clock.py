"""
given number of minutes passed since midnight, print how many hours & minutes are displayed on 24h clock
midnight is 00:00 on 24h clock

- floor division of the input by 60
- hour is the number returned
- modulo m by 60 to get the remainder
- minute is the number returned
"""


def digital_clock(m):
    hours, mins = (m // 60), m % 60
    print(hours, mins)


digital_clock(150)
digital_clock(180)
digital_clock(444)
digital_clock(1439)
