class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #sort array
        nums.sort()
        n = len(nums)   #length of array
        ans = []
        # -nums[i] = nums[j] + nums[k]
        #3 pointers should exist in the nums array
        for i in range(0, n-2, 1):
            if nums[i] > 0:
                # so imagine nums[i] == 1, and the consecutive numbers will be >= 1, which will not give total sum of zero
                break
            if i > 0  and -nums[i] == target: #current number is same as previous target
                continue
            target = -nums[i] #assign new target
            #print ("target : ", target)
            j = i+1 #next to current target
            k = n-1 #last index
            while (j<k):
                if j > i+1 and nums[j] == nums[j-1]:
                    #j contraint is to make sure the j does not check with the target and let while loop run atleast once
                    # don't want repitative ans and checking
                    #print("same j")
                    j+=1
                    continue
                if k < n-2 and nums[k] == nums[k+1]:
                    #k contraint is to make sure the k is not out of the list and let while loop run atleast once
                    # don't want repitative ans and checking
                    #print("same k")
                    k-=1
                    continue
                current_sum = nums[j] + nums[k]
                #print(current_sum)
                if current_sum == target:
                    triplets = [nums[i], nums[j], nums[k]]
                    ans.append(triplets)
                    #print(triplets)
                    k -= 1
                    j += 1
                else :
                    #try to form zero basically
                    if current_sum > target :
                        #we need to remove the bigger num out of the equation to make the sum near to target
                        k -= 1
                    else:
                        j += 1
        return ans