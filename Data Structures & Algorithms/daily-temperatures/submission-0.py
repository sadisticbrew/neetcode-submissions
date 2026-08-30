class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temperatures[i]:
                stack_v, stack_i = stack.pop()
                result[stack_i] = i - stack_i
            stack.append((temp, i))
        return result


