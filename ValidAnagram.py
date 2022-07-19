"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""
def isAnagram(s: str, t: str) -> bool:
    dicS = dict()
    for c in s:
        if(c in dicS):
            dicS[c] = dicS[c]+1
        else:
            dicS[c] = 1

    for c in t:
        if c in dicS:
            dicS[c] = dicS[c]-1
            if dicS[c]<=0 :
                del dicS[c]
        else:
            return False
    if(len(dicS)>0):
        return False

    return True

import unittest 

class IsAnagramTest(unittest.TestCase):

    def test_IsValidTrue(self):
        self.assertTrue(isAnagram("anagram","nagaram"))

    def test_IsValidTrue(self):
        self.assertTrue(isAnagram("",""))

    def test_IsValidFalse(self):
        self.assertFalse(isAnagram("rat","car"))

    def test_IsValidDiffrentCount(self):
        self.assertFalse(isAnagram("rraaa","ar"))

    def test_IsValidDiffrentCount2(self):
        self.assertFalse(isAnagram("ar","rraaa"))

    def test_IsValidDiffrentEmpty(self):
        self.assertFalse(isAnagram("","b"))

    def test_IsValidDiffrentEmpty2(self):
        self.assertFalse(isAnagram("a",""))

unittest.main()

