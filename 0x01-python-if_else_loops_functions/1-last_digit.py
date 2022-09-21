#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_num = (abs(number) % 10) * -1
else:
    last_num = number % 10

str1 = "Last digit of {} is {}".format(number, last_num)
if last_num > 5:
    print(str1 + " and is greater than 5")
elif last_num == 0:
    print(str1 + " and is 0")
else:
    print(str1 + " and is less than 6 and not 0")
