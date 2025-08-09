# # 1.Calculator:
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

# # 2.Palindrome Checker:
# def palindrome(s):
#     s = s.lower()  
#     return s == s[::-1]  
# text = input("Enter a string to check if it's a palindrome: ")
# if palindrome(text):
#     print(f'"{text}" is a palindrome.')     
# else:
#     print(f'"{text}" is not a palindrome.')

# # 3.Number Guessing Game:
# import random
# number =random.randint(1,10)
# guess=int(input("Guess a number between 1 and 10: "))
# if number ==guess:
#     print("correct🎉")
# else:
#     print("wrong number😥")

# # 4.counting vowels in a string:
# def count_vowels(string):
#     vowels='aeiouAEIOU'
#     count=0
#     for char in string:
#         if char in vowels:
#             count +=1
#     return count
# text =input("Enter a string to count vowels: ")
# print("number of vowels", count_vowels(text))

# # 5.email validator:
# def valid_email(email):
#     return '@' in email and '.' in email.split('@')[-1]
# email =input("enter email:")
# if valid_email(email):
#     print("valid email✅")
# else:
#     print("invalid email❌")

# sentence = input("Enter a sentence: ")
# words = sentence.split()
# print(f"Total words: {len(words)}")

# # 6. Prime Number Checker:
# num =int(input("Enter a number: "))
# if num > 1:
#     for i in range(2,num):
#         if num % i ==0:
#             print(f"{num}is not a prime number")
#             break
#     else:
#         print(f"{num} is a prime number")
# else:
#     print("must be grater than 1")

# # 7.Swapping:
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# print("Before swapping: a =", a, ", b =", b)
# a,b=b,a
# print("After swapping: a =", a, ", b =", b)

# # 8. Fibonacci Sequence:
# n=int(input("Enter the number: "))
# a,b=0,1
# for i in range(n):
#     print(a, end=' ')
#     a, b = b, a + b

# # 9.odd or even:
# num =int(input("Enter a number: "))
# if num % 2==0:
#     print(f"{num} is a even number")
# else:
#     print(f"{num} is a odd number")

# # 10.reverse a string:
# text=input("Enter string:")
# reversed_text =text[::-1]
# print("Reversed string:", reversed_text)

# print("Thank you")

# # 11.Multiplication Table:
# n=int(input("Enter a number: "))
# # def multiplication_table(n):
# for i in range(1, 11):
#     print(f"{n} x {i} = {n * i}")
# # multiplication_table(n)

# # 12.Leap year:
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

# # 13.To do List:
# tasks = []
# while True:
#     choice = input("1.Add 2.View 3.Exit: ")
#     if choice == '1':
#         tasks.append(input("Enter task: "))
#     elif choice == '2':
#         print("Tasks:")
#         for i, task in enumerate(tasks, 1):
#             print(i, task)
#     elif choice == '3':
#         break
#     else:
#         print("Invalid choice")

# # 14.simple interest:
# def simple_interest(principal, rate, time): 
#     return (principal * rate * time) / 100
# principal = float(input("Enter principal amount: "))
# rate = float(input("Enter rate of interest: "))
# time = float(input("Enter time in years: "))
# interest = simple_interest(principal, rate, time)
# print(f"Simple Interest: {interest}")

# # 15.Area of Circle:
# import math
# def area_of_circle(radius):
#     return math.pi * radius ** 2
# radius = float(input("Enter the radius of the circle: "))
# area = area_of_circle(radius)  
# print(f"Area of the circle: {area:.2f}")  # Display area rounded to 2 decimal places 

# 16.Word frequency counter:
# text=input("enter text:") .lower()
# words=text.split()
# word_count={}
# for word in words:
#     word_count[word] = word_count.get(word, 0) + 1
# print("Word count:", word_count)

# 17.Average of list of numbers:
# nums =list(map(float,input("enter numbers separated by space:").split()))
# print("average:",sum(nums)/len(nums))

# 18.Armstrong Number Checker:
# num = int(input("Enter a number: "))
# order = len(str(num))  # Number of digits
# total = sum(int(digit) ** order for digit in str(num))

# if num == total:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")

# start=int(input("Enter start of range: "))
# end=int(input("Enter end of range: "))
# for num in range(start, end + 1):
#     order = len(str(num))  # Number of digits
#     total = sum(int(digit) ** order for digit in str(num))
#     if num == total:
#         print(num)

# 19.sum of digits:
# def sum_of_digits(n):
#     total = 0
#     while n > 0:
#         total += n % 10
#         n //= 10
#     return total
# n = int(input("Enter a number: "))
# result = sum_of_digits(n)   
# print(f"Sum of digits: {result}")

# 20.
print("Welcome to the Python Program🎉")







