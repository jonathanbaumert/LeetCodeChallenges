from typing import List

def twoSumsTwoPass(nums: List[int], target:  int):
# This solution is my attempt to recreate the dual pass hash table
# solution provided in Java in LeetCode, but in python
    numDict = dict()
    length = len(nums)

    # create the table
    for i in range(0,length):
        numDict[nums[i]] = i
    
    # find the pair
    for i in range(0,length):
        secondNum = target - nums[i]
        secondIndex = numDict.get(secondNum)
        if secondIndex != None and secondIndex != i:
            return [i, secondIndex]

def twoSumsOnePass(nums: List[int], target:  int):
# This solution is my attempt to recreate the one pass hash table
# solution provided in Java in LeetCode, but in python
    numDict = dict()
    length = len(nums)
    
    # find the pair
    for i in range(0,length):
        secondNum = target - nums[i]
        secondIndex = numDict.get(secondNum)
        if secondIndex != None and secondIndex != i:
            return [i, secondIndex]
        numDict[nums[i]] = i

print(twoSumsTwoPass([3,2,4],6))