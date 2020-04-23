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


# TESTS

def autocomplete_test(prefix, trie):
    prefix_node = trie.find(prefix)
    if(prefix_node):
        print(prefix, prefix_node.suffixes())
    else:
        print(prefix + " not found")
    pass

# TEST 1 & 2

my_trie_1 = Trie()
word_list_1 = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in word_list_1:
    my_trie_1.insert(word)

prefix_1 = "f"
prefix_2 = "tri"
autocomplete_test(prefix_1, my_trie_1)
autocomplete_test(prefix_2, my_trie_1)

# TEST 3

my_trie_3 = Trie()
word_list_3 = []
for word in word_list_3:
    my_trie_3.insert(word)

prefix = "f"

autocomplete_test(prefix, my_trie_3)

# TEST 4

my_trie_4 = Trie()
word_list_4 = ["python", "python", "python"]
for word in word_list_4:
    my_trie_4.insert(word)

prefix_4 = "q"

autocomplete_test(prefix_4, my_trie_4)