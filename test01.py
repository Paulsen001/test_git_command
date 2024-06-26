def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# testtest
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(quick_sort(arr))
# test001
# test002
# test003
#  test004
# test005
