Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
O(1) as it takes constant time to add an element to the array

2. What is the space complexity of your ring buffer's `append` function?
O(1) as it only uses one space at most

3. What is the runtime complexity of your ring buffer's `get` method?
O(n) as I'm doing a for loop to n which is constant time

4. What is the space complexity of your ring buffer's `get` method?
O(n)

5. What is the runtime complexity of the provided code in `names.py`?
O(n^2) as there was a double for loop in the original code 

6. What is the space complexity of the provided code in `names.py`?
I think O(n/2) as in the worst case, each item would have a duplicate. This means I would need to store a list
of all duplicates. For e.g. If there weere 20,000 names. I would store 10,000.

7. What is the runtime complexity of your optimized code in `names.py`?
O(n) as my code uses a cache via a python dictionary. Incorportating a cache is efficient as it looks up values at O(1) time 
complexity. While the code visits n names, it checks whether or not a key already exists in the dictionary of all previously 
reviewd names in constant time or O(1)

8. What is the space complexity of your optimized code in `names.py`?
O(n)
