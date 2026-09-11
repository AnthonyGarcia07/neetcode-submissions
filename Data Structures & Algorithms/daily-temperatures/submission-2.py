class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # temp : index
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            #while loop repeatedly checks the condition and executes the body until the condition becomes false. 
            #if checks the condition once. If it's true, the body executes once, then Python moves on.
            while stack and stack[-1][0] < t:
                stackT, stackI = stack.pop()
                res[stackI] = i - stackI

            stack.append((t,i))
        return res