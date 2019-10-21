#high and low function using built in functions
def high_and_low_auto(exp):
	num_list = exp.split()
	max_value = max(num_list)
	min_value = min(num_list)
	return max_value + " " + min_value

#get the lowest value in a list of numbers
def my_min(my_list):
	min_value = None
	for value in my_list:
		if not min_value:
			min_value = value
		elif value < min_value:
			min_value = value
	return min_value

#get the highest value in a list of numbers
def my_max(my_list):
	max_value = None
	for value in my_list:
		if not max_value:
			max_value = value
		elif value > max_value:
			max_value = value
	return max_value

#high and low function using my own functions
def high_and_low_manual(exp):
	num_list = exp.split()
	max_value = my_max(num_list)
	min_value = my_min(num_list)
	return max_value + " " + min_value

def main():
	print high_and_low_auto("1 2 3 4 5")
	print high_and_low_auto("1 2 -3 4 5")
	print high_and_low_auto("1 9 3 4 -5")

	print high_and_low_manual("1 2 3 4 5")
	print high_and_low_manual("1 2 -3 4 5")
	print high_and_low_manual("1 9 3 4 -5")

if __name__ == "__main__":
	main()