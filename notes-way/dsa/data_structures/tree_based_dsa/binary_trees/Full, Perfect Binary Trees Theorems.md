# Binary Trees Theorems

This article cover:
1. [Full Binary Tree](https://www.programiz.com/dsa/full-binary-tree)
2. [Perfect Binary Tree](https://www.programiz.com/dsa/perfect-binary-tree)

## Full Binary Tree

A full Binary tree is a special type of binary tree in which every parent node/internal node has either two or no children.

> It is also known as a **proper binary tree**.

![](./../assets/img/full-binary-tree_0.webp)

### Full Binary Tree Theorems

```
Let, i = the number of internal nodes
       n = be the total number of nodes
       l = number of leaves
       λ = number of levels
```

1. The number of leaves is `i + 1`.
2. The total number of nodes is `2i + 1`.
3. The number of internal nodes is `(n – 1) / 2`.
4. The number of leaves is `(n + 1) / 2`.
5. The total number of nodes is `2l – 1`.
6. The number of internal nodes is `l – 1`.
7. The number of leaves is at most $2^{(λ - 1)}$.

## Perfect Binary Tree

A perfect binary tree is a type of binary tree in which every internal node has exactly two child nodes and all the leaf nodes are at the same level.

![](./../assets/img/perfect-binary-tree_0.webp)

All the internal nodes have a degree of 2.

Recursively, a perfect binary tree can be defined as:

1. If a single node has no children, it is a perfect binary tree of height `h = 0`,
2. If a node has `h > 0`, it is a perfect binary tree if both of its subtrees are of height `h - 1` and are non-overlapping.

![](./../assets/img/perfect-binary-tree-rec.webp)

### Perfect Binary Tree Theorems

1. A perfect binary tree of height h has $2^{h + 1} – 1$ node.
2. A perfect binary tree with n nodes has height `log(n + 1) – 1 = Θ(ln(n))`.
3. A perfect binary tree of height h has $2^h$ leaf nodes.
4. The average depth of a node in a perfect binary tree is `Θ(ln(n))`.
