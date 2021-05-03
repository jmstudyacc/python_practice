# implements a hash table with separate chaining - lacks efficiency but quick and dirty
# why might a hash table be needed? Accessing elements by key is an improvement to static integer values

class HashTable:
    def __init__(self, INITIAL_CAPACITY=53):
        """
        Args:
            INITIAL_CAPACITY: value is arbitrarily set to 53 to ensure it is prime
            and a decent size for testing purposes. This defines the size of the internal array and in a more complex
            hash table implementation (open-addressed, double-hashed) this value should be able to change

            @TODO
            Current implementation is bad practise for scalability reasons.

        Uniformity is the target for this hash table implementation. High uniformity leads to keys being evenly
        distributed among all available buckets. Uneven distribution negates some of the benefits of a hash table
        and lead to a bloated LinkedList
        """
        self.capacity = INITIAL_CAPACITY
        # refers to the number of elements that have been added
        self.size = 0
        # internal array that stores each inserted value in a 'bucket' based on a key
        self.buckets = [None] * self.capacity

    def hash(self, key):
        """
        This function returns an arbitrary but fairly uniform outcome. You can instead choose to use a
        hash function that comes readily with Python3 or a separate library.
        Args:
            key:

        Returns:
            hash_sum = denotes the index to insert the key

        """
        hash_sum = 0

        # loop over each character in the key
        for index, char in enumerate(key):
            # adds (index + length of key) to the power of (current char code)
            # ord() built-in returns an integer representing the unicode point of that character
            hash_sum += (index + len(key)) ** ord(char)

            # perform modulus on hash_sum to keep the return hash_sum value in range[0..self.capacity-1]
            hash_sum = hash_sum % self.capacity

            return hash_sum

    def insert(self, key, value):
        """
        Inserting a K/V pair into the hash table has the following steps:

        1 - increment the size of the hash table
        2 - compute the index of key using the hash function
        3 - if the bucket at the index is empty, create a new node and add to the bucket at index
        4 - otherwise a collision has occurred, a LinkedList of at least 1 node is present and
            the code must iterate to the end of the LinkedList and append a new Node

        Args:
            key:
            value:

        Returns:

        """
        # 1. increment the size
        self.size += 1

        # 2. Compute the index of key
        idx = self.hash(key)

        # access the node corresponding to the hash result
        node = self.buckets[idx]

        # 3. If bucket is empty
        if node is None:
            # create a node, add it and return it
            self.buckets[idx] = Node(key, value)
            # not returning anything but ending the if statement
            return

        # 4. collision occurs - iterate to the end of the LinkedList at provided index value
        prev = Node
        while node is not None:
            prev = node
            node = node.next

        # add a new node at the end of the LinkedList with the key, value pair specified
        prev.next = Node(key, value)

    def find_key(self, key):
        """
        Once the data is stored, you need to be able to find the value when provided a key.

        1. compute the index for the provided key using the hash function
        2. access the bucket for that index
        3. iterate the nodes in the LinkedList until the key is found - or end of LinkedList is reached
        4. return the value of the found node, or None if value not found

        Args:
            key:

        Returns:

        """
        # 1. compute hash
        index = self.hash(key)

        # 2. go to first node in list at bucket
        node = self.buckets[index]

        # 3. traverse the LinkedList at this node continuing until value found or list is empty
        while node is not None and node.key != key:
            node = node.next

        # 4. node will either be the require key/value pair or return None
        if node is None:
            # failure condition
            return None
        else:
            # success condition
            return node.value

    def remove(self, key):
        """
        Removing an item from a hash table is similar to removing an element from a Linked List.
        This method returns the data value removed or None if the requested node is not found.

        1. compute hash for the key to determine the required index
        2. iterate LinkedList of nodes, continue until found or until end of list
        3. if key is not found, return None
        4. if key is found, remove from the LinkedList and return Node value

        Args:
            key:

        Returns:

        """
        # 1. compute hash
        index = self.hash(key)
        node = self.buckets[index]
        prev = None

        # 2. iterate to the requested node
        while node is not None and node.key != key:
            prev = node
            node = node.next

        # the node will either become the required Node or None needs to be returned
        if node is None:
            # 3. key is not found
            return None
        else:
            # 4. key is found
            self.size -= 1      # reduce the size of the LinkedList as we are removing a Node
            result = node.value

            # delete the element in the LinkedList
            if prev is None:
                node = None
            else:
                prev.next = prev.next.next

            # return the deleted value
            return result


class Node:
    """
    This approach enables us to implement 1 mitigation of collisions. This occurs when two keys have the same
    hash value. If a new value is written to a hash value that is a collision, you will lose the original value
    as the new value overwrites it.

    By using separate chaining, a linkedlist is created at each index of the bucket array. This contains all of the
    keys at the given bucket array index. When you need to find an item, you iterate over the linkedlist until
    you find a Node with the required key.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        # node is a member of a LinkedList so needs to have the next value set - it is None at init though
        self.next = None


# instantiate a hash table
ht1 = HashTable()

# create a dataset to store
names = ["Abe", "Bob", "Clyde"]

# inserts the created data under a key known as 'Staff'
ht1.insert("Staff", names)

staff_records = ht1.find_key('Staff')
print(staff_records)

