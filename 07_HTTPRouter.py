
class RouteTrieNode:
    def __init__(self):
        self.children = {}
        self.handler = None

    def insert(self, path_part):
        if path_part not in self.children:
            self.children[path_part] = RouteTrieNode()


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        # the Trie is initialized with a root node and a handler
        self.root = RouteTrieNode()
        self.handler = root_handler

    def insert(self, split_path, handler):
        node = self.root

        for path_part in split_path:
            node.insert(path_part)
            node = node.children[path_part]

        node.handler = handler
        # only assign the handler to the deepest node of this path

    def find(self, split_path):
        node = self.root

        for path_part in split_path:
            if path_part not in node.children:
                # return None for no match
                return None
            node = node.children[path_part]

        # return the handler for a match
        return node.handler

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, no_handler):
        self.router = RouteTrie(root_handler)
        self.no_handler = no_handler
        # You could also add a handler for 404 page not found responses as well!

    # add a handler for a path
    def add_handler(self, path, handler):
        split_path = self._split(path)
        self.router.insert(split_path, handler)

    # lookup path (by parts) and return the associated handler
    def lookup(self, path):
        split_path = self._split(path)

        if len(split_path) == 0:
            return self.router.handler

        result = self.router.find(split_path)

        return self.no_handler if result is None else result


    def _split(self, path):
        parts = path.split("/")
        # removes trailing slash
        parts = [x for x in parts if x!=""]
        return parts


# TEST CASES

# create the router and add a route
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))
# should print 'root handler'
print(router.lookup("/home"))
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))
# should print 'about handler'
print(router.lookup("/home/about/"))
# should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))
# should print 'not found handler' or None if you did not implement one