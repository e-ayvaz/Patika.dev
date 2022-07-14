def insertion(arr):
    for i in range(1,len(arr)):
        key = arr[i] # right element
        j = i-1 # left element
        while j>=0 and arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            j -= 1
        arr[j+1] = key
    return arr
arr=[5,1,8,3,6,0,9,4,2]
print(insertion(arr))
