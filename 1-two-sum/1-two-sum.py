class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #O(n) vs O(n^2)
        e = set()
        dic ={};
        # Add all number
        for i in range(len(nums)):
            v = nums[i]
            e.add(v)
            dic[v] = i;
        for i in range(len(nums)):
            v = nums[i]
            g = target - v;                      
            if g in e: 
                if i!=dic[g]:
                    l = i                                      
                    r = dic[g]                                                 
                    return [l,r]
        return None      