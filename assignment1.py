# 1.Write a program to check whether the entered number is postive or negative
# num=int (input("enter the number"))
# if num==0:
#     print("zero")
# elif num>0:
#         print("number is positive")
# else:
#         print("number is negative")


# 2.Write a program to  swap two variables

# a= int (input ("enter the first number"))
# b= int (input ("enter the second number"))
# c=a
# a=b
# b=c
# print("the value of the first variable after swapping is:",a)
# print("the value of the second variable after swapping is:",b)

# 3.Write a program to  Determine If Year Is Leap Year

# year=int (input("enter the year:"))
# if(year % 4)==0:
#     if(year%100)==0:
#         if(year % 400)==0:
#             print("the given year is a leap year")
#         else:
#                 print("it is a not leap year")
#     else:
#             print("it is a not a leap year")
# else:
#                         print("it is a not a leap year")



# 4.Write a program check whether the given number is odd or even

# num = int(input("Enter a number: "))

# if (num % 2) == 0:
#    print("{0} is Even".format(num))
# else:
#    print("{0} is Odd".format(num))

# Write a program to print the fibonocci series

# num = 10
# n1, n2 = 0, 1
# print("Fibonacci Series:", n1, n2, end=" ")
# for i in range(2, num):
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3
#     print(n3, end=" ")

# print()

# 6.Write a program to  generate following pyramid or triangle like  given below using for loop
# rows = int(input("Enter number of rows: "))

# for i in range(rows, 0, -1):
#     for j in range(0, i):
#         print("* ", end=" ")
    
#     print("\n")


# B

# 7. Write a program to print the prime numbers between given interval


# lower = 900
# upper = 1000

# print("Prime numbers between", lower, "and", upper, "are:")

# for num in range(lower, upper + 1):
#    # all prime numbers are greater than 1
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)

# 8. Write a program for Printing Odd numbers between 1 and 50 and calculate the sum of that numbers

# start = 1
# end = 50
 
# if start % 2 != 0:
 
#     for num in range(start, end + 1, 2):
#         print(num, end=" ")
# else:
 
#     for num in range(start+1, end + 1, 2):
#         print(num, end=" ")


# 9. Write a program to find the factorial of the given number.

# num = 7

# factorial = 1


# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print("The factorial of",num,"is",factorial)

# 10.Write a program to Check if the given string  is Palindrome or not.

# def isPalindrome(str):
 
    
#     for i in range(0, int(len(str)/2)):
#         if str[i] != str[len(str)-i-1]:
#             return False
#     return True

# s = "malayalam"
# ans = isPalindrome(s)
 
# if (ans):
#     print("Yes")
# else:
#     print("No")


# 11. Write a program to find sum of all integers greater than 100 and less than 200 that are divisible by 7.

# start_num = int(100)

# end_num = int(200)
 

# cnt = start_num
 

# while cnt <= end_num:
   
    
#     if cnt % 7 == 0 and cnt % 5 == 0:
#         print(cnt, " is divisible by 7.")
         
    
#     cnt += 1


# 12.Write a program to Display Multiplication Table

# num = 5

# for i in range(1, 11):
#    print(num, 'x', i, '=', num*i)



# 13. Write a program to calculate the area and perimeter of a rectangle..

 
# l=int(input("Length : "))
# w=int(input("Width : "))
# area=l*w
# perimeter=2*(l+w)
# print("Area of Rectangle : ",area)
# print("Perimeter of Rectangle : ",perimeter)

# 14. Write a program to find the sum of n' Natural Numbers

# num = 12

# if num < 0:
#    print("Enter a positive number")
# else:
#    sum = 0
   
#    while(num > 0):
#        sum += num
#        num -= 1
#    print("The sum is", sum)


# 15.Write a program to find whether given no. is Armstrong or not.

# n = int(input("Enter a number: "))

# s = 0
# t = n

# while t > 0:

#    digit = t % 10

#    s += digit ** 3

#    t //= 10

# if n == s:

#    print(n,"is an Armstrong number")

# else:

#    print(n,"is not an Armstrong number")

# 16. Write a program to find the largest among 3 numbers.

# num1 = 10
# num2 = 14
# num3 = 12

# if (num1 >= num2) and (num1 >= num3):
#    largest = num1
# elif (num2 >= num1) and (num2 >= num3):
#    largest = num2
# else:
#    largest = num3

# print("The largest number is", largest)

# 17. Write a program to remove all punctuations from given string.

# punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# my_str = "Hello!!!, he said ---and went."
# no_punct = ""
# for char in my_str:
#    if char not in punctuations:
#        no_punct = no_punct + char
# print(no_punct)

# 18. Write a program to  Display Triangle as follow :

# 1

# 2 2

# 3 3 3

# 4 4 4 4...

# rows = int(input("Enter number of rows: "))

# for i in range(rows):
#     for j in range(i+1):
#         print(j+1, end=" ")
#     print("\n")


# 19. Write a program to count the no:of each vowel in a given string.


# def vowel_count(str):
#     count = 0
#     vowel = set("aeiouAEIOU")
#     for alphabet in str:
#         if alphabet in vowel:
#             count = count + 1
     
#     print("No. of vowels :", count)
# str = "GeeksforGeeks"
# vowel_count(str)



# 20. Program to perform Addition,Subtraction,Multiplication and division on Complex-No's

# print("Enter First Number: ")
# numOne = int(input())
# print("Enter Second Number: ")
# numTwo = int(input())
# res = numOne+numTwo
# print("\nAddition Result = ", res)
# res = numOne-numTwo
# print("Subtraction Result = ", res)
# res = numOne*numTwo
# print("Multiplication Result = ", res)
# res = numOne/numTwo
# print("Division Result = ", res)

# 21. Find Value of the following expressions

# num_1 = 10

# num_2 = 11

 

# num_1 % num_2

# num_1 - num_2

# num_1 * num_2

# print('The sum is %.1f' %(float(input('Enter first number: ')) + float(input('Enter second number: '))))


# 22. Find the results of the following expressions (True or False)

num_1=7

num_2 = 6

 

num_1 < num_2

num_1 > num_2

num_1 <= num_2

num_1 >= num_2

num_1=num_2


# 23. Find the results of the following expressions (True or False)

num_1=3

num_2 = 4