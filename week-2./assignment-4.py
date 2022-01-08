def twoSum(nums, target):
    for i in nums:
        for j in nums:
            if i!=j and i+j==target:
                return [nums.index(i), nums.index(j)]


result=twoSum([2,11,7,15],9)
print(result)