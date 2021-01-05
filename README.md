# Mirrored Binary Search Tree



## About The Project 

This algorithm has been designed to convert a given binary tree to a mirrored binary search tree and to output the pre-order traversal of the resultant tree. 

- To mirror the original binary tree, the left and right child for each node is swapped 

- Since in-order traversal of a binary search tree would yield a list of sorted values, perform an in-order traversal of the mirrored binary tree and replace the original value of each node with the corresponding sorted value to preserve the structure of the mirrored binary tree  

- Perform pre-order traversal of the mirrored binary search tree to generate output values

  

## Time Complexity

The time complexity for this algorithm in MBST function is O(n^2), where n is the number of nodes. This is because in the nested for-loops to link each node to its respective child node(s), the outer for-loop will be executed n times and for each execution of the outer for-loop, the inner for-loop will be executed n times to search for the child node(s). Thus, the total number of operations from the nested for-loops would be n*n = n^2 based on product rule and the time complexity would be O(n^2).

