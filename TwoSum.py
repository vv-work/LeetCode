from typing import List


def twoSum( nums: List[int], target: int) -> List[int]:
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
                    l = i;
                    r = dic[g]
                    return [l,r]
        return []

print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))
print(twoSum([1,3,3],6))
print(twoSum([3,3,1],6))
          
