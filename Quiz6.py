'''
Question 6: Count Vowels
Write a program that counts the number of vowels in a sentence.

eg " Hello World " => returns 2
'''
def Count(sentence):
      vowels ="aeiouAEIOU"
      count = 0
      repeated_vowels  = set()

      for char in sentence:
            if char in vowels and char not in repeated_vowels:
                  count += 1
                  repeated_vowels.add(char)


      return count
while True:
      sentence = str(input("Write a sentence: "))
      Count(sentence)