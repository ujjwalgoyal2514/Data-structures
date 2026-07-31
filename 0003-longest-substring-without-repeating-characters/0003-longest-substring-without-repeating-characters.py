class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        l = r = 0
        maxi = 0

        while r < len(s):
            hash_map[s[r]] = hash_map.get(s[r], 0) + 1

            while hash_map[s[r]] > 1:
                hash_map[s[l]] -= 1
                l += 1

            maxi = max(maxi, r - l + 1)
            r += 1

        return maxi