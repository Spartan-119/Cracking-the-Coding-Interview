# the Rabin-Karp algorithm without the sliding window optimization, calculating the hash for each window from scratch. 
# This version will be less efficient but easier to understand for beginners.

class RabinKarp:
    def __init__(self, base=256, prime=101):
        self.base = base
        self.prime = prime

    def calculate_hash(self, string):
        """Calculate hash for a given string"""
        hash_value = 0
        for char in string:
            hash_value = (self.base * hash_value + ord(char)) % self.prime
        return hash_value

    def pattern_matched(self, text: str, pattern: str) -> bool:
        if not pattern or len(pattern) > len(text):
            return False

        n, m = len(text), len(pattern)
        pattern_hash = self.calculate_hash(pattern)

        # Check each window of text
        for i in range(n - m + 1):
            window = text[i:i+m]
            window_hash = self.calculate_hash(window)

            if window_hash == pattern_hash:
                # If hashes match, check character by character
                if window == pattern:
                    return True

        return False