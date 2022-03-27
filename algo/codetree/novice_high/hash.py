from copy import deepcopy
from collections import Counter
arr = [17, 26, 32, 5, 11, 12, 6, 8, 9]

def hash_function(a, b):
    n = len(arr)
    ret = deepcopy(arr)
    for i in range(n):
        ret[i] = (ret[i] * a + b) % 10
    return ret

print(Counter(hash_function(6, 2)))
print(Counter(hash_function(5, 5)))
print(Counter(hash_function(4, 8)))
print(Counter(hash_function(3, 1)))
print(Counter(hash_function(2, 11)))


