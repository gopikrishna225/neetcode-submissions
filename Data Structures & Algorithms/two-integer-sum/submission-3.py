class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexs = []
        for j in nums:
            index2 = target-j
            if index2!=j:
                if index2 in nums:
                    indexs.extend([j,index2])
                    break
            elif (index2==j) and (nums.count(j)>1):
                if index2 in nums:
                    indexs.extend([j,index2])
                    break                
        indexs1 = []
        for i in indexs:
            val_indx = nums.index(i)
            indexs1.append(val_indx)
            nums[val_indx] = ''
        indexs1.sort()
        return indexs1