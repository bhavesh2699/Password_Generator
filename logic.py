from random import choice
import random
ASCII=[random.randrange(48, 57, 1),random.randrange(97, 122, 1),random.randrange(64, 90, 1)]
value=input("Enter Password\n")
value_altered = ''.join(chr(choice(ASCII)) for letter in value)
print(value_altered)
