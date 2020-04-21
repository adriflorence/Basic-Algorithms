
class RouteTrieNode:
    def __init__(self):
        self.children = {}
        self.handler = None

    def insert(self, path_part):
        if path_part not in self.children:
            self.children[path_part] = RouteTrieNode()


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler
        # this is the root path or home page node
        self.root = RouteTrieNode()
        self.handler = None

    def insert(self, split_path, handler):
        node = self.root

        for path_part in split_path:
            node.insert(path_part)
            node = node.children[path_part]

        node.handler = handler
        # only assign the handler to the deepest node of this path

    def find(self):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        pass


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler, non_found_handler):
        self.router = RouteTrie()
        self.handler = handler
        self.non_found_handler = non_found_handler
        # You could also add a handler for 404 page not found responses as well!

    # Add a handler for a path
    def add_handler(self, path, handler):
        split_path = self.split_path(path)
        self.router.insert(split_path, handler)

    def lookup(self):
        pass
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler


    def split_path(self, path):
        parts = path.split("/")
        return parts


# TEST CASES

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# # some lookups with the expected output
# print(router.lookup("/"))
# # should print 'root handler'
# print(router.lookup("/home"))
# # should print 'not found handler' or None if you did not implement one
# print(router.lookup("/home/about"))
# # should print 'about handler'
# print(router.lookup("/home/about/"))
# # should print 'about handler' or None if you did not handle trailing slashes
# print(router.lookup("/home/about/me"))
# # should print 'not found handler' or None if you did not implement one