def compress_string(s):
    compressed = []
    counter = 0
    n = len(s)

    for i in range(n):
        if i != 0 and s[i] != s[i - 1]:
            compressed.append(s[i - 1] + str(counter))
            # resetting the counter
            counter = 0
        counter += 1

    # add last repeated character
    if counter:
        compressed.append(s[-1] + str(counter))

    # returns the original string if the compressed string isn't smaller
    return min(s, "".join(compressed), key=len)

print(compress_string("abbccccc"))
