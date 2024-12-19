from DoublyLinkedList import DoublyLinkedList as DLL
import unittest

# Basic tests are provided for you, but you need to implement the last 3 unittests
class testDLL(unittest.TestCase):
    def test_addfirst_removefirst(self):
        'adds items to front, then removes from front'
        dll = DLL()
        n = 100

        for j in range(5): # repeat a few times to make sure removing last item doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_first(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_first(), n-1-i)

            with self.assertRaises(RuntimeError):
                dll.remove_first()

    def test_addlast_removelast(self):
        'adds items to end, then removes from end'
        dll = DLL()
        n = 100

        for j in range(5): # repeat a few times to make sure removing last item doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_last(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_last(), n-1-i)

            with self.assertRaises(RuntimeError):
                dll.remove_last()

    def test_add_remove_mix(self):
        'various add/remove patterns'
        dll = DLL()
        n = 100

        # addfirst/removelast
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_first(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_last(), i)

        # addlast/removefirst
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_last(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_first(), i)

        # mix of first/last
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                if i%2: dll.add_last(i) # odd numbers - add last
                else: dll.add_first(i)  # even numbers - add first

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                if i%2: self.assertEqual(dll.remove_last(), n-i) # odd numbers: remove last
                else: self.assertEqual(dll.remove_first(), n-2-i) # even numbers: remove first

    # TODO: Add docstrings to and implement the unittests below
    def test_contains(self):



        n = 50
        dll = DLL()
        for i in range(n): # Repeats 50 times
            self.assertEqual((i in dll), False) # Checks to see if i is in ddl
            dll.add_first(i) # adds i to dll
            self.assertEqual((i in dll), True) # checks to see if i was added properly in dll
            dll.remove_first() # Removes i
            self.assertEqual((i in dll), False) # Checks to see if i was removed properly

        pass

    def test_neighbors(self):



        n = 100
        dll = DLL()
        for i in range(n):
            dll.add_last(i) # creates ddl instance with range 100
        for i in range(n+100):
            if i in dll:
                if i == dll._head.item: # checks to see if head node is being called
                    self.assertEqual((dll.neighbors(i)), (None, (i+1))) # returns neigbors
                elif i == dll._tail.item: # checks to see if tail node is being called
                    self.assertEqual((dll.neighbors(i)), ((i-1), None))# returns neigbors
                else:
                    self.assertEqual((dll.neighbors(i)), ((i-1), (i+1))) # returns neigbors
            else:
                self.assertRaises(RuntimeError) # Returns error if not in ddl









        pass

    def test_remove_item(self):

        # “stitch together” testing
        dll = DLL([1,2,3]) # created a ddl instance
        self.assertEqual((dll._head._next), dll._nodes.get(2)) # Check to see node1 is pointed to node 2
        self.assertEqual((dll._tail._prev), dll._nodes.get(2)) # While node3 is back pointed to node 2
        dll.remove_node(2) # Removes node2
        self.assertEqual((dll._head._next), dll._nodes.get(3)) # Check that node1 is now pionted to node 3 since node2 was removed
        self.assertEqual((dll._tail._prev), dll._nodes.get(1)) # Check that node3 is now back pionted to node 1 since node2 was removed

        # Edge case - Removing the head
        dll = DLL([1, 2, 3])  # created a ddl instance
        self.assertEqual((dll._nodes.get(2))._prev, dll._nodes.get(1))  # Check to see node2 is back pointed to node 1
        self.assertEqual((dll._nodes.get(2))._next, dll._nodes.get(3))  # Check to see node2 is pointed to node 3
        dll.remove_node(1)  # Removes node1
        self.assertEqual((dll._nodes.get(2))._prev, None)  # Check to see node2 is back pointed to None since it is now the head
        self.assertEqual((dll._nodes.get(2))._next, dll._nodes.get(3))  # Check to see node2 is pointed to node 3\
        self.assertEqual(dll._head, (dll._nodes.get(2)))  # Node 2 is now the head

        # Edge case - Removing the tail
        dll = DLL([1, 2, 3])  # created a ddl instance
        self.assertEqual((dll._nodes.get(2))._prev, dll._nodes.get(1))  # Check to see node2 is back pointed to node 1
        self.assertEqual((dll._nodes.get(2))._next, dll._nodes.get(3))  # Check to see node2 is pointed to node 3
        dll.remove_node(3)  # Removes node1
        self.assertEqual((dll._nodes.get(2))._prev, dll._nodes.get(1))  # Check to see node2 is back pointed to node1
        self.assertEqual((dll._nodes.get(2))._next, None)  # Check to see node2 is pointed to None now that it is the tail
        self.assertEqual(dll._tail, (dll._nodes.get(2)))  # Node 2 is now the tail











        pass



if __name__ == "__main__":
    unittest.main()
