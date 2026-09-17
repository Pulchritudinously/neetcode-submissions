class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)
        for i, num in enumerate(nums):
            ans[i] = ans[i + n] = num # set ans[i + n] = nums[i]
        return ans

# Time: o(n) length of input arr
# Space: o(n) allocate an array of size 2n 