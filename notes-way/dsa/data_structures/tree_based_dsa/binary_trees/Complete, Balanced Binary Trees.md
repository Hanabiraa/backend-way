# Complete and Balanced Binary Trees

This article cover:
1. [Complete Binary Tree](https://www.programiz.com/dsa/complete-binary-tree)
2. [Balanced Binary Tree](https://www.programiz.com/dsa/balanced-binary-tree)

## Complete Binary Tree

complete binary tree is a binary tree in which all the levels are completely filled except possibly the lowest one, which is filled from the left.

A complete binary tree is just like a full binary tree, but with two major differences

1. All the leaf elements must lean towards the left.
2. The last leaf element might not have a right sibling i.e. a complete binary tree doesn't have to be a full binary tree.

![](./../../assets/img/comparison-1_0.webp)

![](./../../assets/img/comparison-2_0.webp)

![](./../../assets/img/comparison-3_0.webp)

![](./../../assets/img/comparison-4.webp)

### How a Complete Binary Tree is Created?

1. Select the first element of the list to be the root node. (no. of elements on level-I: 1)

![](./../../assets/img/complete-binary-tree-creation-1.webp)

2. Put the second element as a left child of the root node and the third element as the right child. (no. of elements on level-II: 2)

![](./../../assets/img/complete-binary-tree-creation-2.webp)

3. Put the next two elements as children of the left node of the second level. Again, put the next two elements as children of the right node of the second level (no. of elements on level-III: 4) elements).

4. Keep repeating until you reach the last element.

![](./../../assets/img/complete-binary-tree-creation-3.webp)

###  Relationship between array indexes and tree element

A complete binary tree has an interesting property that we can use to find the children and parents of any node.

If the index of any element in the array is `i`, the element in the index `2i+1` will become the left child and element in `2i+2` index will become the right child. Also, the parent of any element at index `i` is given by the lower bound of `(i-1)/2`.

Let's test it out,

## Balanced Binary Tree

A balanced binary tree, **also referred to as a height-balanced binary tree**, is defined as a binary tree in which the height of the left and right subtree of any node differ by not more than 1.

1. difference between the left and the right subtree for any node is not more than one
2. the left subtree is balanced
3. the right subtree is balanced

**balanced**

![](./../../assets/img/height-balanced_1.webp)

**unbalanced**

![](./../../assets/img/unbalanced-binary-tree.webp)