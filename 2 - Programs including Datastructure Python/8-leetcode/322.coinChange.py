# complexity O(len(coins)^ amount)  if coins have 1 in it  -> horrible
# space Complexity : O(amount) if coins have 1 in it


class Solution:

    def minCoins(self, coins, amount):
        if(amount < 0):
            return -1
        if(amount == 0):
            return 0
        min_value = 9999999
        for coin in coins:
            minSubCoins = self.minCoins(coins, amount - coin)
            if(minSubCoins != -1):
                min_value = min(min_value, minSubCoins)

        if(min_value == 9999999):
            return -1
        else:
            return min_value + 1

    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.minCoins(coins, amount)

# since this problem have optimal SubStructures and have operlapping subproblems as well
# Hence we can use extra space ior say memCache to store some results
# DP Approach: TOP-DOWN APPROACH
# Time Complexity = O(amount*len(coins))
# space complexity = O(amount) + recusion stack space


class Solution:
    def minCoins(self, coins, amount, dp):
        if(amount < 0):
            return -1

        if(amount == 0):
            return 0

        if(dp[amount] != -2):
            return dp[amount]

        min_value = 9999999
        for coin in coins:
            minSubCoins = self.minCoins(coins, amount - coin, dp)
            if(minSubCoins != -1):
                min_value = min(min_value, minSubCoins)
        if(min_value == 9999999):
            dp[amount] = -1
            return dp[amount]
        else:
            dp[amount] = min_value + 1
            return dp[amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-2] * (amount + 1)
        dp[0] = 0
        self.minCoins(coins, amount, dp)
        return dp[amount]


# DP Approach: Bottom-UP APPROACH
# Space O(amount)
# Time O(amount*len(coins))

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount+1):
            min_value = 999999
            for coin in coins:
                if(i - coin >= 0 and dp[i - coin] != -1):
                    min_value = min(min_value, dp[i - coin])

            if(min_value == 999999):
                dp[i] = -1
            else:
                dp[i] = min_value + 1
        return dp[amount]
