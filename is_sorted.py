def is_sorted(arr):
    for i in range(0,len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

a = [1,2,3,4,5,4]
print(is_sorted(a))