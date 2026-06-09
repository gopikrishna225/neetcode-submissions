class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        elif len(nums)==0:
            return 0
        nums.sort()
        counts = []
        count1 = 1
        for i in range(len(nums)):
            try:
                if (nums[i]+1 == nums[i+1]):
                    count1+=1
                elif (nums[i] == nums[i+1]):
                    continue
                else:
                    # print(i)
                    counts.append(count1)
                    count1 = 1
            except IndexError as e:
                if (len(counts)==0) or (count1 not in counts):
                    counts.append(count1)
                else:
                    continue
        return max(counts)
        