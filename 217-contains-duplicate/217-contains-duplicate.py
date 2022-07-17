class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = set()
        for x in nums:
            if x in dic:
                return True
            else:
                dic.add(x)
        return False
