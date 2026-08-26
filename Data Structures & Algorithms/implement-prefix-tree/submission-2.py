class TrieNode:

    def __init__(self, letter = "", marker = False, children = {}):
        self.letter = letter
        self.marker = marker
        self.children = children

class PrefixTree:

    def __init__(self):
        self.root = TrieNode("", False, {})

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode(c, False, {})
            
            cur = cur.children[c]
        
        cur.marker = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            
            cur = cur.children[c]
        
        return cur.marker
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            
            cur = cur.children[c]
        
        return True
        