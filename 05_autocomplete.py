# Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
    # Add a child node in this Trie
    def insert(self, char):
        if char not in self.children:
           self.children[char] = TrieNode()

    # ["fun", "function", "factory"] -> expect to receive ["un", "unction", "actory"] back from node.suffixes()
    def suffixes(self, suffix = ''):
        suffixes = []

        if self.is_word and suffix != '':
            suffixes.append(suffix)

        if len(self.children) == 0:
            return suffixes

        for char in self.children:
            suffixes.extend(self.children[char].suffixes(suffix = suffix + char))

        return suffixes


    def print_children(self):
        for char in self.children:
            print(char)
        
# The Trie itself containing the root node and insert/find functions
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


# TEST 1

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

prefix = "f"
prefixNode = MyTrie.find(prefix)
if(prefixNode):
    print(prefixNode.suffixes())
else:
    print(prefix + " not found")

# TEST 2

MyTrie = Trie()
wordList = []
for word in wordList:
    MyTrie.insert(word)

prefix = "f"
prefixNode = MyTrie.find(prefix)
if prefixNode:
    print('\n'.join(prefixNode.suffixes()))
else:
    print(prefix + " not found")