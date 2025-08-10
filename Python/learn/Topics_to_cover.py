#PYTHON

#* topic completed

"""
output
variabls
input
If/else
loops (for, while)
nested conditions
List
Tuple
Set
Dictionary
Functions
CLASS
"""

#* current TOPIC HAShing

# Input: arr[] = {10,5,10,15,10,5};
# o/p
#10 3
#5 2
#15 1
def merge_sort(arr,low,high):
    if low >= high:
        return
    
    mid = (low+high)//2
    
    merge_sort(arr,low,mid) #left
    merge_sort(arr,mid+1,high) #right
    merge(arr,low,mid,high)

def merge(arr,low,mid,high):
    left = arr[low:mid+1]
    right = arr[mid+1:high+1]

    i= j = 0
    k = low

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
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

num = [3,2,4,1,3]
merge_sort(num,0,len(num)-1)
print(num)