class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = len(nums) - 1

        if j == 0: #size 1
            if nums[i] == val:
                return 0 #ntg other than val
            else:
                1

        while i <= j:
            if nums[i] == val:  #need to replace with the 2nd pointer
                #2nd pointer should not be the val
                while nums[j] == val : #move pointer until 2nd pointer not val
                    if j <= i: #couldn't find a index to replace
                        return i
                    j -= 1
                nums[i] = nums[j] #replace with 2nd pointer value
                j -= 1  #reduce after replacing
            if i == j:
                return i+1
            i += 1
        
        return i+1