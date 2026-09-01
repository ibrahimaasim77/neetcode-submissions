class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        from collections import Counter

        chars_count = Counter(chars)
        total = 0

        for word in words:
            word_count = Counter(word)

            # Check if this word can be made from chars
            if all(word_count[char] <= chars_count[char] for char in word_count):
                total += len(word)

        return total