print("this is an easy python function that basically displays output to the user...")

'''
All questions originate from w3resource:
Source: https://www.w3resource.com/python-exercises/python-functions-exercises.php
'''

'''
1. Write a Python function to find the Max of three numbers.
'''
# My basic solution
def maxofthree(x,y,z):
    if x>y and x>z:
        return x
    elif y>z:
        return y
    else:
        return z
print(maxofthree(1,45,5))
