def twoSum(arr, target):
    # code here
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] == target:
                return True
    return False

arr1=[1,2,3,4,-5]
target1=7
print(twoSum(arr1,target1))

#faster
def twoSum(arr, target):
    # code here
# Create a set to store the elements
    s = set()

    # Iterate through each element in the array
    for num in arr:
        
        # Calculate the complement that added to
        # num, equals the target
        complement = target - num

        # Check if the complement exists in the set
        if complement in s:
            return True

        # Add the current element to the set
        s.add(num)

    # If no pair is found
    return False