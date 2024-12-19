# Do not modify this class
class Node:
    'Node object to be used in DoublyLinkedList'
    def __init__(self, item, _next=None, _prev=None):
        'initializes new node objects'
        self.item = item
        self._next = _next
        self._prev = _prev

    def __repr__(self):
        'String representation of Node'
        return f"Node({self.item})"


class DoublyLinkedList:
    def __init__(self, items=None):
        'Construct a new DLL object'
        self._head = None
        self._tail = None
        self._len = 0
        self._nodes = dict()    # dictionary of item:node pairs

        # initialize list w/ items if specified
        if items is not None:
            for item in items:
                self.add_last(item)

    def __len__(self):
        'returns number of nodes in DLL'
        return self._len

    def __repr__(self):
        return str(self._nodes)

    # TODO: Modify the 4 methods below to keep `self._nodes` up-to-date
    def add_first(self, item):
        'adds item to front of dll'
        # add new node as head
        self._head = Node(item, _next=self._head, _prev=None)
        self._len += 1

        # if that was the first node
        if len(self) == 1: self._tail = self._head

        # otherwise, redirect old heads ._tail pointer
        else: self._head._next._prev = self._head



        # creates temp dic
        temporarydic = {}
        # Adds new node to temp dic so new node is at the start of the dic
        temporarydic.update({item: self._head})
        # adds all of _nodes together so the new node is first always
        temporarydic.update(self._nodes)
        # copies to _nodes
        self._nodes = temporarydic.copy()

    def add_last(self, item):
        'adds item to end of dll'
        # add new node as head
        self._tail = Node(item, _next=None, _prev=self._tail)
        self._len += 1
        # if that was the first node
        if len(self) == 1: self._head = self._tail
        # otherwise, redirect old heads ._tail pointer
        else: self._tail._prev._next = self._tail


        # adds node to end of dic
        self._nodes.update({item: self._tail})


    def remove_first(self):
        'removes and returns first item'
        if len(self) == 0: raise RuntimeError("cannot remove from empty dll")
        # extract item for later
        item = self._head.item

        # move up head pointer
        self._head = self._head._next
        self._len -= 1

        # was that the last node?
        if len(self) == 0: self._tail = None

        else: self._head._prev = None



        # removes first in dic
        (k := next(iter(self._nodes)))
        self._nodes.pop(k)



        return item
        
    def remove_last(self):
        'removes and returns last item'
        if len(self) == 0: raise RuntimeError("cannot remove from empty dll")

        # extract item for later
        item = self._tail.item

        # move up tail pointer
        self._tail = self._tail._prev
        self._len -= 1

        # was that the last node?
        if len(self) == 0: self._head = None

        else: self._tail._next = None



        # removes las element in dic
        self._nodes.popitem()

        return item
        
    # TODO: Add a docstring and implement
    def __contains__(self, item):
        'Returns true/false depending on if item is in ._nodes'
        return (item in self._nodes)

    # TODO: Add a docstring and implement
    def neighbors(self, item):
        'Returns node and neghiboring nodes if item is in ._nodes'
        if item in self._nodes:
            if item == self._head.item:
                return (None, ((self._nodes.get(item))._next).item)
            elif item == self._tail.item:
                return (((self._nodes.get(item))._prev).item, None)
            else:
                return (((self._nodes.get(item))._prev).item, ((self._nodes.get(item))._next).item)
        else:
            raise RuntimeError

    # TODO: Add a docstring and implement
    def remove_node(self, item):
        'Removes selected node and stiches surroundng nodes'
        # if there are no nodes
        if self._len == 0:
            raise RuntimeError
        # if item in not in dic
        elif item not in self._nodes:
            raise RuntimeError
        # if there is only 1 item in dic and that item is removed
        elif self._len == 1:
            self._nodes.pop(item)
            self._tail = None
            self._head = None

        # if the head if being removed
        elif (self._nodes.get(item)) == self._head:
            self._head = ((self._nodes.get(item))._next)
            ((((self._nodes.get(item)))._next)._prev) = None
            self._nodes.pop(item)

        # if the tail is being removed
        elif (self._nodes.get(item)) == self._tail:
            self._tail = ((self._nodes.get(item))._prev)
            ((((self._nodes.get(item)))._prev)._next) = None
            self._nodes.pop(item)

        # every other scenerio
        else:
            ((((self._nodes.get(item)))._next)._prev) = (((self._nodes.get(item)))._prev)
            ((((self._nodes.get(item)))._prev)._next) = (((self._nodes.get(item)))._next)
            self._nodes.pop(item)

        self._len -= 1











