'''
Palindrome Permutation
Given a string, write a function to check if it is a permutation of a palindrome.
EXAMPLE:
Input: "Tact Coa"
Output: True
Explanation: permutations: ["taco cat", 'atco cta', ...]
'''
class PalindromePermutation:
	def __init__(self) -> None:
		return None

	def find_palindrome_permutation(self, st):
		# ignore casing
		st = st.lower()

		# creating an empty dictionary 'd' that would store the count of each character
		d = {}

		for char in st:
			if char in d.keys():
				d[char] += 1
			elif ord(char) >= 97 and ord(char) <= 122:
				d[char] = 1

		middle = ""
		for char in d:
			if middle and d[char] % 2 == 1:
				return False
			elif d[char] % 2 == 1:
				middle = char
		return True

#######################
# The main driver program

if __name__ == '__main__':
	palindrome = PalindromePermutation()
	print(palindrome.find_palindrome_permutation("Tact Coa\n"))
	print(palindrome.find_palindrome_permutation("abin varghese"))