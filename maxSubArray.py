# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# A subarray is a contiguous part of an array.
# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

class Solution:
    def maxSubArray(self,nums):
        try:
            maxSub = nums[0]
            curSum = 0

            for i in nums:
                if curSum < 0:
                    curSum = 0
                curSum += i
                maxSub = max(maxSub, curSum)
            return maxSub
        except Exception as e:
            print(e)

nums = [-2,1,-3,4,-1,2,1,-5,4]
P = Solution()
Q = P.maxSubArray(nums)
print(Q)
