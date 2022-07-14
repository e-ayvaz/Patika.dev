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
 
#time complexity: O(nlog(n))

def merge(Arr,p,q,r):
    nL= q-p+1
    nR= r-q
    L= [0]*(nL+1)
    R= [0]*(nR+1)
    for i in range(nL):
        L[i]=Arr[p+i]
    for j in range(nR):
        R[j]=Arr[q+j+1]
    i=0
    j=0
    k=p
    while i<nL and j<nR:
        if L[i]<=R[j]:
            Arr[k]=L[i]
            i+=1
        else:
            Arr[k]=R[j]
            j+=1
        k+=1
    while i<nL:
        Arr[k]=L[i]
        i+=1
        k+=1
    while j<nR:
        Arr[k]=R[j]
        j+=1
        k+=1
arr = [7,3,5,8,2,9,4,15,6]
def mergePR(Arr,p,r):
    if p<r:
        q= (p+r)//2
        mergePR(Arr,p,q)
        mergePR(Arr,q+1,r)
        merge(Arr,p,q,r)
arr = [7,3,5,8,2,9,4,15,6]
mergePR(arr,0,len(arr)-1)
printList(arr)

