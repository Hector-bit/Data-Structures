from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.storage = {}
        self.cache = DoublyLinkedList()
        self.size = 0
    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        #if key is in storage
            #move it to the end
            #return the value
        #if key is not in storage
            #return nothing
        if key in self.storage:
            node = self.storage[key]
            self.cache.move_to_end(node)
            return node.value[1]
        else:
            return None
    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        #If the cache is empty:
            # Add to the linked list(key and the value)
            # Add the key and value to the dictionary
            # increment size
        # If cache not emtpy:
            #check and see if the key is in the dict
            # If it is
                #overwrite the value
                #move it to the end

            # if it isn't
                # check and see if the cache is full
                    # if the cache is not full
                        # same as if the cache is empty
                    # if cach is full
                        #remove the oldest entry from dict and Linked list
                        #reduce the size
                        #same as if cache is emtpy
        #add to the linked list (key and the value)
        #add the key and value to the dictionary
        #increment the size
        if key in self.storage: 
            self.storage[key].value = (key, value)
            self.cache.move_to_end(self.storage[key])
        else:
            if self.size == self.limit:
                self.storage.pop(self.cache.head.value[0])
                self.cache.remove_from_head() 
            else:
                self.size += 1
            self.cache.add_to_tail((key, value))
            self.storage[key] = self.cache.tail
        # if key
        # if self.size == self.limit:
        #     del self.storage[self.cache.head.value[0]]
        #     self.cache.remove_from_head()
        #     self.size -= 1
        # self.cache.add_to_tail((key, value))
        # self.storage[key] = self.cache.tail
        # self.size += 1