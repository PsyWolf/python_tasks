import re
from collections import Counter

def get_most_common_words(filename, n):
	f = open(filename, "r")
	if f.mode == "r":
		contents = f.read()

		all_words = re.findall(r'\w+', contents) #get a list of all words in the file
		cap_words = [word.upper() for word in all_words] #capitalize all words
		word_counter = Counter(cap_words) #save the list in a Counter to save the words as {"word": count}

		most_common_words = word_counter.most_common(n) #get the most common words in decreasing order
		for word in most_common_words:
			print word[0] + ": " + str(word[1]) + "\n"

def main():
	get_most_common_words("text.txt", 2) #change the file name here

if __name__ == "__main__":
	main()