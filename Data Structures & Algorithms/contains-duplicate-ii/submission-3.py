class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # Sliding window, given arr within window k

        window = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1 # if window size exceeds k remove nums[L] and increment
            if nums[R] in window: # duplicate found
                return True

            window.add(nums[R])
        
        return False
    
# Time: o(N)
# Space: O(min(n, k))