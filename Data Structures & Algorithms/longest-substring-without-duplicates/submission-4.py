class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        highest_len = 0
        for i in range(len(s)):
            new_string = s[i]
            for j in range(i+1,len(s)):
                if s[j] in new_string:
                    break
                if s[j] not in new_string:
                    new_string += s[j]
                if len(new_string) > highest_len:
                    highest_len = len(new_string)
        if len(s)>0 and highest_len==0:
            highest_len = 1
        return highest_len