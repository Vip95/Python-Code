from functools import reduce


# Print the total of the all entry of the array
number = [1,2,3,4,5]
result = reduce ( lambda a,b : a+b, number )

print ( result )