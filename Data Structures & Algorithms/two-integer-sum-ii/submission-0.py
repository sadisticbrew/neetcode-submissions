class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        nums = numbers
        mp = defaultdict(int)
        for i in range(n) :
            complement = target - nums[i]
            if mp[complement]:
                return [mp[complement], i + 1]
            mp[nums[i]] = i + 1
        return []