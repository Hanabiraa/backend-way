# Hash table

This article cover:
1. [Hash Table](https://www.programiz.com/dsa/hash-table)
2. [Hash Table in Data Structure: Python Example](https://www.guru99.com/hash-table-data-structure.html)

## Basic

The Hash table data structure stores elements in key-value pairs where

* **Key** - unique integer that is used for indexing the values
* **Value** - data that are associated with keys.
  
## Hashing (Hash Function)

In a hash table, a new index is processed using the keys. And, the element corresponding to that key is stored in the index. This process is called **hashing**.

Let:

* `k` - key
* `h(x)` - hash function for key `x`
  
Then hash func `h(k)` will give us a new index to store the element linked with `k`

![](./../assets/img/Hash-2_0.webp)

## Hash Collision

When the hash function generates the same index for multiple keys, there will be a conflict (what value to be stored in that index). This is called a **hash collision**.

We can resolve the hash collision using one of the following techniques.

* Collision resolution by **chaining**
* **(Probing) Open Addressing**: Linear/Quadratic Probing and Double Hashing Probing

## Chaining to avoid collision

> In chaining, if a hash function produces the same index for multiple elements, these elements are stored in the same index by using a doubly-linked list.

If `j` is the slot for multiple elements, it contains a pointer to the head of the list of elements. If no element is present, `j` contains `NIL`.

![](./../assets/img/Hash-3_1.webp)

### Benefits of chained lists

The following are the benefits of chained lists:

* Chained lists have better performance when inserting data because the order of insert is `O(1)`.
* It is not necessary to resize a hash table that uses a chained list.
* It can easily accommodate a large number of values as long as free space is available.

## Probing (Open address)

> The other technique that is used to resolve collision is probing. When using the probing method, if a collision occurs, we can simply move on and find an empty slot to store our value.

The following are the methods of probing:

1. Linear probing	

    Just like the name suggests, this method searches for empty slots linearly starting from the position where the collision occurred and moving forward. If the end of the list is reached and no empty slot is found. The probing starts at the beginning of the list.

    ```
    h(k, i) = (h′(k) + i) mod m

    where:
    i = {0, 1, ….}
    h'(k) is a new hash function
    m - size of hash table
    ```

2. Quadratic probing

    This method uses quadratic polynomial expressions to find the next available free slot.

    ```
    h(k, i) = (h′(k) + c1 * i + c2 * i^2) mod m

    where:
    c1 and c2 are positive auxiliary constants,
    i = {0, 1, ….}
    m - size of hash table
    ```

3. Double hashing

    If a collision occurs after applying a hash function h(k), then another hash function is calculated for finding the next slot.

    ```
    h(k, i) = (h1(k) + i * h2(k)) mod m

    where:
    h1, h2 - hash func
    i = {0, 1, ..}
    m - size of hash table
    ```

## Good hash function

A good hash function may not prevent the collisions completely however it can reduce the number of collisions.

Here, we will look into different methods to find a good hash function

1. Division Method

    If `k` is a key and `m` is the size of the hash table, the hash function `h()` is calculated as:

    ```
    h(k) = k mod m
    ```

2. Multiplication Method

    ```
    h(k) = ⌊m(kA mod 1)⌋

    where:
    1) A is any constant. The value of A lies between 0 and 1.
    But, an optimal choice will be ≈ (√5-1)/2 suggested by Knuth.
    1) kA mod 1 gives the fractional part kA
    2) m - size of hash table
    3) ⌊ ⌋ gives the floor value
    ```
3. Universal Hashing

    In Universal hashing, the hash function is chosen at random independent of keys.

## Advantages of hash tables
Here, are pros/benefits of using hash tables:
  
* Hash tables have high performance when looking up data, inserting, and deleting existing values.
* The time complexity for hash tables is constant regardless of the number of items in the table.
* They perform very well even when working with large datasets.
  
## Disadvantages of hash tables
Here, are cons of using hash tables:

* You cannot use a null value as a key.
* Collisions cannot be avoided when generating keys using. hash functions. Collisions occur when a key that is already in use is generated.
* If the hashing function has many collisions, this can lead to performance decrease.


## Applications of Hash Table

Hash tables are implemented where

* constant time lookup and insertion is required
* cryptographic applications
* indexing data is required
* databases
* associative arrays
* sets
* memory cache
