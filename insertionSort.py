def instertionSort(arr):
    for i in range(1,len(arr)): 
        print(str(i) + ".adım -----")   
        key = arr[i] 
        j=i-1 
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j] 
            j-=1
        arr[j+1] = key
        for i in range (len(arr)):
            print("%d" %arr[i])
     
    


arr = [7,3,5,8,2,9,4,15,6]
instertionSort(arr)
print("Instertion sort : ")
for i in range (len(arr)):
    print("% d" %arr[i])
