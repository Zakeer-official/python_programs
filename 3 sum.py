from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final = []
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    result = []
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append(nums[i])
                        result.append(nums[j])
                        result.append(nums[k])
                    if not len(result) == 0:
                        if result not in final:
                            final.append(result)
        return final


#Example:

nums = [-1,0,1,2,-1,-4] #Output: [[-1,-1,2],[-1,0,1]]
x = Solution()
print(x.threeSum(nums)) # It is a leetcode sum which pases 308/313 testcases beacuse of time limit exceeds . It takes O(n^3) complexity..so, we can optimize it without using much loops.


'''
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
'''
