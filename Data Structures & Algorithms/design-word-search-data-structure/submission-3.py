class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_End = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_End = True 

    def search(self, word: str) -> bool:
        def dfs(node , i):
            if len(word) == i:
                return node.is_End

            ch = word[i]
            if ch == '.':
                for ch in node.children.values():
                    if dfs(ch , i + 1):
                        return True
                return False 
            else:
                if ch not in node.children:
                    return False 
                return dfs(node.children[ch] , i + 1)
        return dfs(self.root , 0)

    
                
        
