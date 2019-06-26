
def partition(vec, low, high):
    i, j = low, high
    pivot = vec[low]
    while i < j:
        while i < j and vec[j] >= pivot:
            j -= 1
        vec[i] = vec[j]

        while i < j and vec[i] <= vec[j]:
            i += 1
        vec[j] = vec[i]
    vec[i] = pivot
    return i

def quickSort(nums, low, high):
    if low < high:
        pivot = partition(nums, low, high)
        print(pivot, low, high, nums)
        quickSort(nums, low, pivot-1)
        quickSort(nums, pivot + 1, high)

a = [3,4, 7, 1, 2, 9, 8]
quickSort(a, 0, len(a)-1)
print(a)
