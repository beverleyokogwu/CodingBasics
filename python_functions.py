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
    return z
print(maxofthree(1,45,5))

'''
2. Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20
'''
def sum_of_num(list):
    sum=0
    for num in list:
        sum+=num
    return sum


print(sum_of_num([8, 2, 3, 0, 7]))


'''
3. Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336
'''
def mult_of_num(list):
    mult=1
    for num in list:
        mult*=num
    return mult


print(mult_of_num([8, 2, 3, -1, 7]))
