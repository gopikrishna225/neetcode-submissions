from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums)==0:
            return False
        reslut = Counter(nums)
        if max(reslut.values())>1:
            return True
        else:
            return False
        