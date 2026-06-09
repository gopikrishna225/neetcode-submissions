import numpy as np
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            check = target-numbers[i]
            if (check in numbers) and (numbers.index(check)!=i):
                result = [numbers.index(check)+1,i+1]
                result.sort()
                return result