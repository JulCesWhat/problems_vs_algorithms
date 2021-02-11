# Problem 5: Autocomplete with Tries

Decided to use Trie Node data structure since we need to find prefixes of words and need to store
the values while using the least memory.

* Worse TrieNode `insert` time case complexity: O(1)    
* Worse TrieNode `suffixes` time case complexity: O(n)    n is the size of the word being retrieved
* Worse Trie `insert` time case complexity: O(n*m)    n is the size of the dictionary of current node and m
  the size of dictionary of the child node
* Worse Trie `find` time case complexity: O(n)    n is the size of the suffix word

* Worse TrieNode `insert` space complexity: 0(1)
* Worse TrieNode `suffixes` space complexity: 0(1)
* Worse Trie `insert` space complexity: 0(1)
* Worse Trie `find` space complexity: 0(1)

    
    
## Required Tools
* Python3

## Usage
* clone project
* `cd {folder}` into the repo folder
* `python3 {fine_name}` the file you want to run