# 1.Calculator:
# def calculator(a,b,operators):
#     if operators =='+':
#         print("sum is:",a+b)
#     elif operators =='-':
#         print("difference is:",a-b)
#     elif operators =='*':
#         print('product is:',a*b)
#     elif operators =='/':
#         print('division is:',a/b)
#     else:
#         print('invalid operator')
# a =float(input('enter first number:'))     
# b =float(input('enter second number:'))
# operators=input('enter operators(+,-,*,/):')
# result = calculator(a, b, operators)
# print("Result:", result)

# 2.Palindrome Checker:
# def palindrome(s):
#     s = s.lower()  
#     return s == s[::-1]  
# text = input("Enter a string to check if it's a palindrome: ")
# if palindrome(text):
#     print(f'"{text}" is a palindrome.')     
# else:
#     print(f'"{text}" is not a palindrome.')

# 3.Number Guessing Game:
# import random
# number =random.randint(1,10)
# guess=int(input("Guess a number between 1 and 10: "))
# if number ==guess:
#     print("correct🎉")
# else:
#     print("wrong number😥")

# 4.counting vowels in a string:
# def count_vowels(string):
#     vowels='aeiouAEIOU'
#     count=0
#     for char in string:
#         if char in vowels:
#             count +=1
#     return count
# text =input("Enter a string to count vowels: ")
# print("number of vowels", count_vowels(text))

# 5.email validator:
def valid_email(email):
    return '@' in email and '.' in email.split('@')[-1]
email =input("enter email:")
if valid_email(email):
    print("valid email✅")
else:
    print("invalid email❌")
