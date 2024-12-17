arr = [2, 3, 1, 2, 3]
arr2 = [2]
arr3 = [2,2,1,0,9,2,5,9,8]
#expected output [2,3]

def findDuplicates(arr):
    arr.sort()
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    result = []
    for key, value in freq.items():
        if value > 1:
            result.append(key)
    return result

print(findDuplicates(arr3))