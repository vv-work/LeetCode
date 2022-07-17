def ContainsDublicate(nums:[int])->bool:
    """
        dic = set()
        for x in nums:
            if x in dic:
                return True
            else:
                dic.add(x)
    """
    """ 
    nums.sort()
    for i in range(1,len(nums)):

       if(nums[i-1]==nums[i]):
          return True
    

    return False
    """
    return len(nums)!=len(set(nums))


import unittest

class ContainsDublicateTest(unittest.TestCase):

    def test_containsDublicates(self):
        self.assertTrue(ContainsDublicate([1,2,3,1]))
        
    def test_notContainsDublicates(self):
        self.assertFalse(ContainsDublicate([1,2,3]))

    def test_lastNumber(self):
        self.assertTrue(ContainsDublicate([1,2,3,3]))

unittest.main()
