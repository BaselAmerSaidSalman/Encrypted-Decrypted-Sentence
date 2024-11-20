import string
import time

def encrypted(word, shift):
  small_alphabet = string.ascii_lowercase
  big_alphabet = string.ascii_uppercase
  encrypted_word = ""
  for i in word:
    if i in small_alphabet:
      word_index = small_alphabet.index(i)
      new_position = (word_index + keyword) % 26
      encrypted_word += small_alphabet[new_position]
    elif i in big_alphabet:
      word_index = big_alphabet.index(i)
      new_position = (word_index + keyword) % 26
      encrypted_word += big_alphabet[new_position]
    else:
      encrypted_word += i
  print(f"Your encrypted word is: {encrypted_word}")
  time.sleep(2)
  
def encrypted_solution(word, shift):
  small_alphabet = string.ascii_lowercase
  big_alphabet = string.ascii_uppercase
  encrypted_word = ""
  for i in word:
    if i in small_alphabet:
      word_index = small_alphabet.index(i)
      new_position = (word_index - keyword) % 26
      encrypted_word += small_alphabet[new_position]
    elif i in big_alphabet:
      word_index = big_alphabet.index(i)
      new_position = (word_index - keyword) % 26
      encrypted_word += big_alphabet[new_position]
    else:
      encrypted_word += i
  print(f"Your encrypted word is: {encrypted_word}")
  time.sleep(2)


user_want = input("Do you want to encrypt or decrypt? ").lower()
while user_want != "encrypt" and user_want != "decrypt":
  print("Sorry, Invalid input")
  user_want = input("Do you want to encrypt or decrypt? ").lower()
if user_want == "encrypt":
  sentence = input("Please enter a sentence: ")
  keyword = int(input("Please enter a encrypted keyword: "))
  encrypted(sentence, keyword)
else:
  sentence = input("Please enter a sentence: ")
  keyword = int(input("Please enter a encrypted keyword: "))
  encrypted_solution(sentence, keyword)