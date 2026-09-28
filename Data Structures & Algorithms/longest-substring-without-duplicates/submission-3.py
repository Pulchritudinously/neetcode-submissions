class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # charSet = set()
        # l = 0
        # res = 0

        # for r in range(len(s)):
        #     while s[r] in charSet: # if we found a char already in set, remove and increment left poitner
        #         charSet.remove(s[l])
        #         l += 1
        #     charSet.add(s[r])
        #     res = max(res, r - l + 1)
        # return res

        # Can be optimzed to strore the last index of each character. Instead of removing chars one by one when we see repeat, we can jump the left point direcctly to the correct pos

        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l) # move left pointer to char last seen 
            mp[s[r]] = r # add char to map with index of r
            res = max(res, r - l + 1)
        return res

    # Time: O(n)
    # Space: O(m)
            