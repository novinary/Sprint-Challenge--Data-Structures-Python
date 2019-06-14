import time
from collections import defaultdict

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

join_names = names_1 + names_2
cache = defaultdict(int)
duplicates = []

for name in names_1:
    cache[name] += 1
for name in names_2:
    if cache[name]:
        duplicates.append(name)

      
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

