
import sys

name = input("enter text : ")

def count_letters(name):
     count = 0
     
     for ch in name:
         if ("A" <= ch <= "Z" or "a" <= ch <= "z"):
                count += 1
     return count

wordscount = count_letters(name)

print(wordscount)