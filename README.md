# TASK 1 - SQUARE ROOT OF INTEGER

Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.
If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.


# TASK 2 - Search in a Rotated Sorted Array

You are given a sorted array which is rotated at some random pivot point.

`Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]`

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of `O(log n)`.

`Example: Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4`.

# TASK 3 - Rearrange Array Elements

Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is `O(nlog(n))`.

`Example: [1, 2, 3, 4, 5]`

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

# TASK 4 - Dutch National Flag

Given an input array consisting on only 0, 1, and 2, sort the array in a **single traversal**. You're not allowed to use any sorting function that Python provides.

Note: `O(n)` does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an `O(n)` solution but it will not count as single traversal.

# TASK 5 - Autocomplete with Tries

First, create a working trie for storing strings. Create:
- A Trie class that contains the root node (empty string)
- A TrieNode class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.

Secondly, implement an autocomplete feature by creating a new function on the TrieNode object that will return all complete word suffixes that exist below it in the trie.

For example, if the Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the f node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.

# TASK 6 - Max and Min in a Unsorted Array

In this problem, look for smallest and largest integer from a list of unsorted integers. The code should run in `O(n)` time. Do not use Python's inbuilt functions to find min and max.
Is it possible to find the max and min in a single traversal?

# TASK 7 - HTTPRouter using a Trie

Implement an HTTPRouter like in a typical web server using the Trie data structure. There are many different implementations of HTTP Routers such as regular expressions or simple string matching, but the Trie is an excellent and very efficient data structure for this purpose.

The purpose of an HTTP Router is to take a URL path like `"/"`, `"/about"`, or `"/blog/2019-01-15/my-awesome-blog-post"` and figure out what content to return. In a dynamic web server, the content will often come from a block of code called a `handler`.

The Trie will contain a part of the http path at each node, building from the root node /

In addition to a path though, we need to know which function will handle the http request. In a real router we would probably pass an instance of a class like Python's SimpleHTTPRequestHandler which would be responsible for handling requests to that path. For the sake of simplicity, just a string should be printed out to display of the right handler.

Split the path into parts that are separated by slashes ("/"). A Trie with a single path entry of: "/about/me" would look like:

`(root, None) -> ("about", None) -> ("me", "About Me handler")`

Also, the RouteTrie class is simplified a bit by excluding the suffixes method and the endOfWord property on RouteTrieNodes. It is just the insertion and finding of nodes that are used, and if a RouteTrieNode is not a leaf node, it will not have a handler.

The Router will initialize itself with a RouteTrie for holding routes and associated handlers. It should also support adding a handler by path and looking up a handler by path. All of these operations will be delegated to the RouteTrie.

Bonus Points:
- Add a not found handler to your Router which is returned whenever a path is not found in the Trie.
- Handle trailing slashes! A request for '/about' or '/about/' are probably looking for the same page. Requests for '' or '/' are probably looking for the root handler. Handle these edge cases in your Router.


# TIME AND SPACE COMPLEXITIES

### 1. Square root of integer

The time complexity is `O(log(n))`.
The space complexity is not influenced by the size of the input, the method is just placin pointers, therefore it is `O(1)` in every case.

### 2. Rotated Array Search

The implemented algorithm (binary search algorithm)'s runtime complexity is O(log n) as required.
The space complexity is not influenced by the size of the input, the method is just placin pointers, therefore it is `O(1)` in every case.

### 3. Rearrange Array Elements

The tast was solved with an implementation of the merge sort algorithm, having a time complexity of `O(n*log(n))`.

### 4. Dutch National Flag

This task was solved with a single traversal of the array, therefore the time complexity is `O(n)` where n is the length of the array. 

### 5. Autocomplete with Tries

"The worst-case runtime for creating a trie is a combination of m, the length of the longest key in the trie, and n, the total number of keys in the trie. Thus, the worst case runtime of creating a trie is O(mn)." 

Cited from https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014

### 6. Max and Min in a Unsorted Array

This task was solved with a single traversal of the array, therefore the time complexity is `O(n)` where n is the length of the array. 

### 7. HTTPRouter using a Trie

The time complexity of the implemented Trie's search and insert methods depend on how many slashes the pathname has, therefore how many path blocks/parts the search method will need to go though. Time complexity therefore is `O(n)` where n is the sum of the parts in-between slashes. 