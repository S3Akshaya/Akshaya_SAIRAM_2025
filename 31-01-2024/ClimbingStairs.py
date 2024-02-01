''' Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 '''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        pre1=1
        pre2=2
        o=0
        for i in range(2,n):
            o=pre1+pre2
            pre1=pre2
            pre2=o
        return o
    
