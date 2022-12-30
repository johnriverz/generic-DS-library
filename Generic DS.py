"""
Program: Data Structures
Author: Juan Rios
Date: 02/25/2022
Description: Implementations of Queues, Stacks, Priority Queues, BSTs, and RBTs.
"""

# --------------------------------------Exceptions-----------------------------------------------------------------------
class QueueCapacityTypeError(Exception):
    """Exception raised if Queue capacity is of the wrong type."""
    pass

class QueueCapacityBoundError(Exception):
    """Exception raised if Queue capacity is negative or zero."""
    pass

class StackCapacityTypeError(Exception):
    """Exception raised if Stack capacity is of the wrong type."""
    pass

class StackCapacityBoundError(Exception):
    """Exception raised if Stack capacity is negative or zero."""
    pass

class QueueIsFull(Exception):
    """Exception raised if the queue is full."""
    pass

class QueueIsEmpty(Exception):
    """Exception raised if the queue is empty."""
    pass

class StackIsFull(Exception):
    """Exception raised if push method is called when the stack is full."""
    pass

class StackIsEmpty(Exception):
    """Exception raised if pop method is called when the stack is empty."""
    pass

class PQInvalidPriority(Exception):
    """Exception raised if passing invalid priority into a priority queue."""
    pass

class PQItemTypeError(Exception):
    """Exception raised if item is of wrong type."""
    pass

class TreeIsEmpty(Exception):
    """Exception raised if tree is empty."""
    pass

# --------------------------------------Helper Methods-------------------------------------------------------------------

# --------------------------------------AUX Classes----------------------------------------------------------------------
class Node:
    """ Description: The Node class. Creates a linked list
        node to store values of a queue/stack.
        """

    def __init__(self, data):
        self.data = data
        self.next = None

class BSTNode():
    """ This class implements a node for the BST. """
    def __init__(self, item):
        """
        Description: The constructor for the Node class.
        Usage: node = BSTNode(item)
               item == (<int>, <value>)
        """
        self._parent = None
        self._lChild = None
        self._rChild = None
        self._value = item
        self._key = item[0]

    def __str__(self):
        """ Returns a string rep of the node (for debugging ^,^) """
        returnValue = "Node: {}\n".format(self._key)
        returnValue += "Parent: {}\n".format(self._parent._key)
        returnValue += "Left Child: {}\n".format(self._lChild._key)
        returnValue += "Right Child: {}\n".format(self._rChild._key)
        return returnValue

    #Accessor Methods
    def getParent(self):
        """
        Description: Accessor method for the Node. Returns parent.
        Usage: <node>.getParent()
        """
        return self._parent
    def getRChild(self):
        """
        Description: Accessor method for the Node. Returns right child.
        Usage: <node>.getRChild()
        """
        return self._rChild
    def getLChild(self):
        """
        Description: Accessor method for the Node. Returns left child.
        Usage: <node>.getLChild()
        """
        return self._lChild
    def getValue(self):
        """
        Description: Accessor method for the Node. Returns the item.
        Usage: <node>.getValue()
        """
        return self._value
    # Mutator methods
    def setParent(self, node):
        """
        Description: Mutator method. Sets the parent reference.
        Usage: <node>.setParent(<BSTNode>)
        """
        self._parent = node
    def setLChild(self, node):
        """
        Description: Mutator method. Sets the lchild reference.
        Usage: <node>.setLChild(<BSTNode>)
        """
        self._lChild = node
    def setRChild(self, node):
        """
        Description: Mutator method. Sets the rchild reference.
        Usage: <node>.setRChild(<BSTNode>)
        """
        self._rChild = node

    #comparison operators
    def __gt__(self, other):
        """
        Description: Overloads the > operator to allow direct comparison of
                     nodes.
        Usage: node1 > node2
        """
        returnValue = False
        if(other != None):
            returnValue = self._key > other._key
        return returnValue
    def __lt__(self, other):
        """
        Description: Overloads the < operator to allow direct comparison of
                     nodes.
        Usage: node1 < node2
        """
        returnValue = False
        if(other != None):
            returnValue = self._key < other._key
        return returnValue
    def __eq__(self, other):
        """
        Description: Overloads the == operator to allow direct comparison of
                     nodes.
        Usage: node1 == node2
        """
        returnValue = False
        if(other != None):
            returnValue = self._key == other._key
        return returnValue
    def __ne__(self, other):
        """
        Description: Overloads the != operator to allow direct comparison of
                     nodes.
        Usage: node1 != node2
        """
        returnValue = False
        if(other != None):
            returnValue = self._key != other._key
        if(other == None):
            returnValue = True
        return returnValue
    def __le__(self, other):
        """
        Description: Overloads the <= operator to allow direct comparison of
                     nodes.
        Usage: node1 <= node2
        """
        returnValue = False
        if(other != None):
            returnValue = self._key <= other._key
        return returnValue
    def __ge__(self, other):
        """
        Description: Overloads the >= operator to allow direct comparison of
                     nodes.
        Usage:  node1 >= node2
        Input: Another instance of the node class.
        """
        returnValue = False
        if(other != None):
            returnValue = self._key >= other._key
        return returnValue

    #Some helper methods to make things easy in the BST
    def hasLeftChild(self):
        """
        Description: This method returns true if the current node
                     has a left child.
        Usage: <node>.hasLeftChild()
        """
        returnValue = False
        if(type(self._lChild) == BSTNode and self._lChild._parent is self):
            returnValue = True
        return returnValue
    def hasRightChild(self):
        """
        Description: This method returns true|false depending on if the current
                     node has a right child or not.
        Usage: <node>.hasRightChild()
        """
        returnValue = False
        if(type(self._rChild) == BSTNode and self._rChild._parent is self):
            returnValue = True
        return returnValue
    def hasOnlyOneChild(self):
        """
        Description: Returns True if the current node has only one child.
        Usage: <node>.hasOnlyOneChild()
        """
        LC = self.hasLeftChild()
        RC = self.hasRightChild()
        return (LC and not RC) or (not LC and RC)
    def hasBothChildren(self):
        """
        Description: Returns True if the current node has both children
        Usage: <node>.hasBothChildren()
        """
        return self.hasLeftChild() and self.hasRightChild()
    def isLeaf(self):
        """
        Description: Returns true if the current node is a leaf node.
        Usage: <node>.isLeaf()
        """
        returnValue = False
        if(self._rChild == None and self._lChild == None):
            returnValue = True
        return returnValue
    def isLeftChild(self):
        """
        Description: Returns true if the current node is a left child
        Usage: <node>.isLeftChild()
        """
        returnValue = False
        if(self._parent != None):
            if(self._parent._lChild is self):
                if(self._parent._rChild is not self):
                    returnValue = True
        return returnValue
    def isRightChild(self):
        """
        Description: Returns true if the current node is a right child
        Usage: <node>.isRightChild()
        """
        returnValue = False
        if(self._parent != None):
            if(self._parent._rChild is self):
                if(self._parent._lChild is not self):
                    returnValue = True
        return returnValue

class RBNode():
    """ This class implements a node for the RBT."""
    def __init__(self, item):
        """
        Description: The constructor for the RBNode class. Default color is red.
        Usage: node = RBNode(item)
               item == (<int>, <value>)
        """
        self._parent = None
        self._lChild = None
        self._rChild = None
        self.color = True
        self._value = item
        self._key = item[0]
    def __str__(self):
        """ Returns a string rep of the node (for debugging ^,^) """
        color = "red" if(self.color) else "black"
        returnValue = f"Node: ({self._key}, {color})\n"
        returnValue += f"Parent: {self._parent._key if(self._parent != None) else self._parent}\n"
        returnValue += f"Left Child: {self._lChild._key if( self._lChild != None) else self._lChild}\n"
        returnValue += f"Right Child: {self._rChild._key if(self._rChild != None) else self._rChild}\n"
        return returnValue
    #Accessor Methods
    def getParent(self):
        """
        Description: Accessor method for the Node. Returns parent.
        Usage: <node>.getParent()
        """
        return self._parent
    def getRChild(self):
        """
        Description: Accessor method for the Node. Returns right child.
        Usage: <node>.getRChild()
        """
        return self._rChild
    def getLChild(self):
        """
        Description: Accessor method for the Node. Returns left child.
        Usage: <node>.getLChild()
        """
        return self._lChild
    def getValue(self):
        """
        Description: Accessor method for the Node. Returns the item.
        Usage: <node>.getValue()
        """
        return self._value
    def getKey(self):
        """
        Description: Accessor method for the Node. Returns the key.
        Usage: <node>.getKey()
        """
        return self._key
    def getColor(self):
        """
        Description: Accessor method for the Node. Returns the color.
        Usage: <node>.getColor()
        """
        return self.color
    # Mutator methods
    def setParent(self, node):
        """
        Description: Mutator method. Sets the parent reference.
        Usage: <node>.setParent(<RBNode>)
        """
        self._parent = node
    def setLChild(self, node):
        """
        Description: Mutator method. Sets the lchild reference.
        Usage: <node>.setLChild(<RBNode>)
        """
        self._lChild = node
    def setRChild(self, node):
        """
        Description: Mutator method. Sets the rchild reference.
        Usage: <node>.setRChild(<RBNode>)
        """
        self._rChild = node
    def setValue(self, value):
        """
        Description: Mutator method. Sets the value reference.
        Usage: <node>.setValue(<tuple>)
        """
        self._value = value
    def setKey(self, key):
        """
        Description: Mutator method. Sets the key reference.
        Usage: <node>.setKey(<int>)
        """
        self._key = key
    def setRed(self):
        """
        Description: Sets the color of the node to red.
        Usage: <node>.setRed()
        """
        self.color = True
    def setBlack(self):
        """
        Description: Sets the color of the node to black.
        Usage: <node>.setBlack()
        """
        self.color = False
    #comparison operators
    def __gt__(self, other):
        """
        Description: Overloads the > operator to allow direct comparison of
                     nodes.
        Usage: node1 > node2
        """
        returnValue = False
        if(other != None):
            returnValue = self._key > other._key
        return returnValue
    def __lt__(self, other):
        """
        Description: Overloads the < operator to allow direct comparison of
                     nodes.
        Usage: node1 < node2
        """
        returnValue = False
        if(other != None):
            returnValue = self._key < other._key
        return returnValue
    def __eq__(self, other):
        """
        Description: Overloads the == operator to allow direct comparison of
                     nodes.
        Usage: node1 == node2
        """
        returnValue = False
        if(other != None):
            returnValue = self._key == other._key
        return returnValue
    def __ne__(self, other):
        """
        Description: Overloads the != operator to allow direct comparison of
                     nodes.
        Usage: node1 != node2
        """
        returnValue = False
        if(other != None):
            returnValue = self._key != other._key
        if(other == None):
            returnValue = True
        return returnValue
    def __le__(self, other):
        """
        Description: Overloads the <= operator to allow direct comparison of
                     nodes.
        Usage: node1 <= node2
        """
        returnValue = False
        if(other != None):
            returnValue = self._key <= other._key
        return returnValue
    def __ge__(self, other):
        """
        Description: Overloads the >= operator to allow direct comparison of
                     nodes.
        Usage:  node1 >= node2
        Input: Another instance of the node class.
        """
        returnValue = False
        if(other != None):
            returnValue = self._key >= other._key
        return returnValue
    #Some helper methods to make things easy in the BST
    def hasLeftChild(self):
        """
        Description: This method returns true if the current node
                     has a left child.
        Usage: <node>.hasLeftChild()
        """
        returnValue = False
        if(type(self._lChild) == RBNode and self._lChild._parent is self):
            returnValue = True
        return returnValue
    def hasRightChild(self):
        """
        Description: This method returns true|false depending on if the current
                     node has a right child or not.
        Usage: <node>.hasRightChild()
        """
        returnValue = False
        if(type(self._rChild) == RBNode and self._rChild._parent is self):
            returnValue = True
        return returnValue
    def hasOnlyOneChild(self):
        """
        Description: Returns True if the current node has only one child.
        Usage: <node>.hasOnlyOneChild()
        """
        LC = self.hasLeftChild()
        RC = self.hasRightChild()
        return (LC and not RC) or (not LC and RC)
    def hasBothChildren(self):
        """
        Description: Returns True if the current node has both children
        Usage: <node>.hasBothChildren()
        """
        return self.hasLeftChild() and self.hasRightChild()
    def isLeaf(self):
        """
        Description: Returns true if the current node is a leaf node.
        Usage: <node>.isLeaf()
        """
        returnValue = False
        if(self._rChild == None and self._lChild == None):
            returnValue = True
        return returnValue
    def isLeftChild(self):
        """
        Description: Returns true if the current node is a left child
        Usage: <node>.isLeftChild:wq
        ()
        """
        returnValue = False
        if(self._parent != None):
            if(self._parent._lChild is self):
                if(self._parent._rChild is not self):
                    returnValue = True
        return returnValue
    def isRightChild(self):
        """
        Description: Returns true if the current node is a right child
        Usage: <node>.isRightChild()
        """
        returnValue = False
        if(self._parent != None):
            if(self._parent._rChild is self):
                if(self._parent._lChild is not self):
                    returnValue = True
        return returnValue
    def isRed(self):
        """
        Description: Returns True if this node is red.
        Usage: <node>.isRed()
        """
        return self.color == True
    def isBlack(self):
        """
        Description: Returns True if this node is black.
        Usage: <node>.isBlack()
        """
        return self.color == False

# --------------------------------------Data Structures------------------------------------------------------------------
class Stack:
    """ Description: The Stack class.
    """

    def __init__(self, capacity):
        """ Description: The constructor for the Stack class.
            Parameters:
                       1. capacity (total number of items that can be fit into the stack)
                """
        if (type(capacity) != int):
            raise StackCapacityTypeError("ERROR: capacity must be of type int.")

        if (capacity == 0) or (capacity < 0):
            raise StackCapacityBoundError("ERROR: capacity cannot be negative or zero.")

        self.head = None
        self.capacity = capacity
        self.currentSize = 0

    def push(self, item):
        """ Description: Adds an item to the stack.
            Usage: S = Stack(2)
                   S.push(1)
            Return: True/False depending
                 on if the push was successful or not.
                """
        if self.isFull():
            raise StackIsFull("Cannot push on a full stack.")

        elem = Node(item)
        elem.next = None

        if self.head == None:
            self.head = elem
        else:
            elem.next = self.head
            self.head = elem
        self.currentSize += 1
        return True

    def pop(self):
        """ Description: Removes an item from the stack.
            Usage: S = Stack(2)
                   S.push(1)
                   S.push(5)
                   S.pop()
            Return: Returns removed item if stack not empty.
                """
        if self.isEmpty():
            raise StackIsEmpty("Cannot pop on an empty stack.")

        elem = self.head
        self.head = self.head.next
        elem.next = None
        self.currentSize -= 1
        return elem.data

    def peek(self):
        """ Description: Allows user to peak at item at the front of the
                         stack without deleting it.
            Usage: S.peek()
            Return: Returns item at the front of the stack.
                    If the stack is empty, it returns False.
                """
        if self.isEmpty():
            return False

        return self.head.data

    def isEmpty(self):
        """ Description: Checks if stack is empty.
            Usage: S.isEmpty()
            Return: Returns True if stack is empty, returns
                    False if not empty.
                """
        return self.head == None

    def isFull(self):
        """ Description: Checks if stack is full.
            Usage: S.isFull()
            Return: Returns True if stack is full, returns
                    False if not full.
                """
        return self.currentSize == self.capacity

class Queue:
    """ Description: The Queue class. Creates a linked list
            node to store values of a queue.
            """

    def __init__(self, capacity):
        """ Description: The constructor for the Queue class.
            Parameters:
                       1. capacity (total number of items that can be fit into the queue)
                """
        if (type(capacity) != int):
            raise QueueCapacityTypeError("ERROR: capacity must be of type int.")

        if (capacity == 0) or (capacity < 0):
            raise QueueCapacityBoundError("ERROR: capacity cannot be negative or zero.")

        self.head = None
        self.tail = None
        self.capacity = capacity
        self.currentSize = 0

    def enqueue(self, item):
        """ Description: Adds an item to the queue.
            Usage: Q = Queue(10)
                   Q.enqueue(1)
            Return: True/False depending
                 on if the enqueue was successful or not.
                """
        if self.isFull():
            raise QueueIsFull("Cannot enqueue on a full queue.")

        elem = Node(item)
        elem.next = None

        if self.tail == None:
            self.head = self.tail = elem
        else:
            self.tail.next = elem
            self.tail = self.tail.next
        self.currentSize += 1
        return True

    def dequeue(self):
        """ Description: Removes an item from the queue.
            Usage:
                Q = Queue(10)
                Q.enqueue(1)
                Q.enqueue(2)
                Q.dequeue()
            Return: Returns removed item if queue not empty.
                """
        result = self.head.data
        if self.isEmpty():
            raise QueueIsEmpty("Cannot dequeue on an empty queue.")
        if (self.currentSize == 1):
            self.head = self.tail = None
        else:
            elem = self.head
            self.head = self.head.next
            elem.next = None
        self.currentSize -= 1
        return result

    def front(self):
        """ Description: Allows user to peak at item at the front of the
                         queue without deleting it.
            Usage: Q.front()
            Return: Returns item at the front of the queue.
                    If the queue is empty, it returns False.
                """
        if self.isEmpty():
            return False

        return self.head.data

    def isEmpty(self):
        """ Description: Checks if queue is empty.
            Usage: Q.isEmpty()
            Return: Returns True if queue is empty, returns
                    False if not empty.
                """
        return self.head == None

    def isFull(self):
        """ Description: Checks if queue is full.
            Usage: Q.isFull()
            Return: Returns True if queue is full, returns
                    False if not full.
                """
        return self.currentSize == self.capacity


class PriorityQueue:
    """ Description: The Max-Heap Priority Queue class.
    """

    def __init__(self, capacity):
        """ Description: The constructor for the Max-Heap Priority Queue class.
            Parameters:
                       1. capacity (total number of items that can be fit into the queue)
        """
        if (type(capacity) != int):
            raise QueueCapacityTypeError("ERROR: capacity must be of type int.")

        if (capacity == 0) or (capacity < 0):
            raise QueueCapacityBoundError("ERROR: capacity cannot be negative or zero.")

        self._heap = []
        self.capacity = capacity
        self.currentSize = 0

    def __str__(self):
        """ Description: The string method.
            Format: [(<prio1>, <item>), (prio2, item), ...]” or “[]” if the queue is
                    empty.
            Return: Returns string representation of heap.
        """
        return f'{self._heap}'

    def insert(self, item):
        """ Description: This method will add a tuple to the queue based on its
                        priority.
            Usage: T1 = (11, "e")
                   PQ.insert(T1)
            Return: Returns True upon successfully adding tuple to the heap.
        """
        if (self.isFull()):
            raise QueueIsFull("Cannot insert on a full queue.")
        if(type(item) != tuple):
            raise PQItemTypeError("Inserted item must be a tuple.")
        if(item[0] == 0 or item[0] < 0):
            raise PQInvalidPriority("Priority must be a positive integer (0, inf].")

        self._heap.append(item)
        self.currentSize += 1
        self._increaseKey(self.currentSize - 1)
        return True

    def extractMax(self):
        """ Description: This method will remove and return the tuple with the
                        highest priority.
            Usage: PQ.extractMax()
            Return: Tuple with the highest priority.
        """
        if self.isEmpty():
            raise QueueIsEmpty("Cannot call extractMax on an empty queue.")

        max = self._heap[0]
        self._heap[0] = self._heap.pop()
        self.currentSize -= 1
        self._maxHeapify(0)
        return max

    def peekMax(self):
        """ Description: This method will return the tuple with the highest priority if
                        the queue is not empty.
            Usage: PQ.peekMax()
            Return: False if queue is empty.
        """
        if (self.isEmpty()):
            ret = False
        else:
            ret = self._heap[0]
        return ret

    def isEmpty(self):
        """ Description: Checks if queue is empty.
            Usage: PQ.isEmpty()
            Return: Returns True if queue is empty, returns
                    False if not empty.
        """
        return self.currentSize == 0

    def isFull(self):
        """ Description: Checks if queue is full.
            Usage: PQ.isFull()
            Return: Returns True if queue is full, returns
                    False if not full.
        """
        return self.currentSize == self.capacity

    def _maxHeapify(self, index):
        """ Description: Restructures the heap to maintain heap property.
            Usage: PQ._maxHeapify(0)
            Return:
        """
        l = self._getLeftChild(index)
        r = self._getRightChild(index)

        while (l < self.currentSize):
            largest = l
            if (r > l):
                largest = r
            if (self._heap[index] < self._heap[largest]):
                self._swap(index, largest)
            else:
                break
            index = largest

    def _swap(self, index1, index2):
        """ Description: Swaps tuple at index1 with tuple at index2.
            Usage: PQ._swap(parentIndex, childIndex)
            Return:
        """
        temp = self._heap[index1]
        self._heap[index1] = self._heap[index2]
        self._heap[index2] = temp

    def _getParent(self, index):
        """ Description: Gets parent tuple index.
            Usage: PQ._getParent()
            Return: Parent's index
        """
        return (index - 1) // 2

    def _getLeftChild(self, index):
        """ Description: Gets left child tuple index.
            Usage: PQ._getLeftChild()
            Return: Left child's index
        """
        return 2 * index + 1

    def _getRightChild(self, index):
        """ Description: Gets right child tuple index.
            Usage: PQ._getRightChild()
            Return: Right child's index
        """
        return 2 * index + 2

    def _hasParent(self, index):
        """ Description: Checks for a parent.
            Usage: PQ._hasParent()
            Return: True if tuple has a parent, false otherwise
        """
        return self._getParent(index) >= 0

    def _increaseKey(self, index):
        """ Description: Sift values up into correct position in tree.
            Usage: PQ._increaseKey(0)
            Return:
        """
        while (self._hasParent(index) and self._heap[self._getParent(index)] < self._heap[index]):
            self._swap(index, self._getParent(index))
            index = self._getParent(index)

class BinarySearchTree:
    """
    Description: A Binary Search Tree (BST).
    Note: Algorithms for the BST can be found in ch. 12 of the book.
    """
    def __init__(self):
        """ The constructor for our BST """
        self._root = None
        #Add any other instance variables you need.

    def _isValid(self, item):
        """
        Description: Checks to see if a tuple is valid
        Usage: (outside) BST.isValid(item) (inside) self.isValid(item)
        """
        returnValue = True
        if(type(item) != tuple):
            returnValue = False
        elif(type(item[0]) != int):
            returnValue = False
        elif(len(item) != 2):
            returnValue = False
        return returnValue

    def _transplantR(self, cNode):
        """
        Description: This transplant attaches the currentNodes right child
                     to the current nodes parent.
        Notes:
                1. Do not call this method when cNode is the root.
                2. Don't forget to handle the cNodes references in your func.
        """
        parent = cNode.getParent()
        child = cNode.getRChild()
        if(cNode.isLeftChild()):
            parent.setLChild(child)
            child.setParent(parent)
        else:
            parent.setRChild(child)
            child.setParent(parent)

    def _transplantL(self, cNode):
        """
        Description: This transplant attaches the currentNodes right child
                     to the current nodes parent.
        Notes:
                1. Do not call this method when cNode is the root.
                2. Don't forget to handle the cNodes references in your func.
        """
        parent = cNode.getParent()
        child = cNode.getLChild()
        if(cNode.isLeftChild()):
            parent.setLChild(child)
            child.setParent(parent)
        else:
            parent.setRChild(child)
            child.setParent(parent)

    def traverse(self, mode):
        """
        Description: The traverse method returns a string rep
                     of the tree according to the specified mode
        """
        self.output = ""
        if(type(mode) == str):
            if(mode == "in-order"):
                self.inorder(self._root)
            elif(mode == "pre-order"):
                self.preorder(self._root)
            elif(mode == "post-order"):
                self.postorder(self._root)
        else:
            self.output = "ERROR: Unrecognized mode..."
        return self.output[:-2]

    def inorder(self, node):
        """ computes the inorder traversal """
        if(node != None):
            self.inorder(node.getLChild())
            self.output += str(node._key) + ", "
            self.inorder(node.getRChild())

    def preorder(self, node):
        """computes the pre-order traversal"""
        if(node != None):
            self.output += str(node._key) + ", "
            self.preorder(node.getLChild())
            self.preorder(node.getRChild())

    def postorder(self, node):
        """ compute postorder traversal"""
        if(node != None):
            self.postorder(node.getLChild())
            self.postorder(node.getRChild())
            self.output += str(node._key) + ", "

    def insert(self, item):
        """ Description: This method will insert a new item into the tree.
            Usage: BST.insert((1, a))
            Return: True or False depending on if the insert was successful.
        """
        if (self._isValid(item) != True):
            return False

        y = None
        x = self._root
        z = BSTNode(item)

        while x != None:
            y = x
            if (z._key < x._key):
                x = x._lChild
            else:
                x = x._rChild

        z._parent = y
        if (y == None):
            self._root = z
        elif (z._key < y._key):
            y._lChild = z
            z._parent = y
        else:
            y._rChild = z
            z._parent = y

        return True

    def delete(self, id):
        """ Description: This method will delete a node from the tree.
            Usage: BST.delete(1)
            Return: True or False depending on if the deletion was successful.
        """
        if self._isEmpty():
            raise TreeIsEmpty("Cannot call delete on an empty tree.")

        node = self._findNode(id)

        if (node is False):
            return False

        if (node._lChild == None):
            self._transplant(node, node._rChild)
            node._rChild = None
            node._parent = None
        elif (node._rChild == None):
            self._transplant(node, node._lChild)
            node._lChild = None
            node._parent = None
        else:
            y = self._minNode(node._rChild)
            if (y._parent != node):
                self._transplant(y, y._rChild)
                y._rChild = node._rChild
                y._rChild._parent = y
            self._transplant(node, y)
            y._lChild = node._lChild
            y._lChild._parent = y
            node._parent = None
            node._rChild = None
            node._lChild = None
        return True

    def find(self, id):
        """ Description: This method takes an int id and returns the tuple in the tree whose
                         ID matches that value.
            Usage: BST.find(1)
            Return: The tuple or False if it is not found in the tree.
        """
        if self._isEmpty():
            raise TreeIsEmpty("Cannot call find on an empty tree.")

        value = self._findNode(id)
        if (value is False):
            return False
        return value._value

    def _findNode(self, id):
        """ Description: This method takes an int id and returns the node in the tree whose
                         ID matches that value.
            Usage: BST._findNode(1)
            Return: The node or False if it is not found in the tree.
        """
        value = False
        x = self._root

        while (x != None and id != x._key):
            if id < x._key:
                x = x._lChild
            else:
                x = x._rChild

        if (x != None):
            value = x

        return value

    def _minNode(self, node):
        """ Description: Finds the minimum element in the subtree at node.
            Usage: BST._minNode(self._rChild)
            Return: Minimum node
        """
        while (node._lChild != None):
            node = node._lChild
        return node

    def _isEmpty(self):
        """ Description: Checks if tree is empty.
            Usage: BST._isEmpty()
            Return: True if tree is empty, False otherwise.
        """
        return self._root == None

    def _transplant(self, u, v):
        """ Description: Replaces one subtree as a child of its parent with another subtree.
            Usage: BST._transplant(node1, node2)
            Return:
        """
        if (u._parent == None):
            self._root = v
        elif (u == u._parent._lChild):
            u._parent._lChild = v
        else:
            u._parent._rChild = v

        if (v != None):
            v._parent = u._parent

class RedBlackTree:
    """
    Description: A Red-Black Tree (RBT).
    """
    def __init__(self):
        """ The constructor for our RBT """
        self._root = None
        #Add any other instance variables you need.

    def _isValid(self, item):
        """
        Description: Checks to see if a tuple is valid
        Usage: (outside) <RBT>._isValid(item) (inside) self._isValid(item)
        """
        returnValue = True
        if(type(item) != tuple):
            returnValue = False
        elif(type(item[0]) != int):
            returnValue = False
        elif(len(item) != 2):
            returnValue = False
        return returnValue

    def _isRoot(self, node):
        """
        Description: This function returns true if the given node is the root.
        Usage: self._isRoot(node)
        """
        return node is self._root

    def _isEmpty(self):
        """
        Description: This method returns true if the tree is empty, else False.
        """
        return self._root == None

    def _rbTransplant(self, u, v):
        """
        Description: A pretty straightforward implementation of RB-Transplant from
        ch. 12 pg. 323 of the book.
        """
        if(u._parent == None):
            self._root = v
        elif(u.isLeftChild()):
            u.getParent().setLChild(v)
        else:
            u.getParent().setRChild(v)
        if(v != None):
            v.setParent(u.getParent())

    def traverse(self, mode):
        """
        Description: The traverse method returns a string rep
                     of the tree according to the specified mode
        """
        self.output = ""
        if(type(mode) == str):
            if(mode == "in-order"):
                self.inorder(self._root)
            elif(mode == "pre-order"):
                self.preorder(self._root)
            elif(mode == "post-order"):
                self.postorder(self._root)
        else:
            self.output = "ERROR: Unrecognized mode..."
        return self.output[:-2]

    def inorder(self, node):
        """ computes the inorder traversal """
        if(node != None):
            self.inorder(node.getLChild())
            color = "red" if(node.color) else "black"
            self.output += f"({node.getKey()}, {color}), "
            self.inorder(node.getRChild())

    def preorder(self, node):
        """computes the pre-order traversal"""
        if(node != None):
            color = "red" if(node.color) else "black"
            self.output += f"({node.getKey()}, {color}), "
            self.preorder(node.getLChild())
            self.preorder(node.getRChild())

    def postorder(self, node):
        """ compute postorder traversal"""
        if(node != None):
            self.postorder(node.getLChild())
            self.postorder(node.getRChild())
            color = "red" if(node.color) else "black"
            self.output += f"({node.getKey()}, {color}), "

    def _findMinimum(self, node):
        """
        Description: Finds the successor of the current node and returns it.
        Usage: self._findMinimum(<RBNode>)
        """
        min = node
        while(min.hasLeftChild()):
            min = min.getLChild()
        return min

    def _findNode(self, id):
        """
        Description: Finds node in tree with given id,
                     returns corresponding ticket. Returns False if unsuccessful.
        """
        currentNode = self._root
        if(type(id) == int):
            while(currentNode != None and currentNode.getKey() != id):
                if(id < currentNode._key):
                    currentNode = currentNode.getLChild()
                else:
                    currentNode = currentNode.getRChild()
        return currentNode if(currentNode != None) else False

    def insert(self, item):
        """
        Description: Inserts given tuple into the tree while
                     preserving binary tree property.
                     Returns True if successful, False otherwise
                     See ch. 12 pg. 315 of the book
        """
        ret = False
        if self._isValid(item):
            z = RBNode(item)
            ret = True
            y = None
            x = self._root
            while(x != None):
                y = x
                if(z < x):
                    x = x.getLChild()
                else:
                    x = x.getRChild()
            z.setParent(y)
            if y == None:
                self._root = z
            elif(z < y):
                y.setLChild(z)
            else:
                y.setRChild(z)
            z.setLChild(None)
            z.setRChild(None)
            z.setRed()
            self._insertFixup(z)
        return ret

    def delete(self, id):
        """
        Description: Deletes node from tree with given ticketID;
                     restructures binary tree. Returns True if successful,
                     False otherwise. See CH. 12 page 324 of the book.
        """
        ret = False
        if(self._isEmpty()):
            raise TreeIsEmpty("ERROR: Cannot delete from an empty tree.\n")
        elif(type(id) == int):
            z = self._findNode(id)
            if(type(z) == RBNode):
                ret = True
                y = z
                y_original_color = y.getColor()
                if(not z.hasLeftChild()):
                    x = z.getRChild()
                    self._rbTransplant(z, z.getRChild())
                elif(not z.hasRightChild()):
                    x = z.getLChild()
                    self._rbTransplant(z, z.getLChild())
                else:
                    y = self._findMinimum(z.getRChild())
                    y_original_color = y.getColor()
                    x = y.getRChild()
                    if(y.getParent() is z):
                        if(x != None):
                            x.setParent(y)
                    else:
                        self._rbTransplant(y, y.getRChild())
                        y.setRChild(z.getRChild())
                        y.getRChild().setParent(y)
                    self._rbTransplant(z, y)
                    y.setLChild(z.getLChild())
                    y.getLChild().setParent(y)
                    y.color = z.color
                if(y_original_color == False):
                    self._deleteFixup(x)
                z.setParent(None)
                z.setRChild(None)
                z.setLChild(None)
        return ret

    def find(self, id):
        """
        Description: Finds node in tree with given id,
                     returns corresponding ticket. Returns False if unsuccessful.
        """
        ret = False
        if(self._root == None):
            raise TreeIsEmpty("ERROR: Cannot find any nodes in an empty tree.\n")
        if(type(id) == int):
            result = self._findNode(id)
            if(type(result) == RBNode):
                ret = result.getValue()
        return ret

    def _insertFixup(self, currentNode):
        """ Description: Balances tree after inserting.
            Usage: self._insertFixup(currentNode)
            Return:
        """
        parent = currentNode.getParent()

        while (parent != None and (parent.isRed() and currentNode.isRed())):
            parent = currentNode.getParent()
            gg = parent.getParent()
            if (parent.isLeftChild()):
                unc = gg.getRChild()
                if (unc != None and unc.isRed()):
                    parent.setBlack()
                    unc.setBlack()
                    gg.setRed()
                    currentNode = gg
                else:
                    if(currentNode.isRightChild()):
                        currentNode = parent
                        parent = currentNode.getParent()
                        gg = parent.getParent()
                        self._leftRotate(currentNode)
                    parent.setBlack()
                    gg.setRed()
                    self._rightRotate(gg)
            else:
                if (parent.isRightChild()):
                    unc = gg.getLChild()
                    if (unc != None and unc.isRed()):
                        parent.setBlack()
                        unc.setBlack()
                        gg.setRed()
                        currentNode = gg
                    else:
                        if (currentNode.isLeftChild()):
                            currentNode = parent
                            parent = currentNode.getParent()
                            gg = parent.getParent()
                            self._rightRotate(currentNode)
                        parent.setBlack()
                        gg.setRed()
                        self._leftRotate(gg)
        self._root.setBlack()

    def _deleteFixup(self, currentNode):
        """ Description: Receives a node and fixes up the tree, balancing from that node.
            Usage: self._deleteFixup(currentNode)
            Return:
        """
        parent = currentNode.getParent()
        while (currentNode != self._root and currentNode.isBlack()):
            if (currentNode.isLeftChild()):
                w = parent.getRChild()
                wRChild =w.getRChild()
                wLChild = w.getLChild()
                if (w.isRed()):
                    w.setBlack()
                    parent.setRed()
                    self._leftRotate(parent)
                    w = parent.getRChild()
                if (wLChild.isBlack() and wRChild.isBlack()):
                    w.setRed()
                    currentNode = parent
                else:
                    if (wRChild.isBlack()):
                        wLChild.setBlack()
                        w.setRed()
                        self._rightRotate(w)
                        w = parent.getRChild()
                    w.color = parent.getColor()
                    parent.setBlack()
                    wRChild.setBlack()
                    self._leftRotate(parent)
                    currentNode = self._root
            else:
                w = parent.getLChild()
                wRChild = w.getRChild()
                wLChild = w.getLChild()
                if (w.isRed()):
                    w.setBlack()
                    parent.setRed()
                    self._rightRotate(parent)
                    w = parent.getLChild()
                if (wLChild.isBlack() and wRChild.isBlack()):
                    w.setRed()
                    currentNode = parent
                else:
                    if (wLChild.isBlack()):
                        wRChild.setBlack()
                        w.setRed()
                        self._leftRotate(w)
                        w = parent.getLChild()
                    w.color = parent.getColor()
                    parent.setBlack()
                    wLChild.setBlack()
                    self._rightRotate(parent)
                    currentNode = self._root
        currentNode.setBlack()

    def _leftRotate(self, currentNode):
        """ Description: perform a left rotation from a given node.
            Usage: self._leftRotate(currentNode)
            Return:
        """
        parent = currentNode.getParent()
        rChild = currentNode.getRChild()  # y from book pseudocode
        gLChild = rChild.getLChild()  # x.right from pseudocode

        currentNode.setRChild(gLChild) #turn y’s left subtree into x’s right subtree
        if gLChild != None:
            gLChild.setParent(currentNode)
        rChild.setParent(parent) #link x's parent to y
        if parent == None:
            self._root = rChild
        elif currentNode.isLeftChild():
            parent.setLChild(rChild)
        else:
            parent.setRChild(rChild)
        rChild.setLChild(currentNode)
        currentNode.setParent(rChild)

    def _rightRotate(self, currentNode):
        """ Description: perform a right rotation from a given node.
            Usage: self._rightRotate(currentNode)
            Return:
        """
        parent = currentNode.getParent()
        lChild = currentNode.getLChild()  # y from book pseudocode
        gRChild = lChild.getRChild()  # x.right from pseudocode

        currentNode.setLChild(gRChild)  # turn y’s left subtree into x’s right subtree
        if (gRChild != None):
            gRChild.setParent(currentNode)
        lChild.setParent(parent)  # link x's parent to y
        if (parent == None):
            self._root = lChild
        elif (currentNode.isRightChild()):
            parent.setRChild(lChild)
        else:
            parent.setLChild(lChild)
        lChild.setRChild(currentNode)
        currentNode.setParent(lChild)