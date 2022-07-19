class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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