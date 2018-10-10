import math

def BinarySearch(key, arr, size):
    low = 0
    high = size - 1
    while(True):
        index = math.floor((low + high)/2) 
        if( key < arr[index] ):
            high = index - 1
        else:
            low = index + 1    
        if( low > high or key==arr[index]):
            break
    return(low <= high)

arr  = (2,3,5,7,9,11)
key  = 5
size = 6

print(BinarySearch(key, arr, size))

#Output:
#True
