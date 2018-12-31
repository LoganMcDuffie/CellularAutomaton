#               -- WHAT THIS SHOULD ACCOMPLISH --
# Define a procedure rabbits that takes as input a number n, and returns a
# number that is the value of the nth number in the rabbit sequence.
# For example, rabbits(10) -> 35. (It is okay if your procedure takes too
#                                long to run on inputs above 30.)

def rabbits(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2 and n < 6:
        return rabbits(n - 1) + rabbits(n - 2)
    elif n > 5:
        return rabbits(n-1) + rabbits(n - 2) - rabbits(n - 5)
    else:
        return "xD?"

print rabbits(10)
#>>> 35

s = ""
for i in range(1,12):
    s = s + str(rabbits(i)) + " "
print s
#>>> 1 1 2 3 5 7 11 16 24 35 52
