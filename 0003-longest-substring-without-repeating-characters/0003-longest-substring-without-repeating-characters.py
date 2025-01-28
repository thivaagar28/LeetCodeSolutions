class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #sliding window technique
        seen = set()
        left, length = 0, 0
        for right in range(0, len(s), 1):
            if s[right] not in seen:
                seen.add(s[right])
            else:
                #calculate the max length without repeating characters
                length = max(length, len(seen))
                #now need to remove elements from left until the repeating character is removed from the seen and then add the current the current character in
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1
                #while loop will end once the repeating character is removed
                seen.add(s[right])

        #also need to consider last character where if the last character was unique and added to the seen
        length = max(length, len(seen))
        return length