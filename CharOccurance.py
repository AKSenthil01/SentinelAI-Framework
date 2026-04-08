# def count_with_loop(input_string):
#     freq = {}
#     for char in input_string.casefold():
#         if char in freq:
#             freq[char] += 1
#         else:
#             freq[char] = 1
#     return freq
#
# print(count_with_loop("Hello Senthil Om Muruga"))
from datetime import datetime
from itertools import count

#Define the string
input_string="Hello Senthil Om Muruga!"
#Create an empty Dictionary
freq = {}
#Iterate through the string
for char in input_string.casefold():
    #If character is already in Dictionary then increment the count
    if char in freq:
        freq[char] += 1
    else:
        #If not then initialize with 1
        freq[char] = 1
#Print the result
print(freq)
#==================================
import string


def remove_punctuation(text):
    """
    Removes all standard punctuation from a given string.

    Args:
        text (str): The input string with potential punctuation.

    Returns:
        str: The string with all punctuation removed.
    """
    # Create a translation table that maps each punctuation character to None (deletion)
    translator = str.maketrans('', '', string.punctuation)

    # Use the translate method to remove the punctuation characters efficiently
    return text.translate(translator)


# Example usage
original_string = "Hello, World! Python is amazing, isn't it?"
cleaned_string = remove_punctuation(original_string)

print(f"Original string: {original_string}")
print(f"Cleaned string: {cleaned_string}")

str1="Senthilkumar"
print(str1[::-1]) #ramuklihtneS
print(str1[::-3]) #ruin
print(str1[1:]) #enthilkumar
print(str1[3:]) #thilkumar
print(str1[:3]) # Sen (Donot include the end index)
print(str1[1:10:2]) # etikm

a = [1,2,3,4,5,6,7,8]
print(a)
numbers = ','.join(str(i) for i in a)
print(numbers)

s = "String in PYTHON"
s1 = s.capitalize()
print(s1) #String in python
s1 = s.title()
print(s1) #String in python

a =[10,20,30,40,50]
print(a)
b = list(reversed(a))#[10, 20, 30, 40, 50]
print(b) #[50, 40, 30, 20, 10]

names = ["john", 'fan', "sam", "megha", "popoye", "tom", "jane", "james","tony"]
for i in names:
    if i.startswith("j"):
        print(i)

names = ['john', 'fan', 'sam', 'megha', 'popoye', 'tom', 'jane', 'james', 'tony']
jnames=[name for name in names if name[0] == 'j']     #One line code to filter names that start with ‘j’
print(jnames)

a = "this is a sample string with many characters"
print(len(set((a)))) #16

import random
print(random.random())

from random import shuffle
x = ['Keep', 'The', 'Blue', 'Flag', 'Flying', 'High']
shuffle(x)
print(x)

list = ["1", "4", "0", "6", "9"]
list = [int(i) for i in list] #[0, 1, 4, 6, 9]
list.sort() #['0', '1', '4', '6', '9']
print (list)

import time
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)
print(datetime.now())

list3=['e','f','g','h']
list4=[5,6,7,8]
#
# x=list(zip(list3,list4))
# print(x)

list1=[1,2,3,4]
list2=['a','b','c','d']
dict1=dict(zip(list1,list2))
print(dict1) #{1: 'a', 2: 'b', 3: 'c', 4: 'd'}

dict2={list1[i]:list2[i] for i in range(len(list1))}
print(dict2) #{1: 'a', 2: 'b', 3: 'c', 4: 'd'}

class A:
    count=0
    def __init__(self):
        A.count+=1
        print("class A is called")

a=A()
b=A()
print(A.count)#2


count2=0
class B:
    def __init__(self):
        global count2
        count2+=1
        print("class B is called")

b1=B()
b2=B()
b3=B()
print(count2) #3

#Duplicate Characters
list=['india','is','my','own','country']
str2=(''.join(list))
print(str2)
duplicates=[]
for char in str2:
    if str2.count(char)>1 and char not in duplicates:
        duplicates.append(char)
print(duplicates) #['i', 'n', 'y', 'o']
print(*duplicates) #i n y o

#Unique Characters
list=['india','is','my','own','country']
str3=''.join(list)
print(str3)            #indiaismyowncountry
unique=[]
for char in str3:
    if str3.count(char)==1 and char not in unique:
        unique.append(char)
print(unique) #['d', 'a', 's', 'm', 'w', 'c', 'u', 't', 'r']
print(*unique) #d a s m w c u t r

#MRO-Method Resolution Order

#print all words starting with i
list1=['india','is','my','own','country']
list2=[word for word in list1 if word.startswith("i")]
print(list2)

class Test:
    def method1(self):
        print("method 1 called")

    def method2(self):
        print("method 2 called")


#Write a program which will find all such numbers which are divisible by 7 but
#are not a multiple of 5, between 2000 and 3200 (both included).
l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))
        print(','.join(l))