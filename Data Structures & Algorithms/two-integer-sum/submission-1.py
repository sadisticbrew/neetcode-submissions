class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        We can use a hashmap to see if we have seen the complement of the current number.
        Complement of the current number is what needs to be added to 
        current number so it matches the target. 
        i.e complement = target - curr_num
        in the hashmap, 1 means seen and we can immediately return the 
        list of indices, 0 means not seen so we can continue to look for it. 
        since every input is gauranteed to have exactly one pair of indices that 
        sum up to the target I can ignore the empty list edge case.
        """
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return []
            