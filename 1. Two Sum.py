# print("Bismillah")
# print("Allahu Akbar")

nums = [2, 7, 11, 15]
target = 9



# Method 1:

for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                #  return([i, j])
                print([i, j])




# Method 2:

seen = {}
for i, num in enumerate(nums):
    if target - num in seen:
        print([seen[target-num], i])
    elif num not in seen:
        seen[num] = i
        # return(seen)
        print(seen)