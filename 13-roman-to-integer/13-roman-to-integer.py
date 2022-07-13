class Solution:
    

    def charToInt(self,c:int) -> int:
        if c==ord('I'):
            return 1
        if c==ord('V'):
            return 5
        if c==ord('X'):
            return 10
        if c==ord('L'):
            return 50
        if c==ord('C'):
            return 100
        if c==ord('D'):
            return 500
        if c==ord('M'):
            return 1000
        return -1    
    
    def romanToInt(self, s: str) -> int:
        r=0
        for i in range(len(s)):
            val=self.charToInt(ord(s[i]))
            if(i+1<len(s)):
                nVal = self.charToInt(ord(s[i+1]))
                if(val<nVal):
                    val=val*-1
            r= r+val
        return r
            
