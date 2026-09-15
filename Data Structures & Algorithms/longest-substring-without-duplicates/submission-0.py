class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = start = 0
        state = {}
        
        for end in range(len(s)):
            state[s[end]] = state.get(s[end], 0) + 1
            while state[s[end]] > 1:
                state[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start + 1)

        return max_len

