def twoSum(self, nums, target):
    hash_nums = {}
    for index, num in enumerate(nums):
        another = target - num
        try:
            hash_nums[another]
            return [hash_nums[another], index]
        except KeyError:
            hash_nums[num] = index


def twoSum(self, nums, target):
    # two point
    nums_index = [(v, index) for index, v in enumerate(nums)]
    nums_index.sort()
    begin, end = 0, len(nums) - 1
    while begin < end:
        curr = nums_index[begin][0] + nums_index[end][0]
        if curr == target:
            return [nums_index[begin][1], nums_index[end][1]]
        elif curr < target:
            begin += 1
        else:
            end -= 1


class Solution:
    def twoSum(self, nums, target):
        nums_hash = {}
        for i in range(len(nums)):
            if target - nums[i] in nums_hash:
                return [nums_hash[target - nums[i]], i]
            nums_hash[nums[i]] = i


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.twoSum([3, 2, 4, 77, 231], 234))
