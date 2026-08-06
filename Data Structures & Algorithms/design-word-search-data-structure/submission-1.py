class TrieNode:
    def __init__(self):
        self.children = {}   # maps a character -> child TrieNode
        self.is_end = False  # True if a full word ends exactly at this node


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()  # empty root, represents "no characters consumed yet"

    def addWord(self, word: str) -> None:
        node = self.root  # pointer starts at root for every insert
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()  # create branch if it doesn't exist yet
            node = node.children[ch]  # move pointer down into that branch (new or existing)
        node.is_end = True  # after consuming all chars, mark this node as "a word ends here"

    def search(self, word: str) -> bool:
        def dfs(node, i):
            # node = current position in the trie
            # i    = current index into the search word

            if i == len(word):
                # we've consumed the whole search word;
                # it's only a real match if a word actually ends here,
                # not just because the letters existed as a prefix
                return node.is_end

            ch = word[i]  # the character we need to match at this position

            if ch == '.':
                # wildcard: try every possible branch from this node
                for ch in node.children.values():
                    # recurse: check if the REST of the word (i+1 onward)
                    # matches starting from this particular child
                    if dfs(ch, i + 1):
                        return True  # one branch worked -> whole search succeeds, stop early
                return False  # none of the branches worked -> this path fails

            else:
                # literal letter: only one possible branch to try
                if ch not in node.children:
                    return False  # that letter doesn't exist here at all -> dead end
                # letter exists -> move one level deeper and check the rest of the word
                return dfs(node.children[ch], i + 1)

        return dfs(self.root, 0)  # start the search at the root, position 0

        
