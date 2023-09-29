# 1. Write a program to find the transpose of a matrix.

 
# N = 4
 
# def transpose(A,B):
 
#  for i in range(N):
#   for j in range(N):
#    B[i][j] = A[j][i]

# A = [ [1, 1, 1, 1],
#  [2, 2, 2, 2],
#  [3, 3, 3, 3],
#  [4, 4, 4, 4]]

# B = A[:][:] 
 
# transpose(A, B)
 
# print("Result matrix is")
# for i in range(N):
#  for j in range(N):
#   print(B[i][j], " ", end='')
#  print() 


# 2. Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

# sentence = "MY PYTHON"
# capitalized_string = sentence.capitalize()
# print(capitalized_string)


# 3. Write a program to implement all built-in methods of list.

# List Methods in Python


# S.no	  Method                                 Description
# 1	      append()	     Used for appending and adding elements to the end of the List. 
# 2	       copy()	     It returns a shallow copy of a list
# 3	      clear()	     This method is used for removing all items from the list. 
# 4	      count()	     These methods count the elements
# 5	     extend()	     Adds each element of the iterable to the end of the List
# 6	      index()	     Returns the lowest index where the element appears. 
# 7	     insert()	     Inserts a given element at a given index in a list. 
# 8	        pop()	     Removes and returns the last value from the List or the given index value.
# 9	     remove()     	 Removes a given object from the List. 
# 10    reverse()	     Reverses objects of the List in place.
# 11	    sort()	     Sort a List in ascending, descending, or user-defined order
# 12	      min()	     Calculates the minimum of all the elements of the List
# 13	      max()	     Calculates the maximum of all the elements of the List



# 4. Write a program to read dictionary values through keyboard and merge two 


# dict_1 = {1: 'a', 2: 'b'}
# dict_2 = {2: 'c', 4: 'd'}

# print(dict_1 | dict_2)

# 5.Write a program to demonstrate all built-in methods of dictionary.

                #   Python Dictionary Methods

# Functions Name                                Descriptions

# clear()                              Removes all items from the dictionary

# copy()                                 Returns a shallow copy of the dictionary

# fromkeys()                                Creates a dictionary from the given sequence
# get()                                   Returns the value for the given key

# items()                                   Return the list with all dictionary keys with values

# keys()                                       Returns a view object that displays a list of all the keys in the dictionary in order of insertion

# pop()                                         Returns and removes the element with the given key

# popitem()                                       Returns and removes the key-value pair from the dictionary

# setdefault()                                    Returns the value of a key if the key is in the dictionary else inserts the key with a value to the dictionary

# values                                         Updates the dictionary with the elements from another dictionary

# update()                                        returns a list of all the values available in a given dictionary

# 6. Write a program to find the sum of all the elements in a list.

# Python program to find sum of elements in list
 
# total = 0
# list1 = [11, 5, 17, 18, 23]

# for ele in range(0, len(list1)):
#     total = total + list1[ele]

# print("Sum of all elements in given list: ", total)

# 7. With a given integral number n, write a program to generate a dictionary that contains(i,i*i) such that i is an integral number between 1 and n. And then the program should print the dictionary.

# number = int(input("Type a number: "))

# numberDict = {}
# for i in range(1, number+1):
#     numberDict[i] = i*i
# print(numberDict)

# 8. Write a program that accepts a sentence and calculate the number of letters & digits

# num = 3452
# count = 0

# while num != 0:
#     num //= 10
#     count += 1

# print("Number of digits: " + str(count))


# 9. Write a program to implement filter(), map() and reduce() 

	
# def newfunc(a):
#     return a*a
# x = map(newfunc, (1,2,3,4)) 
# print(x)
# print(set(x))


# 10. Write a program to implement List Comprehension .

# numbers = [1, 2, 3, 4, 5]
# squared = [x ** 2 for x in numbers]
# print(squared)

# 11. Write a program to implement Dictionary Comprehension

# square_dict = {num: num*num for num in range(1, 11)}
# print(square_dict)

# 12. Write a program to find the largest and smallest element from a list.
# mylist = []
# number = int(input('How many elements to put in List: '))
# for n in range(number):
#     element = int(input('Enter element '))
#     mylist.append(element)
# print("Maximum element in the list is :", max(mylist))
# print("Minimum element in the list is :", min(mylist))

# 13. Write a Python program to print the numbers of a specified list after removing even numbers from it

# list = [11, 22, 33, 44, 55]
# print("Original list:")
# print(list)
# for i in list:
#     if i % 2 == 0:
#         list.remove(i)
# print("List after removing EVEN numbers:")
# print(list)

# 14. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30


# l = list()
# for i in range(11,25):
# 	l.append(i**2)
# print(l[:5])
# print(l[-5:])

# 15. Write a Python program to insert a given string at the beginning of all items in a li

# lst = ['Foo', 'fOO', 'geeKs']
# lst = [i.lower() for a,i in enumerate(lst)]
# print(lst)

