myset = set(["a", "b", "c"])
if "d"  in myset:
    print("not")

def removeDuplicates(arr):
    seen = set()
    idx = 0
    for i in range(len(arr)):
        if arr[i] not in seen:
            seen.add(arr[i]) #add to the set
            arr[idx] = arr[i] #update the arr values
            # print(seen)
            # print(arr)
            idx += 1
    # Return the size of the array 
    # with unique elements
    return idx

if __name__=="__main__":
    arr1 = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    newSize = removeDuplicates(arr1)
    print(removeDuplicates(arr1))

    for i in range(newSize):
        print(arr1[i], end=" ")