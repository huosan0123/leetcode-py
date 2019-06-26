
def merge(vec, vec1, low, mid, high):
    for i in range(low, high+1):
        vec1[i] = vec[i]
    i, j = low, mid+1
    k = low
    while i <= mid and j <= high:
        if vec1[i] < vec1[j]:
            vec[k] = vec1[i]
            i += 1
        else:
            vec[k] = vec1[j]
            j += 1
        k += 1
    while i <= mid:
        vec[k] = vec1[i]
        i += 1
        k += 1
    while j <= high:
        vec[k] = vec1[j]
        j += 1
        k += 1

def mergeSort(nums, copy, low, high):
    if low < high:
        mid = (high + low) // 2
        mergeSort(nums, copy, low, mid)
        mergeSort(nums, copy, mid+1, high)
        merge(nums, copy, low, mid, high)

a = [3,6,5,4,1,9,0]
b = [0] * len(a)
mergeSort(a, b, 0, len(a)-1)
print(a)
