#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2

print("solve 2a + 4b + 6c")
print ("What are your a, b, and c values?")
question1 = "a = "
question2 = "b = "
question3 = "c = "
response1 = int(input(question1))
response2 = int(input(question2))
response3 = int(input(question3))
x = 2*response1 + 4*response2 + 6*response3
print(f"your answer is {x}")