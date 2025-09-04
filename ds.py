------------------------------
--------- STACK --------------
------------------------------

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

------------------------------
--------- QUEUE --------------
------------------------------


# this class is suboptimal. It uses an underlying list (array), so the push method is O(n). This can be fixed by using an underlying linked list instead of an array. 
class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0,item)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

------------------------------
--------- LINKED LIST --------
------------------------------


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    # don't touch below this line

    def __repr__(self):
        return self.val



class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        current = self.head
        while current and hasattr(current, "val"):
            nodes.append(current.val)
            current = current.next
        return " -> ".join(nodes)

    def add_to_tail(self, node):
        if not self.head:
            self.head = node
            return 
        last = None
        for thing in self:
            last = thing
        last.set_next(node)

    def add_to_head(self, node):
        node.set_next(self.head)
        self.head = node
--------------------------------------
------- new linked list stuff, look through lataer and compare
-------------------------------------

from node import Node


class LinkedList:
    def add_to_head(self, node):
        if not self.head:
            self.tail = node
        node.set_next(self.head)
        self.head = node

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.set_next(node)
        self.tail = node

    def __init__(self):
        self.head = None
        self.tail = None

        
    # don't touch below this line

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)


------------- and another one


from node import Node


class LLQueue:
    def remove_from_head(self):
        if not self.head:
            return None
        old_head = self.head
        self.head = self.head.next
        if not self.head:
            self.tail = None
        old_head.next = None
        return old_head
        

    # don't touch below this line

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.set_next(node)
        self.tail = node

    def __init__(self):
        self.tail = None
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " <- ".join(nodes)

---------------------------------------
--------- BINARY SEARCH TREE ----------
---------------------------------------

class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        # O(log(n))
        if not self.val:
            self.val = val
            return
        if self.val == val:
            return
        if val < self.val:
            if not self.left:
                self.left = BSTNode(val)
            else:
                self.left.insert(val)
        else:
            if not self.right:
                self.right = BSTNode(val)
            else:
                self.right.insert(val)

    def get_min(self):
        if not self.left:
            return self.val
        else:
            return self.left.get_min()

    def get_max(self):
        if not self.right:
            return self.val
        else:
            return self.right.get_max()

    def delete(self, val):
        # O(log(n))
        if not self.val:
            return None
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
                # and update the left child reference with the result
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
                # and update the right child's reference with the result
            return self
        if val == self.val:
            if not self.right:
                return self.left
            if not self.left:
                return self.right
            min = self.right.get_min()
            update = self.right.delete(min)
            self.val = min
            self.right = update
            return self

    # preorder traversal is a way to visit all nodes in a BST. it started with the parent and then prints the full left child, then prints the full right child
    def preorder(self, visited):
        visited.append(self.val)
        if self.left != None:
            self.left.preorder(visited)
        if self.right != None:
            self.right.preorder(visited)
        return visited

    # postorder traversal is similar to preorder traversal, but the order the nodes are traversed in is different. The children are done before the parent.
    def postorder(self, visited):
        if self.left:
            self.left.postorder(visited)
        if self.right:
            self.right.postorder(visited)
        visited.append(self.val)
        return visited

    # inorder returns all the nodes of a BST in sorted order
    def inorder(self, visited):
        if self.left:
            self.left.inorder(visited)
        visited.append(self.val)
        if self.right:
            self.right.inorder(visited)
        return visited

    # check to see if a val exists in the BST
    def exists(self, val):
        if self.val == val:
            return True
        elif (val < self.val) and self.left:
            return self.left.exists(val)
        elif (val > self.val) and self.right:
            return self.right.exists(val)
        else:   
            return False

    def height(self):
        if not self.val:
            return 0
        left = self.left.height() if self.left else 0
        right = self.right.height() if self.right else 0
        return max(left, right) + 1

----------------------------------------
------------- RED BLACK TREE -----------
----------------------------------------

class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        # initialise the node to insert
        new_node = RBNode(val)
        new_node.red = True
        new_node.left = self.nil
        new_node.right = self.nil
        
        # find the parent
        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                return # they're equal so val is a duplicate
        # parent is now a reference to the future parent of new_node
        new_node.parent = parent
        if not parent:
            self.root = new_node
        else:
            if parent.val < new_node.val:
                parent.right = new_node
            elif parent.val > new_node.val:
                parent.left = new_node
        self.fix_insert(new_node)

    def rotate_left(self, pivot_parent):
        
        if pivot_parent == self.nil or pivot_parent.right == self.nil:
            return
        pivot = pivot_parent.right
        pivot_parent.right = pivot.left
        if pivot.left != self.nil:
            pivot.left.parent = pivot_parent
        pivot.parent = pivot_parent.parent
        if pivot_parent == self.root:
            self.root = pivot
            pivot.parent = None
        else:
            if pivot_parent == pivot_parent.parent.left:
                pivot_parent.parent.left = pivot
            if pivot_parent == pivot_parent.parent.right:
                pivot_parent.parent.right = pivot
        pivot.left = pivot_parent
        pivot_parent.parent = pivot
    
    def rotate_right(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.left == self.nil:
            return
        pivot = pivot_parent.left
        
        pivot_parent.left = pivot.right
        if pivot.right != self.nil:
            pivot.right.parent = pivot_parent
        pivot.parent = pivot_parent.parent
        if pivot_parent == self.root:
            self.root = pivot
            pivot.parent = None
        else:
            if pivot_parent == pivot_parent.parent.right:
                pivot_parent.parent.right = pivot
            if pivot_parent == pivot_parent.parent.left:
                pivot_parent.parent.left = pivot
        pivot.right = pivot_parent
        pivot_parent.parent = pivot

    def fix_insert(self, new_node):
        current_node = new_node
        while current_node != self.root and current_node.parent.red:
            
            # get a handle on parent, grandparent and uncle nodes
            parent = current_node.parent
            grandparent = parent.parent
            
            if parent == grandparent.left:
                uncle = grandparent.right
                if uncle.red:
                    uncle.red = False
                    parent.red = False
                    grandparent.red = True
                    current_node = grandparent
                else:
                    if current_node == parent.right:
                        current_node = parent
                        self.rotate_left(parent)
                    parent = current_node.parent
                    parent.red = False
                    grandparent.red = True
                    self.rotate_right(grandparent)
                    
            else:
                uncle = grandparent.left
                if uncle.red:
                    uncle.red = False
                    parent.red = False
                    grandparent.red = True
                    current_node = grandparent
                else:
                    if current_node == parent.left:
                        current_node = parent
                        self.rotate_right(parent)
                    parent = current_node.parent
                    parent.red = False
                    grandparent.red = True
                    self.rotate_left(grandparent)
        self.root.red = False    
       

----------------------------------------
------------- HASH MAP -----------------
----------------------------------------


class HashMap:
    def insert(self, key, value):
        storage_index = self.key_to_index(key)
        kv_pair = (key, value)
        self.hashmap[storage_index] = kv_pair

    def resize(self):
        if len(self.hashmap) == 0:
            self.hashmap.append(None)
            return
        cl = self.current_load()
        if cl >= 0.05:
            temp = self.hashmap
            new_hashmap = HashMap(10*len(self.hashmap))
            for thing in temp:
                if thing is not None:
                    new_hashmap.insert(*thing)
            self.hashmap = new_hashmap.hashmap
            

    def current_load(self):
        if len(self.hashmap) == 0:
            return 1
        else:
            count = 0
            for thing in self.hashmap:
                if thing is not None:
                    count += 1
            return count/len(self.hashmap)

    def get(self, key):
        index = self.key_to_index(key)
        if self.hashmap[index]:
            return self.hashmap[index][1]
        else:
            raise Exception("sorry, key not found")
    -----------------------------
    # the following is called 'Linear Probing'. It's a better way of inserting and getting elements from a hashmap because it handles collisions better (a collision is when two different keys have the same index after applying key_to_index()).
    def insert(self, key, value):
        index = self.key_to_index(key)
        original_index = index
        first_iteration = True
        while (self.hashmap[index] is not None):
            print(index)
            if not first_iteration and index == original_index:
                raise Exception("hashmap is full")
            index += 1 
            index = index % len(self.hashmap)
            first_iteration=False
        self.hashmap[index] = (key, value)

    def get(self, key):
        index = self.key_to_index(key)
        original_index = index
        first_iteration = True
        while self.hashmap[index] is not None:
            if self.hashmap[index][0] == key:
                return self.hashmap[index][1]
            if not first_iteration and index == original_index:
                raise Exception("sorry, key not found")
            index += 1 
            index = index % len(self.hashmap)
            first_iteration = False
        raise Exception("sorry, key not found")

    ----------------------------------------

    def __init__(self, size):
        self.hashmap = [None for i in range(size)] 

    def key_to_index(self, key): 
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {i}: {str(v)}\n"
            else:
                final += f" - {i}: None\n"
        return final


-----------------------------------------------
---------------- TRIES ------------------------
-----------------------------------------------


class Trie:
    def exists(self, word):
        current_level = self.root
        for letter in word:
            if letter not in current_level:
                return False
            current_level = current_level[letter]
        if self.end_symbol in current_level:
            return True
        else:
            return False
    def add(self, word):
        current_level = self.root
        for letter in word:
            if letter not in current_level:
                # add it and create a new nested level/dict for it
                current_level[letter] = {}
            # update current level to the nested dict for this letter
            current_level = current_level[letter]
        current_level[self.end_symbol] = True


    def search_level(self, current_level, current_prefix, words):
        if self.end_symbol in current_level:
            words.append(current_prefix)
        
        letters = current_level.keys()
        sorted_letters = sorted(letters)
        
        for letter in sorted_letters:
            prefix = current_prefix + letter
            if current_level[letter] is not True:
                self.search_level(current_level[letter], prefix, words)
        return words

    def words_with_prefix(self, prefix):
        words = []
        current_level = self.root
        for letter in prefix:
            if letter not in current_level:
                return []
            current_level = current_level[letter]
        words = []
        self.search_level(current_level, prefix, words)
        return words


    def find_matches(self, document):
        matches = set()
        current_level = self.root
        for i in range(len(document)):
            current_level = self.root
            for j in range(i, len(document)):
                if document[j] not in current_level:
                    break
                current_level = current_level[document[j]]
                if self.end_symbol in current_level:
                    matches.add(document[i:j+1])
        return matches

    def longest_common_prefix(self):
        current_level = self.root
        prefix = ""
        while True:
            keys = list(current_level.keys())
            if self.end_symbol in keys:
                break
            if len(keys) == 1:
                prefix += keys[0]
                current_level = current_level[keys[0]]
            else:
                break
        return prefix

    def advanced_find_matches(self, document, variations):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch in variations:
                    ch = variations[ch]
                if ch not in level:
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"
