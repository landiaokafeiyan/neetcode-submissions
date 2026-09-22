class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        res = [0] * (len(num1) + len(num2))
        # print(num1)
        num1, num2 = num1[::-1], num2[::-1]#倒序读取字符串
        # print(num1)
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += res[i1 + i2] // 10#carry
                res[i1 + i2] = res[i1 + i2] % 10

        res, beg = res[::-1], 0#反转结果数组
        while beg < len(res) and res[beg] == 0:
            beg += 1
        res = map(str, res[beg:])#把数字转换成字符串会把每个数字转换成字符串
        return "".join(res)