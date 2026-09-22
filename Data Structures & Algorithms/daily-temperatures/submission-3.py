class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []  # 存放元素的索引 (index)

        for i, t in enumerate(temperatures):
            # 当栈不为空，且当前温度 t 大于栈顶索引对应的温度时
            while stack and t > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index  # 计算等待的天数
            
            stack.append(i)  # 把当前天的索引压入栈中

        return res
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     # def dailyTemperatures(temperatures: list[int]) -> list[int]:
    #     n = len(temperatures)
    #     res = [0] * n
        
    #     for i in range(n):
    #         for j in range(i + 1, n):
    #             if temperatures[j] > temperatures[i]:
    #                 res[i] = j - i
    #                 break  # 找到第一个更暖和的就立即停下
                    
    #     return res
    class Solution:
        def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
            res = [0] * len(temperatures)
            stack = []  # pair: [temp, index]

            for i, t in enumerate(temperatures):
                while stack and t > stack[-1][0]:
                    stackT, stackInd = stack.pop()
                    res[stackInd] = i - stackInd
                stack.append((t, i))
            return res