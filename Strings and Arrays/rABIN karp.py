# implementing rABIN karp algo for string matching

def rabin_karp(source, search):
    """
    Returns the starting index of the first occurrence of search in source,
    or -1 if not found.
    """
    source_len = len(source)
    search_len = len(search)
    if search_len == 0:
        return 0

    hash_source = hash(search)
    hash_search = hash(search[0])
    result = -1
    for i in range(source_len - search_len + 1):
        if hash_source == hash(source[i:i+search_len]):
            if source[i:i+search_len] == search:
                result = i
                break
        hash_source = (hash_source * 256 - ord(source[i]) * 256**(search_len-1)) // 256
        if i < source_len - search_len:
            hash_search = (hash_search * 256 - ord(source[i+1]) * 256**(search_len-1)) // 256
    return result
