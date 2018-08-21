"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


"""
first solution
""" 


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



"""
one hash table
"""

class Solution:
	def twoSum(self, nums, target):
		dic = {}
		for i, value in enumerate(nums):
			key = target - value
			if key in dic:
				return [dic[key], i]
			else:
				dic[value] = i




			
				