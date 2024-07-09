# implementing rABIN karp algo for string matching

import unittest

class RabinKarp:
    def __init__(self, base = 256, prime = 101):
        self.base = base
        self.prime = prime

    def pattern_matched(self, text: str, pattern: str) -> bool:
        # the first and obvious edge case
        if not pattern or len(pattern) > len(text):
            return False
        
        n, m = len(text), len(pattern)
        

class TestRabinKarp(unittest.TestCase):
    def setUp(self) -> None:
        self.rabin_karp = RabinKarp()