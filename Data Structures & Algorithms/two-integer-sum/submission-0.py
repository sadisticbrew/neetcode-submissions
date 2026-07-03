class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in hashmap:
                hashmap[nums[i]] = i
                continue
            return [hashmap[diff], i] 