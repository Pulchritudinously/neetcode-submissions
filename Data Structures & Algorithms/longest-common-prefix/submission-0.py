class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = strs[0] # use first word 
        for i in range(1, len(strs)):
            j = 0
            while j < min(len(prefix), len(strs[i])):
                if prefix[j] != strs[i][j]:
                    break
                j += 1
            prefix = prefix[:j] 
            #IMPORTANT: prefix is a running candidate that gets overwritten each iteration. After matching flower and flow, the candidate became flow. THen flight is compared against this candidate "FLOW vs flight"

            # j is the length of the ocmmon prefix between the current prefix and strs[i] Include everthing up to j
        return prefix


# Time: O(n)
# Space: o(1)
        