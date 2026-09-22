class Solution:

    def frequencySort(self, nums: List[int]) -> List[int]:

        if not nums:
            return []

        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = []

            freq[num].append(num)#这里其实不需要保存所哟的values 只需要保存频次信息就可以了

        sorted_nums = sorted(
            freq,
            key=lambda x: (len(freq[x]), -x)
        )

        result = []

        for num in sorted_nums:
            result.extend(freq[num])

        return result


class Solution:
# sorted(data, key=lambda x: (primary_key, secondary_key))对一个 iterable 进行排序，并且返回一个新的 list。第一个参数是一可以遍历的对象 列入list tuple dictionary string setkey 的意思：告诉 Python：排序的时候应该根据什么值来比较元素。Python 对 tuple 的比较是：先比较第一个元素；如果第一个元素相同，再比较第二个元素。 
    def frequencySort(self, nums: List[int]) -> List[int]:

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        ordered = sorted(
            freq,
            key=lambda x: (freq[x], -x)
        )

        result = []

        for num in ordered:
            result.extend([num] * freq[num])

        return result