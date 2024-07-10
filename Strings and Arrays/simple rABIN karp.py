# the Rabin-Karp algorithm without the sliding window optimization, calculating the hash for each window from scratch. 
# This version will be less efficient but easier to understand for beginners.

class RabinKarp:
    def __init__(self, base=256, prime=101):
        self.base = base
        self.prime = prime

    def calculate_hash(self, string):
        """Calculate hash for a given string"""
        """
        The conceptual formula for the hash. For "ABC" with base 256, it would indeed be:
        A * 256² + B * 256¹ + C * 256⁰
        This code is actually implementing the same concept, just in an iterative manner. Let's break it down step by step for "ABC":
        1. Start with hash_value = 0
        2. For 'A':
         hash_value = (256 * 0 + ord('A')) % prime
         This is equivalent to: A * 256⁰
        3. For 'B':
         hash_value = (256 * (A * 256⁰) + ord('B')) % prime
         This is equivalent to: A * 256¹ + B * 256⁰
        4. For 'C':
         hash_value = (256 * (A * 256¹ + B * 256⁰) + ord('C')) % prime
         This is equivalent to: A * 256² + B * 256¹ + C * 256⁰
        As you can see, after processing each character, we're effectively shifting the previous value left by one position (multiplying by 256) and then adding the new character.
        The `% prime` operation is performed at each step to keep the numbers manageable and to distribute the hash values more evenly.
        """
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