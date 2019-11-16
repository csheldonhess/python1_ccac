import random

with open('numbers.txt', 'w') as num_file:
    for whatever in range(0,500):
        num_file.write(str(random.randint(0,100)) + "\n")