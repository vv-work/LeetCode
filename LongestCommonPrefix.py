
def longestCommonPrefix(strs) -> str :

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

print(longestCommonPrefix(["cir","car"]))

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["flower","flow","flight","form"]))
print(longestCommonPrefix(["dog","racer","flight"]))
print(longestCommonPrefix(["dog"]))
print(longestCommonPrefix(["dog","dogie"]))
print(longestCommonPrefix([""]))
