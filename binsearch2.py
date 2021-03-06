import random

def binary_search(arr, start, end, target):
    i = 1
    while start <= end:
        mid = start + (end - start) // 2; 
          
        if arr[mid] == target: 
            return mid, i
        elif arr[mid] < target:
            start = mid + 1 
        else: 
            end = mid - 1
        i = i + 1
  
    # Not found
    return -1, i-1

arr = random.sample(range(10000000), k=1000000)
arr.sort()
target = arr[1000]
  
result, i = binary_search(arr, 0, len(arr)-1, target) 
  
if result != -1: 
    print(f"{target} found at {result} in {i} iterations")
else: 
    print(f"{target} not found after {i} iterations")
