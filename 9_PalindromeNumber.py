# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 19:06:01 2018

@author: iris
"""
import numpy as np


class Solution:
    def isPalindrome(self,x):
        if (x < 0) or ( (x > 0) and (x % 10 == 0)): return False
        res = 0
        while (x > res):
            res =  res * 10 + x % 10
            x = x // 10
        return (x == res) or (x == res // 10)
    
    def isPalindrome2 (self, x):
        if (x<0):
            return False
        else: 
            n = (np.log(x) / np.log(10) )  // 1
            while (n > 0):
                print(n, x)
                head = x // (10**n)
                tail = x % 10
                
                if (head == tail):
                    x = (x % (10**n)) // 10
                    n = n-2
                else:
                    return False
            return True

      
        

if __name__ == '__main__':
    print(Solution().isPalindrome(9999))