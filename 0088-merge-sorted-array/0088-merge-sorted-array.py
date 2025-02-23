class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n != 0:  #there are elements to merge from nums2
            i = 0   #choose the 1st element of nums2, m is already pointing to the place where new numnbers should be added
            while i < n:
                nums1[m+i] = nums2[i]
                i += 1
            nums1.sort()