# cook your dish here
def alpha(s):
    binaryy = ""
    for i in range(len(s)):
        if(s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u"):
            binaryy += "1"
        else:
            binaryy += "0"
    ans = 0
    power = 0
    for i in binaryy[::-1]:
        if(i == "1"):
            ans += pow(2, power, 1000000007)
            ans = ans % 1000000007
        power += 1
    return ans


t = int(input())
while(t > 0):
    s = input()
    print(alpha(s))
    t -= 1
