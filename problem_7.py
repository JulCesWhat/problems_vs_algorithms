

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, rootHandler, noHandler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode('/', rootHandler)
        self.noHandler = noHandler

    def insert(self, sub_paths, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        index = 0

        for path in sub_paths:
            if path in current_node.children:
                current_node = current_node.children[path]
            else:
                handle_val = self.noHandler
                if len(sub_paths) - 1 is index:
                    handle_val = handler
                new_node = RouteTrieNode(path, handle_val)
                current_node.insert(path, new_node)
                current_node = current_node.children[path]
            index += 1

    def find(self, sub_paths):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root

        for path in sub_paths:
            if path in current_node.children:
                current_node = current_node.children[path]
            elif path == "":
                continue
            else:
                return self.noHandler

        return current_node.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, route, handler):
        # Initialize the node with children as before, plus a handler
        self.route = route
        self.handler = handler
        self.children = {}

    def insert(self, route, new_node):
        # Insert the node as before
        if route not in self.children:
            self.children[route] = new_node


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, no_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router = RouteTrie(root_handler, no_handler)

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        sub_paths = self.split_path(path)
        self.router.insert(sub_paths, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        sub_paths = self.split_path(path)
        return self.router.find(sub_paths)

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        sub_paths = path.split('/')
        return sub_paths[1:]


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route


# some lookups with the expected output
print(router.lookup("/"))
# should print 'root handler'

print(router.lookup("/home"))
# should print 'not found handler'

print(router.lookup("/home/about"))
# should print 'about handler'

print(router.lookup("/home/about/"))
# should print 'about handler'

print(router.lookup("/home/about/me"))
# should print 'not found handler'
