import random

lower_bound = int(input("Enter lower bound: "))
upper_bound = int(input("Enter upper bound: "))

print(random.randint(lower_bound + 1, upper_bound - 1))
