arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

def findPlatform(arr, dep):
    plat_needed = 1
    result = 1
    n = len(arr) #6
    for i in range(n): #0,1,2,3,4,5
        plat_needed = 1
        for j in range(n): #0,1,2,3,4,5
            if i != j:
                if (arr[i] >= arr[j] and dep[j] >= arr[i]):
                    plat_needed += 1
        result = max(result, plat_needed)

    return result
print(findPlatform(arr, dep))