class Solution:
    

    def charToInt(self,c:str) -> int:
        if (c=='I'):
            return 1
        if (c=='V'):
            return 5
        if (c=='X'):
            return 10
        if (c=='L'):
            return 50
        if (c=='C'):
            return 100
        if (c=='D'):
            return 500
        if (c=='M'):
            return 1000
        return -1    
    
    def romanToInt(self, s: str) -> int:
        r=0
        for i in range(len(s)):
            val=self.charToInt(s[i])
            if(i+1<len(s)):
                nVal = self.charToInt(s[i+1])
                if(val<nVal):
                    val=val*-1
            r= r+val
        return r
            
