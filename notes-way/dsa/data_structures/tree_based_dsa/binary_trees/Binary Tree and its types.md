# Binary Tree

This article cover:
1. [Binary Tree](https://www.programiz.com/dsa/binary-tree)

## Intro

A binary tree is a tree data structure in which each parent node can have at most two children. Each node of a binary tree consists of three items:

* data item
* address of left child
* address of right child

![](./../assets/img/binary_tree_1.webp)

## Types of Binary Tree

1. **Full Binary Tree**

    A full Binary tree is a special type of binary tree in which every parent node/internal node has either two or no children.

    ![](./../assets/img/full-binary-tree_0.webp)


2. **Perfect Binary Tree**

    A perfect binary tree is a type of binary tree in which every internal node has exactly two child nodes and all the leaf nodes are at the same level.

    ![](./../assets/img/perfect-binary-tree_0.webp)


3. **Complete Binary Tree**

    A complete binary tree is just like a full binary tree, but with two major differences

    1. Every level must be completely filled
    2. All the leaf elements must lean towards the left.
    3. The last leaf element might not have a right sibling i.e. a complete binary tree doesn't have to be a full binary tree.

    ![](./../assets/img/complete-binary-tree_0.webp)

4. **Degenerate or Pathological Tree**
   
    A degenerate or pathological tree is the tree having a single child either left or right.

    ![](./../assets/img/degenerate-binary-tree_0.webp)


5. **Skewed Binary Tree**

    A skewed binary tree is a pathological/degenerate tree in which the tree is either dominated by the left nodes or the right nodes. Thus, there are two types of skewed binary tree: left-skewed binary tree and right-skewed binary tree.

    ![](./../assets/img/skewed-binary-tree_0.webp)

6. **Balanced Binary Tree**

    It is a type of binary tree in which the difference between the height of the left and the right subtree for each node is either 0 or 1.

    ![](./../assets/img/height-balanced_1.webp)

## Binary Tree Representation

A node of a binary tree is represented by a structure containing a data part and two pointers to other structures of the same type.

```cpp
struct node
{
 int data;
 struct node *left;
 struct node *right;
};
```

![](./../assets/img/binary-tree-representation_0.webp)
