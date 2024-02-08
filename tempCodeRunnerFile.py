def Capitalize(string):
      words = string.split()
      for word in words:
            words[words.index(word)] = word.Capitalize()
            return" ".join(words)
while True:
      string = str(input("Enter a string: "))
      Capitalize (string)