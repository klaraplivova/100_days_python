#Step 1 random select and check input number for match
word_list = ["aardvark", "baboon", "camel"]
import random
ran_word = random.choice(word_list)
player = input("_"*len(ran_word)+"\nChoose a letter:")
for ch in ran_word:
  if ch == player:
    print("True")
  else:
    print("False")
