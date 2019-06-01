'''
Check redundant brackets
Given a string mathematical expression, return true if redundant brackets are present in the expression. 
    1. Brackets are redundant if there is nothing inside the bracket or more than one pair of brackets are present.
    2. Assume the given string expression is balanced and contains only one type of bracket i.e. ().

Note: You will not get partial score for this problem. You will get marks only if all test cases are passed.
Input Format :
String s (Expression)
Output Format :
true or false
Sample Input 1:
((a + b)) 
Sample Output 1:
true
Sample Input 2:
(a+b) 
Sample Output 2:
false

'''


def hasRedundant(string):

    my_stack = [] # using list as stack
    for chr in string:

        if chr == ' ' :
            continue

        if chr == ')':
            if my_stack == [] : # not needed as it is given string is Balanced ,but using , my wish !! , :)
                return False

            if my_stack[-1] == '(':
                return True
            else:
                while my_stack[-1] != '(':
                    my_stack.pop()
                my_stack.pop()

        else:
            my_stack.append(chr)
    
    return False

def main():

    string = input()

    if hasRedundant(string):
        print('true')
    else:
        print('false')

if __name__ =='__main__':
	main()