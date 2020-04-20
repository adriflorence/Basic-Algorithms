## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
    ## Add a child node in this Trie
    def insert(self, char):
        if char not in self.children:
           self.children[char] = TrieNode()
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        self.root = TrieNode()
     
    # Add a word to the Trie
    def insert(self, word):
        node = self.root

        for char in word:
            node.insert(char)
            node = node.children[char]

        node.is_word = True

    
    # Find the Trie node that represents this prefix
    def find(self, prefix):
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return node