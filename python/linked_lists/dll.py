import pdb

class DNode:
    """
    Define a node with data, prev_node and next_node reference
    """
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None


class DoublyLinkedList:
    """
    Set beginning and end of a doubly linked list defining the fist and last nodes
    """
    def __init__(self, first_node, last_node):
        self.first_node = first_node
        self.last_node = last_node


    def print_list(self):
        """
        Print current doubly linked list
        """

        current = self.first_node
        idx = 0
        while current:
            print(f'{current.data}')
            current = current.next_node
            idx += 1
        print('')


    def print_list_reverse(self):
        """
        Print current doubly linked list in reverse order
        """

        current = self.last_node
        idx = 0
        while current:
            print(f'{current.data}')
            current = current.prev_node
            idx += 1
        print('')


    def read(self, index):
        """
        Return node value at index
        """

        current = self.first_node
        current_idx = 0

        while current_idx < index:
            current = current.next_node
            current_idx += 1
            if not current:
                return
        return current.data


    def search(self, value):
        """
        Return the index for a node of value
        """
        current = self.first_node
        current_idx = 0

        while current:
            if current.data == value:
                return current_idx

            current = current.next_node
            current_idx += 1


    def insert_at_end(self, new_node):
        """
        Insert a node at the end of the doubly linked list in O(1)
        """

        # if there are no element in the dll
        if not self.first_node:
            self.first_node = new_node
            self.last_node = new_node

        self.last_node.next_node = new_node
        new_node.prev_node = self.last_node
        self.last_node = new_node


    def remove_from_front(self):
        """
        Remove the first node and return it
        """
        removed = self.first_node
        self.first_node = self.first_node.next_node
        self.first_node.prev_node = None
        return removed

if __name__ == "__main__":

    ## some examples

    node1 = DNode('a')
    node2 = DNode('b')

    node1.next_node = node2
    node2.prev_node = node1

    dllist = DoublyLinkedList(node1, node2)

    new_node = DNode('zz')
    dllist.insert_at_end(new_node)
    dllist.print_list()

    print(dllist.remove_from_front())
    print('')
    dllist.print_list()
