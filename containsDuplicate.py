# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

class Solution:
    def containsDuplicate(self,nums):
        try:
            hashset = set()
            for i in nums:
                if i in hashset:
                    return True
                hashset.add(i)
            return False
        except Exception as e:
            print(e)

nums = [1,2,3,1]
P = Solution()
Q = P.containsDuplicate(nums)
print(Q)
