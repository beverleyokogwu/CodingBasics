#print("this is an easy python function that basically displays output to the user...")

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
#print(maxofthree(1,45,5))

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


#print(sum_of_num([8, 2, 3, 0, 7]))


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


#print(mult_of_num([8, 2, 3, -1, 7]))

'''
4. Write a Python program to reverse a string. Go to the editor
Sample String : "1234abcd"
Expected Output : "dcba4321"
'''
def reverse(some_string):
    reversed_string_arr= []
    rev_string=""
    for char in some_string:
        reversed_string_arr.append(char)
    for s in range(len(reversed_string_arr)):
        rev_string+=reversed_string_arr.pop()
    return rev_string

#print(reverse("1234abcd"))

'''
5. Write a Python function to calculate the factorial of a number
(a non-negative integer). The function accepts the number as an argument.
'''
def fact(num):
    if num <=1:
        return 1
    else:
        return num * fact(num-1)
#print(fact(10))

'''
6. Write a Python function to check whether a number is in a given range.
'''
def in_range(num,r1,r2):
    if num >r1 and num<r2:
        return True
    return False

print(in_range(37,4,67))


'''
7. Write a Python function that accepts a string and calculate the number of
upper case letters and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12
'''
def tallyLetters(str):
    num_upper=0
    num_lower=0
    for char in str:
        if char.isupper():
            num_upper+=1
        else:
            num_lower+=1
    return "No. of Upper case characters : {} \nNo. of Lower case characters : {}".format(num_upper,num_lower)

tallyLetters('The quick Brow Fox')
