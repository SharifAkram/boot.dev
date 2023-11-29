class Trie:
    def words_with_prefix(self, prefix):
        words = []
        current = self.root
        for letter in prefix:
            if letter not in current:
                return []
            current = current[letter]
        return self.search_level(current, prefix, words)

    def search_level(self, cur, cur_prefix, words):
        if self.end_symbol in cur:
            words.append(cur_prefix)
        for letter in sorted(cur.keys()):
            if letter == self.end_symbol:
                continue
            words = self.search_level(cur[letter], cur_prefix + letter, words)
        return words

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True
