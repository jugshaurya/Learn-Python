class Solution:
    def powpow(self, x, n):
        if(n == 0):
            return 1
        if(n == 1):
            return x

        smallpowpow = self.powpow(x, n//2)
        mid_result = smallpowpow * smallpowpow
        return mid_result*x if(n % 2) else mid_result

    def myPow(self, x: float, n: int) -> float:
        result = self.powpow(x, abs(n))
        return result if(n >= 0) else (1/result)

# other


class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n < 0:
            x = 1/x
            n = -n

        ans = 1
        while n:
            if n & 1:
                ans *= x
            x *= x
            n >>= 1
        return ans
