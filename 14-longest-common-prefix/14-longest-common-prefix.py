class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
           return ""
        out = strs[0]
        outCI = len(out)
        for i in range(len(strs)):

            current=strs[i]

            if len(current)==0:
                return ""

            if len(current)<outCI:
                outCI=len(current)

            for j in range(outCI):
                if current[j]!=out[j]:
                    outCI = j
                    if outCI==-1:
                        return ""
                    break

        return out[:outCI]
