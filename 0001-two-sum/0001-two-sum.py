class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #store diff: index
        needed = {}
        for i in range(0, len(nums), 1):
            diff = target - nums[i]
            if diff in needed:
                return [needed[diff], i]
            else:
                needed[nums[i]] = i