def checkPermutations1(st1, st2):
	if len(st1) != len(st2):
		return False
	else:
		n = len(st1)
		st1 = sorted(st1)
		st2 = sorted(st2)

		for i in range(n):
			if st1[i] != st2[i]:
				return False

		return True


#####################################
# Approach 2

NO_OF_CHARS = 256

def checkPermutations2(st1, st2):

	# create two arrays and initialize
	# all values as 0

	count1 = [0] * NO_OF_CHARS
	count2 = [0] * NO_OF_CHARS

	# for each character in input strings,
	# increment count in the corresponding
	# count array

	for i in st1:
		count1[ord(i)] += 1

	for i in st2:
		count2[ord(i)] += 1

	# if both strings are of different length,
	# removing this condition will make the
	# program fail for strings like
	# "aaca" and "aca"

	if len(st1) != len(st2):
		return False

	# compare count arrays
	for i in range(NO_OF_CHARS):
		if count1[i] != count2[i]:
			return False

	return True

print(checkPermutations2('abcd', 'dbac'))