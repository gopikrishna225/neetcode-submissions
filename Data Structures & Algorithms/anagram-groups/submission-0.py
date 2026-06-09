from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs1 = [''.join(sorted(i)) for i in strs]
        strs1.sort()
        output = {}
        for v in set(strs1):
            for k in strs:
                k1 = ''.join(sorted(k))
                if (v in output.keys()) and (v==k1):
                    output[v].append(k)
                elif v==k1:
                    output[v] = [k]
        return list(output.values())