'''
Question 2: Fibonacci Sequence
Write a program to generate the Fibonacci sequence up to 100.
'''
def sequence ():
      secondnumb = 0
      firstnumb = 1
      while firstnumb + secondnumb <=100:
            currentterm = firstnumb + secondnumb
            print(currentterm, )
            secondnumb = firstnumb
            firstnumb = currentterm
sequence()
