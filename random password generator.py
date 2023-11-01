import random
import string
def generatepassword(num):
   str1=""
   list1=string.ascii_letters+string.digits+string.punctuation
   for i in range(num):
       str1=str1+random.choice(list1)
   return str1

n=int(input())
password=generatepassword(n)
print(password)