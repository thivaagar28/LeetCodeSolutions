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
            i = 0
            while i < n:
                nums1[m] = nums2[i]
                m += 1
                i += 1
            nums1.sort()