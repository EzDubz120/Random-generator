import random
import time
import string

#text = open("dictionary.txt", "r").read()
#text_2 = open("simple dictionary.txt", "r").read()

# open file
with open("dictionary.txt", "r") as file:
    data = file.read()
    words = data.split()
      
    # Generating a random number for word position
    word_pos = random.randint(0, len(words)-1)
    print("Position:", word_pos)
    print("Word at position:", words[word_pos])

string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'
string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print("Welcome to this random generating app, we can generate numbers, letters and words")
time.sleep(0.5)

selection = input("What would you like to generate: numbers, letters or words ")

if selection == "number":
    range_l = int(input("Enter the lowest the number can be "))
    range_h = int(input("Enter the maxiumum value the number can be "))
    number = random.randint(range_l, range_h)
    print("Generating number")
    time.sleep(1)
    print("Your number is", number)
elif selection == "numbers":
    range_l = int(input("Enter the lowest the number can be "))
    range_h = int(input("Enter the maxiumum value the number can be "))
    number = random.randint(range_l, range_h)
    print("Generating number")
    time.sleep(1)
    print("Your number is", number)

if selection == "letters":
    uppercase_or_lowercase = input("Would you like the letter to be uppercase or lowercase ")

if selection == "letters" and uppercase_or_lowercase == "lowercase":
    letter = random.choice(string.ascii_lowercase)
    print("Your random letter is", letter)

if selection == "letters" and uppercase_or_lowercase == "uppercase":
    letter = random.choice(string.ascii_uppercase)
    print("Your random letter is", letter)

if selection == "words":
    simple_or_not = input("Would you like a word from the simple dictionary ")

if selection == "words" and simple_or_not == "no":
    word_pos = random.randint(0, len(words)-1)
    print("Your word is:", words[word_pos])

if selection == "words" and simple_or_not == "yes":
    with open("simple dictionary.txt", "r") as file:
        data = file.read()
        words = data.split()
    word_pos = random.randint(0, len(words)-1)
    print("Position:", word_pos)
    print("Word at position:", words[word_pos])

#if you have a very slow machine then it MIGHT take a while to load in the whole dictionary file however it shouldn't crash it