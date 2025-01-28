class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left, right, total = 0, 0, 0
        length = len(nums)+1

        for right in range(0, len(nums), 1):
            #finding intial sliding window and back calculation
            total += nums[right]

            while total >= target:
                length = min(length, right-left+1)
                #sliding window front calculation
                total -= nums[left]
                #removed previous left and point to new left which already exist in sliding window
                left += 1
                

        return length if length <= len(nums) else 0