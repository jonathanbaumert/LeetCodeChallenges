from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    length = len(nums)
    for i in range(0,length):
        for j in range(i+1,length):
            testVal = nums[i] + nums[j]
            if testVal == target:
                return [i,j]

    return 1





o = twoSum([2,7,11,15],22)
print(o)
