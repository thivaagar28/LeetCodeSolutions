class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 1
        candidate = nums[0] #1st candidate
        count = 1
        n = len(nums)
        if n < 2:
            return candidate #one and only candidate with only voter
        m = math.floor(n/2)
        while i < n:
            if nums[i] == candidate:
                count += 1 #increase vote
                if count > m :
                    return nums[i]
            else:
                candidate = nums[i] #new candidate
                count = 1
            i +=1