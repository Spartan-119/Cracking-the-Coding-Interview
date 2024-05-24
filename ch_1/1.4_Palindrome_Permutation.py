'''
Palindrome Permutation
Given a string, write a function to check if it is a permutation of a palindrome.
EXAMPLE:
Input: "Tact Coa"
Output: True
Explanation: permutations: ["taco cat", 'atco cta', ...]
'''

class PalidromePermutation:
	def __init__(self) -> None:
		return None

	def find_palindrome_permutation(self, st) -> bool:
		st = st.lower()			# ignore the casing
		d = {}

		for char in st:
			if char in d.keys():
				d[char] += 1
			elif ord(char) >= 97 and ord(char) <= 122:
				d[char] = 1

		middle = False
		for char in d:
			if middle and d[char] % 2 == 1:
				return False
			elif d[char] % 2 == 1:
				middle = char

		return True


#############################
# the main driver method
if __name__ == '__main__':
	palidrome = PalidromePermutation()
	test_cases = ['Racecar', 'Tact Coa', 'Python Programming']

	for test in test_cases:
		print(palidrome.find_palindrome_permutation(test))








