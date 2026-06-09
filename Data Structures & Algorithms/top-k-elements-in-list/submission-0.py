from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)
        nums_count = dict(sorted(nums_count.items(), key = lambda item:item[1],reverse=True))
        return list(nums_count.keys())[:k]