def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        mergesort(left)
        mergesort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1
def printList(arr):
    for i in range(len(arr)):
        print((arr[i]), end=" ")
    print()  

arr = [7,3,5,8,2,9,4,15,6]
print('Array : ' + str(arr))
mergesort(arr)
printList(arr)
 
#time complexity: O(nlog(n))