class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # 编码格式: 长度 + '#' + 字符串本身
            # 例如: ["lint", "code"] -> "4#lint4#code"
            res += f"{len(s)}#{s}"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            # 1. 用指针 j 找到当前长度后的第一个 '#'
            j = i
            while s[j] != '#':
                j += 1
            
            # 2. 截取 i 到 j 之间的数字作为长度
            length = int(s[i:j])
            
            # 3. 从 j + 1 开始，截取长度为 length 的原字符串
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            # 4. 将指针 i 移动到下一个编码块的起点
            i = end
            
        return res