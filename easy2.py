# Print words
import time
import random

print_words = input("yo whats up ")

random_word= ["hello", "hi", "hey", "yo", "sup"]

for i in range(1000):
    print(random.choice(random_word))
    time.sleep(1)