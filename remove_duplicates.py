def remove_duplicates(arr):
    uniq = []
    for num in arr:
        if num not in uniq:
            uniq.append(num)
    return uniq
    
a=[1,3,2,3,2,5,4,7,7]
print(remove_duplicates(a))