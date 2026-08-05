class Solution:
    def findMissingElements(self, nums):
        nums.sort()
        ans = []

        for i in range(nums[0], nums[-1] + 1):
            if i not in nums:
                ans.append(i)

        return ans