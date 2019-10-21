open_list = ["{","[","("] 
close_list = ["}","]",")"]

#check for parentheses balance in a given exp
#using a stack
def check_parentheses_balance(exp):
	stack = []
	for i in exp:
		if i in open_list:
			stack.append(i)
		elif i in close_list:
			pos = close_list.index(i)
			if ((len(stack) > 0) and (open_list[pos] == stack[len(stack)-1])):
				stack.pop()
			else:
				return "Unbalanced"
	if len(stack) == 0:
		return "Balanced"




def main():
	string = "[(hjgfhjgdfhgf)]{}{[(lkjhkjggf)()](hgfdghdfh)}"
	print string + " - " + check_parentheses_balance(string)

	string = "[(cgfjhgkjh]kjgkjhg)"
	print string + " - " + check_parentheses_balance(string)

if __name__ == "__main__":
	main()