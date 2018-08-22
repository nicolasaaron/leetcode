"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2**31 -1
        INT_MIN = -2**31
        if (x == INT_MIN):
            return 0
        
        if (x > 0):
            sign = 1
        else:
            sign = -1
        
        x = abs(x)
        rev = 0        
        while (x != 0):
            pop = x % 10
            x = x // 10
            if (rev > (INT_MAX // 10) ) or ((rev == (INT_MAX // 10)) and (pop > (INT_MAX % 10))): 
                return 0
           # if (rev < (INT_MIN // 10)) or ((rev == (INT_MIN // 10)) and (pop < (INT_MIN % 10))) :
           #     return 0
            rev = rev * 10 + pop
        return sign * rev