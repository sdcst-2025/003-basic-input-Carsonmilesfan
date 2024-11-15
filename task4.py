#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912

import math
print("what are your variables")
question1 = "height = "
question2 = "radius = "
h = int(input(question1))
r = int(input(question2))
AA = r + math.sqrt(h**2+r**2)
A = math.pi*r*AA
print(f"your surface area is {A}")