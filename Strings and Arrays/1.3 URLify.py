# Approach One

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

	# start filling characters from the end.
	index = new_length - 1

	url = list(url)

	# filling the string array
	for i in range(n - 2, new_length - 2):
		url.append('0')

	# filling the rest of the string from the end
	for j in range(n - 1, 0, -1):
		# inserts %20 in place of space
		if url[j] == ' ':
			url[index] = '0'
			url[index - 1] = '2'
			url[index - 2] = '%'
			index = index - 3
		else:
			url[index] = url[j]
			index -= 1

	return ''.join(url)

#############################

# Testing the function
url = "Mr John Smith "
print(URLify(url))