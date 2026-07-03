class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hm = {}
        out = []
        for num in nums:
            hm[num] = 1 + hm.get(num, 0)
        sorted_hm =  dict(sorted(hm.items(), key=lambda item: item[1], reverse=True))
        freq = list(sorted_hm.keys())
        for i in range(k):
            out.append(freq[i])
        return out