class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        #convert magazine to list
        magazine_list = list(magazine)

        for char in ransomNote:
            try :
                index = magazine_list.index(char)
                magazine_list.pop(index)
            except ValueError:
                return False
                
        return True