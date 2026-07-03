class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)
        for s in strs:
            L = [0]*26
            for c in s:
                L[ord(c) - ord("a")] += 1
            hashmap[tuple(L)].append(s)
            
        return list(hashmap.values())

