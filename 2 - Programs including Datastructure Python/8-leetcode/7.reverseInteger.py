import math


class Solution:
    def reverse(self, x: int) -> int:

        if x < 0:
            if(-1*int(str(abs(x))[::-1]) < -1*math.pow(2, 31)):
                return 0
            else:
                return -1*int(str(abs(x))[::-1])
        else:
            if(int(str(abs(x))[::-1]) >= math.pow(2, 31)):
                return 0
            else:
                return int(str(abs(x))[::-1])
