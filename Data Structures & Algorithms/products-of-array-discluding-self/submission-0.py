import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums1 = nums.copy()
        output = []
        for i in range(len(nums)):
            nums1.pop(i)
            output.append(math.prod(nums1))
            nums1 = nums.copy()
        return output