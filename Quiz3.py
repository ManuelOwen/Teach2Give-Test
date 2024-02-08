'''
Question 3: Power of Two
Write a program that takes an integer as input and returns true if the input is a power of two.

Examples:
8=> returns true
6=> returns false
'''
import math
def power(number):
      if number <=0: 

           

            return False
      elif math.log2(number).is_integer():
            
            return True
      else:
           

            return False
      
number = input("enter number:")
intnumber = int(number)
power(intnumber)


      
