#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (35.93%)
# Likes:    4950
# Dislikes: 150
# Total Accepted:    470.2K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,5]\n11'
#
# You are given coins of different denominations and a total amount of money
# amount. Write a function to compute the fewest number of coins that you need
# to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.
# 
# You may assume that you have an infinite number of each kind of coin.
# 
# 
# Example 1:
# 
# 
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# 
# 
# Example 2:
# 
# 
# Input: coins = [2], amount = 3
# Output: -1
# 
# 
# Example 3:
# 
# 
# Input: coins = [1], amount = 0
# Output: 0
# 
# 
# Example 4:
# 
# 
# Input: coins = [1], amount = 1
# Output: 1
# 
# 
# Example 5:
# 
# 
# Input: coins = [1], amount = 2
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        # init coin 
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        
        for i in range(1, amount+1):
            lst = [dp[i-coin]+1 for coin in coins if i>=coin]            
            if lst:
                dp[i] = min(lst)
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]
        
# @lc code=end

