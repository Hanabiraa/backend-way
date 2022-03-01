# Stack and Queue and types of queue

This article cover:
1. [Linked list Data Structure](https://www.programiz.com/dsa/linked-list)
2. [Linked List Operations: Traverse, Insert and Delete](https://www.programiz.com/dsa/linked-list-operations)
3. [Types of Linked List - Singly linked, doubly linked and circular](https://www.programiz.com/dsa/linked-list-types)
4. [Doubly Linked List](https://www.programiz.com/dsa/doubly-linked-list)
5. [Circular Linked List](https://www.programiz.com/dsa/circular-linked-list)

## **Intro**

A linked list is a linear data structure that includes a series of connected nodes. Here, each node stores the data and the address of the next node. For example,

![](./assets/img/linked-list-concept.webp)

You have to start somewhere, so we give the address of the first node a special name called `HEAD`. Also, the last node in the linked list can be identified because its next portion points to `NULL`.

## **Simply Linked List**

Let's see how each node of the linked list is represented. Each node consists:

* A data 
* An address of another node

We wrap both the data item and the next node reference in a struct as:

```cpp
struct node
{
  int data;
  struct node *next;
};
```

The power of a linked list comes from the ability to break the chain and rejoin it. E.g. if you wanted to put an element 4 between 1 and 2, the steps would be:

* Create a new struct node and allocate memory to it.
* Add its data value as 4
* Point its next pointer to the struct node containing 2 as the data value
* Change the next pointer of "1" to the node we just created.

Doing something similar in an array would have required shifting the positions of all the subsequent elements.

### Linked List operations: 

There are various linked list operations that allow us to perform different actions on linked lists. For example, the insertion operation adds a new element to the linked list.

Here's a list of basic linked list operations:

* Traversal - access each element of the linked list
* Insertion - adds a new element to the linked list
* Deletion - removes the existing elements
* Search - find a node in the linked list
* Sort - sort the nodes of the linked list

### **Traverse** 

Displaying the contents of a linked list is very simple. We keep moving the temp node to the next one and display its contents.

When temp is `NULL`, we know that we have reached the end of the linked list so we get out of the while loop.

```cpp
struct node *temp = head;
printf("\n\nList elements are - \n");
while(temp != NULL) {
  printf("%d --->",temp->data);
  temp = temp->next;
}
```

The output of this program will be:

```
List elements are - 
1 --->2 --->3 --->
```

### **Insert**

You can add elements to either the beginning, middle or end of the linked list.

#### 1. Insert at the beginning
* Allocate memory for new node
* Store data
* Change next of new node to point to head
* Change head to point to recently created node

```cpp
struct node *newNode;
newNode = malloc(sizeof(struct node));
newNode->data = 4;
newNode->next = head;
head = newNode;
```

#### 2. Insert at the end

* Allocate memory for new node
* Store data
* Traverse to last node
* Change next of last node to recently created node

```cpp
struct node *newNode;
newNode = malloc(sizeof(struct node));
newNode->data = 4;
newNode->next = NULL;

struct node *temp = head;
while(temp->next != NULL){
  temp = temp->next;
}

temp->next = newNode;
```

#### 3. Insert at the Middle
* Allocate memory and store data for new node
* Traverse to node just before the required position of new node
* Change next pointers to include new node in between

```cpp
struct node *newNode;
newNode = malloc(sizeof(struct node));
newNode->data = 4;

struct node *temp = head;

for(int i=2; i < position; i++) {
  if(temp->next != NULL) {
    temp = temp->next;
  }
}
newNode->next = temp->next;
temp->next = newNode;
```

### **Delete**

You can delete either from the beginning, end or from a particular position.

#### 1. Delete from beginning
* Point head to the second node

```cpp
head = head->next;
```

>  **Remember**: in some languages, the garbage collector does not automatically remove nodes, so in addition to the usual pointer transfer, you also need to remove the structure (for example, with ordinary pointers in C++)

#### 2. Delete from end
* Traverse to second last element
* Change its next pointer to null

```cpp
struct node* temp = head;
while(temp->next->next!=NULL){
  temp = temp->next;
}
temp->next = NULL;
```

#### 3. Delete from middle

* Traverse to element before the element to be deleted
* Change next pointers to exclude the node from the chain

```cpp
for(int i=2; i< position; i++) {
  if(temp->next!=NULL) {
    temp = temp->next;
  }
}

temp->next = temp->next->next;
```

### **Search**

You can search an element on a linked list using a loop using the following steps. We are finding item on a linked list.

* Make `head` as the `current` node.
* Run a loop until the `current` node is `NULL` because the last element points to `NULL`.
* In each iteration, check if the key of the node is equal to `item`. If it the key matches the item, return `true` otherwise return `false`.

```cpp
// Search a node
bool searchNode(struct Node** head_ref, int key) {
  struct Node* current = *head_ref;

  while (current != NULL) {
    if (current->data == key) return true;
      current = current->next;
  }
  return false;
}
```

### **Sort**

MergeSort(headRef)
1) If the head is NULL or there is only one element in the Linked List 
    then return.
2) Else divide the linked list into two halves.  
      FrontBackSplit(head, &a, &b); /* a and b are two halves */
3) Sort the two halves a and b.
      MergeSort(a);
      MergeSort(b);
4) Merge the sorted a and b (using SortedMerge() discussed here) 
   and update the head pointer using headRef.
     *headRef = SortedMerge(a, b);

### Linked List Complexity


| Operations | Worst case | Average case |
| :--- | :---: | :---: | 
| Search | O(n) | O(n) | 
| Insert | O(1) | O(1) |
| Deletion | O(1) | O(1) |

Space Complexity: `O(n)`

### Linked List Applications

* Dynamic memory allocation
* Implemented in stack and queue
* In undo functionality of softwares
* Hash tables, Graphs

## **Doubly Linked List**

A doubly linked list is a type of linked list in which each node consists of 3 components:

* *prev - address of the previous node
* data - data item
* *next - address of next no

Here, the single node is represented as

```cpp
struct node {
    int data;
    struct node *next;
    struct node *prev;
}
```

Each struct node has a data item, a pointer to the previous struct node, and a pointer to the next struct node.

Double linked list view:
![](./assets/img/doubly-linked-list-created.webp)

### Doubly Linked List Complexity


| Operations | Worst case | Average case |
| :--- | :---: | :---: | 
| Insert | O(1) or O(n) | O(1) |
| Deletion | O(1) | O(1) |


1. Complexity of Insertion Operation

    The insertion operations that do not require traversal have the time complexity of O(1).
    And, insertion that requires traversal has time complexity of O(n).
    The space complexity is O(1).

2. Complexity of Deletion Operation

    All deletion operations run with time complexity of O(1).
    And, the space complexity is O(1).

### Doubly Linked List Applications
* Redo and undo functionality in software.
* Forward and backward navigation in browsers.
* For navigation systems where forward and backward navigation is required.

### Singly Linked List Vs Doubly Linked List

| **Singly Linked List** | **Doubly Linked List** |
| :--- | :--- |
| Each node consists of a data value and a pointer to the next node. | Each node consists of a data value, a pointer to the next node, and a pointer to the previous node. |
| Traversal can occur in one way only (forward direction). | Traversal can occur in both ways. |
| It requires less space. | It requires more space because of an extra pointer. |
| It can be implemented on the stack. | It has multiple usages. It can be implemented on the stack, heap, and binary tree. |

## **Circular Linked List**

A circular linked list is a type of linked list in which the first and the last nodes are also connected to each other to form a circle.

There are basically two types of circular linked list:

1. Circular Singly Linked List

Here, the address of the last node consists of the address of the first node.

![](./assets/img/circular-signle-linked-list.webp)


2. Circular Doubly Linked List

Here, in addition to the last node storing the address of the first node, the first node will also store the address of the last node.

![](./assets/img/circular-doubly-linked-list.webp)


> Note: We will be using the singly circular linked list to represent the working of circular linked list.

### Circular Linked List structure

Here, the single node is represented as

```cpp
struct Node {
    int data;
    struct Node * next;
};
```

Each struct node has a data item and a pointer to the next struct node.

### Circular Linked List Complexity

| Operations | Worst case | Average case |
| :--- | :---: | :---: | 
| Insert | O(1) or O(n) | O(1) |
| Deletion | O(1) | O(1) |


1. Complexity of Insertion Operation

    The insertion operations that do not require traversal have the time complexity of O(1).
    And, insertion that requires traversal has time complexity of O(n).
    The space complexity is O(1).

2. Complexity of Deletion Operation

    All deletion operations run with time complexity of O(1).
    And, the space complexity is O(1).
    
### Why Circular Linked List?

* The NULL assignment is not required because a node always points to another node.
* The starting point can be set to any node.
* Traversal from the first node to the last node is quick.

### Circular Linked List Applications
* It is used in multiplayer games to give a chance to each player to play the game.
* Multiple running applications can be placed in a circular linked list on an operating system. The os keeps on iterating over these applications.
* for circular playlist in music app