class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {"I": 1, 'V': 5, 'X': 10,
                   'L': 50, 'C': 100, 'D': 500, 'M':  1000}

        total = 0
        i = len(s)-1
        while(i >= 0):
            intValue = mapping[s[i]]
            if(i-1 >= 0 and s[i-1] == "I" and (s[i] == "V" or s[i] == "X")):
                total += (intValue-1)
                print(s[i])
                i -= 1
            elif(i-1 >= 0 and s[i-1] == "X" and (s[i] == "L" or s[i] == "C")):
                total += (intValue-10)
                print(s[i])
                i -= 1
            elif(i-1 >= 0 and s[i-1] == "C" and (s[i] == "D" or s[i] == "M")):
                total += (intValue-100)
                print(s[i])
                i -= 1
            else:
                total += intValue
            i -= 1

        return total
