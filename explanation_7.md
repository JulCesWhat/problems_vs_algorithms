# Problem 7: Request Routing in a Web Server with a Trie

I decided to use Trie Node structure to solve this problem because it was the best way to handle
the input routes.

* Worse RouteTrie `insert` time case complexity: O(n)   n is the amount of the sub-paths 
* Worse RouteTrie `find` time case complexity: O(n)    n is the size of the word being retrieved
* Worse RouteTrieNode `insert` time case complexity: O(1)
* Worse Router `add_handler` time case complexity: O(n)    n is the amount of the sub-paths 
* Worse Router `lookup` time case complexity: O(n)   n is the amount of the sub-paths 
  
* Worse RouteTrie `insert` space complexity: O(1)    
* Worse RouteTrie `find` space complexity: O(1)
* Worse RouteTrieNode `insert` space complexity: O(1)
* Worse Router `add_handler` space complexity: O(1)
* Worse Router `lookup` space complexity: O(1)
    
    
## Required Tools
* Python3

## Usage
* clone project
* `cd {folder}` into the repo folder
* `python3 {fine_name}` the file you want to run