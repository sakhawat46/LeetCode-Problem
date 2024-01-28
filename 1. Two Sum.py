# print("Bismillah")
# print("Allahu Akbar")

nums = [2, 7, 11, 15]
target = 9


# for i in range(len(nums)-1):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 print([i, j])



seen = {}
for i, num in enumerate(nums):
    # print(i, num)
    if target - num in seen:
        print([seen[target-num], i])
    elif num not in seen:
        seen[num] = i
        print(seen)