class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        fast = 1
        count = 1

        while fast < len(nums):
            if nums[fast] > nums[slow]:
                slow+=1
                nums[slow] = nums[fast]
                count = 1
                fast += 1
                continue
            #found same number
            if count < 2:   #2nd appearance
                slow+=1
                nums[slow] = nums[fast]
                count+=1
            fast +=1

        return slow+1