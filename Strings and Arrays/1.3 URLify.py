'''
Replaces spaces with %20 in-place
and returns new length of modified string.
It returns -1 if the modified string 
cannot be stored in the str[] array.

'''
def URLify(url):

	# remove leading and trailing spaces
	url = url.strip()
	n = len(url)

	# count spaces and find current length
	space_count = url.count(' ')

	# Finding the new length
	new_length = n + (space_count * 2)

	# the new length must be smaller than
	# the length of the string provided.

	# here 1000 is the chosen maximum 
	# length of the string after 
	# modifications. You can choose
	# any other value too.
	if new_length > 1000:
		return -1

	url = list(url)
	result = []

	# start filling the characters from the front
	for i in range(len(url)):
		if url[i] == ' ':
			result.append('%')
			result.append('2')
			result.append('0')
		else:
			result.append(url[i])

	# return the result in the string format
	return ' '.join([str(elem) for elem in result])


#############################

# Testing the function
url = "Mr John  Smith "
print(URLify(url))
