#import numpy

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """        
        abs_nums = [abs(x  - target / 2.) for x in nums]
       # sort_index = numpy.argsort(nums)
       # nums = numpy.sort(nums)
        sort_index = sorted(range(len(nums)), key=abs_nums.__getitem__)
        abs_nums = sorted(abs_nums)
        
        for i in range(len(nums)-1):
            if (abs_nums[i] == abs_nums[i+1]) & (nums[sort_index[i]] + nums[sort_index[i+1]] == target):      
                break;
        return [ sort_index[i], sort_index[i+1] ]
        
#if __name__ == '__main__':
#    print(Solution().twoSum((2, 7, 11, 15), 9))