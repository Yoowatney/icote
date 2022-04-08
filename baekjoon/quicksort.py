a = [4, 5, 6, 1 ,2, 8, 3, 7]

def qsort(a):
    if len(a) <= 1:
        return a
    pivot = a.pop()
    left = [x for x in a if x < pivot]
    right = [x for x in a if x > pivot]
    return qsort(left) + [pivot] + qsort(right)

print(qsort(a))
