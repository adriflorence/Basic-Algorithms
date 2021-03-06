# TIME AND SPACE COMPLEXITIES

### 1. Square root of integer

The first two tasks are solved with a very similar logic, with the use of a binary search algorithm, contantly halving the the range of numbers that include the solution.

The implemented binary search algorithm's runtime complexity is `O(log n)`.
The space complexity is not influenced by the size of the input, therefore it is `O(1)` in every case.

### 2. Rotated Array Search

The implemented binary search algorithm's runtime complexity is `O(log n)` as required.
The space complexity is not influenced by the size of the input, therefore it is `O(1)` in every case.

### 3. Rearrange Array Elements

The task was solved with an implementation of the merge sort algorithm: it divides input array in two halves, calls itself for the two halves and then merges the two sorted halves.
The time complexity of the merge sort is `O(n*log(n))`.
The worst case space complexity is `O(n)` where n is the number of elements in the array.

### 4. Dutch National Flag

The approach to solve this issue was sourced from the following pseudocode:

The array is partitioned into three groups: *"the bottom of the top group, the top of the bottom group, and the top of the middle group. Elements that are yet to be sorted fall between the middle and the top group. At each step, examine the element just above the middle. If it belongs to the top group, swap it with the element just below the top. If it belongs in the bottom, swap it with the element just above the bottom. If it is in the middle, leave it. Update the appropriate index."*

Sourced from https://en.wikipedia.org/wiki/Dutch_national_flag_problem

This task was solved with a single traversal of the array, therefore the time complexity is `O(n)` where n is the length of the array. 

*"Auxiliary Space is the extra space or temporary space used by an algorithm.
Space Complexity of an algorithm is total space taken by the algorithm with respect to the input size. Space complexity includes both Auxiliary space and space used by input."*
Therefore, the overall space complexity is `O(n)`, where n is the length of the input list.

Cited from https://www.geeksforgeeks.org/g-fact-86/

### 5. Autocomplete with Tries

Following the instructions provided by the course, I implemented a working trie for storing strings, then an autocomplete feature by creating a new function on the TrieNode object that will return all complete word suffixes that exist below it in the trie.

*"The worst-case runtime for creating a trie is a combination of m, the length of the longest key in the trie, and n, the total number of keys in the trie. Thus, the worst case runtime of creating a trie is `O(mn)`."*

Cited from https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014

### 6. Max and Min in a Unsorted Array

This task was solved with a single traversal linear search, so the time taken is proportional to length of the array, therefore the algorithm requires linear time complexity, `O(n)`, where n is the length of the array.
The amount of memory required does not change with the length, the algorithm itself still has only two target values (min, max). The space required by the algorithm remains constant regardless of the amount of data, therefore it is `O(1)`.

Source from https://www.youtube.com/watch?v=bNjMFtHLioA

### 7. HTTPRouter using a Trie

The HTTP Router was implemented with a similar approach to the autocomplete task. Using a Trie structure, but instead of each node representing a letter, I used them to store a block or part of the path name (parts in between slashes).

The time complexity of the implemented Trie's search and insert methods depend on how many slashes the pathname has, therefore how many path blocks/parts the search method will need to go though. Time complexity therefore is `O(n)` where n is the number of parts in-between slashes. 
Similarly, the amount of memory required to insert or lookup a path is `O(n)` where n is the number of parts in-between slashes. 