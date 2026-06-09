import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.findall('[a-zA-Z0-9]+',s)
        s = ''.join(s)
        if s.lower()==s[::-1].lower():
            return True
        else:
            return False
        