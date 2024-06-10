#Given an array/list 'ARR' of integers and a position ‘M’. You have to reverse the array after that position.Example:We have an array ARR = {1, 2, 3, 4, 5, 6} and M = 3 , considering 0 based indexing so the subarray {5, 6} will be reversed and our output array will be {1, 2, 3, 4, 6, 5}.

def reverseArray(arr, m):
    
    n = len(arr)
    
    brr = []
    
    #Initialize array brr with 0 values
    for i in range(len(arr)):
        brr.append(0)  
   
    p = 0
    
    # First fill the brr in the same order as the original array upto Mth postion.
    for i in range(m + 1):
        brr[p] = arr[i]
        p += 1

        
    # Now fill the brr in the reverse order till (m+1)th postion.
    for j in range(n - 1, m, -1):
        brr[p] = arr[j]
        p += 1
        
    # Now copy back the array brr into array arr.
    for i in range(n):
        arr[i] = brr[i]
        
    return arr
a= [1,2,3,4,5,6]
print(reverseArray(a,3))