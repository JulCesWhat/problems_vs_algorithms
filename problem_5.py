

# Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.dict = {}

    def insert(self, char, new_node):
        # Add a child node in this Trie
        if char not in self.dict:
            self.dict[char] = new_node

    def suffixes(self, suffix='', suf_list=[]):
        # Recursive function that collects the suffix for
        # all complete words below this point

        if len(self.dict) is 0:
            return suf_list.append(suffix)

        for key in self.dict:
            new_node = self.dict[key]
            # suffix += key
            new_node.suffixes(suffix + key, suf_list)

        return suf_list


# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        current_node = self.root
        for char in word:
            if char not in current_node.dict:
                new_node = TrieNode()
                current_node.insert(char, new_node)

            current_node = current_node.dict[char]

        # Adding emtpy space to finish the word
        new_node = TrieNode()
        current_node.insert('', new_node)

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        current_node = self.root
        for char in prefix:
            if char in current_node.dict:
                current_node = current_node.dict[char]
            else:
                return None
        return current_node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')


test_1 = MyTrie.find("1")
print(test_1)
# None

test_2 = MyTrie.find("an")
print('\n'.join(test_2.suffixes('', [])))
# t
# thology
# tagonist
# tonym

test_3 = MyTrie.find("trigonometr")
print('\n'.join(test_3.suffixes('', [])))
# y
