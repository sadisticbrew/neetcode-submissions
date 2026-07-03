class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        cnt_s, cnt_t = {}, {}

        for char in s:
            cnt_s[char] = cnt_s.setdefault(char, 0) + 1

        for char in t:
            cnt_t[char] = cnt_t.setdefault(char, 0) + 1

        
        return cnt_s == cnt_t
