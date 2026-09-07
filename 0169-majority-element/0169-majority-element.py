class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #without sorting
        num_dict={}
        n=len(nums)
        m = math.floor(n/2)

        for i in range(0, n):
            if nums[i] in num_dict:
                num_dict[nums[i]]+=1
            else:
                num_dict[nums[i]]=1

        for i in num_dict:
            if num_dict[i] > m:
                return i

        """
        nums.sort()
        n=len(nums)
        current_max=nums[0]

        if n<2:
            return current_max

        m=math.floor(n/2)

        count=1

        for i in range(1,n):
            if nums[i] != current_max:
                count=1
                current_max = nums[i]
            else:
                count+=1
                if count > m:
                    return current_max

            i+=1

        return current_max
        """
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
        """