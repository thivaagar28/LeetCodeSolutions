class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow,fast=0,1
        sz=len(nums)
        while fast < sz:
            if nums[fast] != nums[slow]:
                slow+=1
                nums[slow] = nums[fast]
            fast+=1

        return slow+1

        """
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1 #move from original position
                nums[slow] = nums[fast]
            fast += 1
        
        return slow+1
        """