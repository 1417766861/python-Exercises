'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的 两个 整数。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        """
        for index,num in enumerate(nums):
            for i in range(index+1,len(nums)):
                if nums[index] + nums[i] == target:
                    return [index,i]

if __name__ == '__main__':
    p = Solution()
    end = p.twoSum([2,1,5,4,11],12)
    print(end)

    #[1, 4]

