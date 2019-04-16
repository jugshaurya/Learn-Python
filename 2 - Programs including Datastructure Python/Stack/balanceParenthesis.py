'''
Balanced Paranthesis

Given a string expression, check if brackets present in the expression are balanced or not. Brackets are balanced if the bracket which opens last, closes first.
You need to return true if it is balanced, false otherwise.
Sample Input 1 :
{ a + [ b+ (c + d)] + (e + f) }
Sample Output 1 :
true
Sample Input 2 :
{ a + [ b - c } ]
Sample Output 2 :
false
'''


def isBalance(string):

	my_stack = [] # using list as stack
	for chr in string:
		if chr in '({[':
			my_stack.append(chr)
		elif chr in ')}]' :
			if my_stack == [] :
				return False

			if chr == ')':
				if my_stack[-1] != '(':
					return False
				else:
					my_stack.pop()
			elif chr == '}':
				if my_stack[-1] != '{':
					return False
				else:
					my_stack.pop()
			else :

				if my_stack[-1] != '[':
					return False
				else:
					my_stack.pop()

	return my_stack == []

def main():

	string = input()

	if isBalance(string):
		print('true')
	else:
		print('false')

if __name__ =='__main__':
	main()
