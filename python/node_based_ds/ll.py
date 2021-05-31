# Linked-lists

class Node:
    """
    Define a node with data and next_node reference
    """
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __str__(self):
        return f'{self.data} -> {self.next_node}'

class LinkedList:
    """
    Set beginning of a linked list defining the fist node
    """
    def __init__(self, first_node):
        self.first_node = first_node

    def print_list(self):
        """
        Print current linked list
        """

        current = self.first_node
        idx = 0
        while current:
            print(f'{current.data}')
            current = current.next_node
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

    def insert(self, index, new_node):
        """
        Insert a new node at index
        """

        current = self.first_node
        current_idx = 0

        if index == 0:
            new_node.next_node = current
            self.first_node = new_node
            return

        while current_idx < (index -1):
            current_idx += 1
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node


    def delete(self, index):
        """
        Delete a node at index
        """

        current = self.first_node
        current_idx = 0

        if index == 0:
            self.first_node = current.next_node
            return

        while current_idx < (index -1):
            current_idx += 1
            current = current.next_node

        current.next_node = current.next_node.next_node

    def last_node(self, head):
        """
        Return data of the last node. This method does not know
        how many element are in the list
        """
        idx = 0
        current_node = head
        while current_node.next_node:
            current_node = current_node.next_node
        return current_node.data


    @staticmethod
    def reverse(head):
        """
        Reverse a linked list starting from the head
        """
        prev = None
        current = head

        while current:
            _next = current.next_node
            current.next_node = prev
            prev = current
            current = _next

    @staticmethod
    def remove_access_node(access_node):
        """
        The method delete the access node preserving the rest of the list
        The access node has no knowldge of previous nodes.
        """
        _next_node = access_node.next_node
        # copy the next node in place of the access node
        access_node.data = _next_node.data
        access_node.next_node = _next_node.next_node




if __name__ == "__main__":

    ## some examples

    node1 = Node('a')
    node2 = Node('b')
    node3 = Node('c')
    node4 = Node('d')

    node1.next_node = node2
    node2.next_node = node3
    node3.next_node = node4

    llist = LinkedList(node1)
    llist.print_list()

    #reverse llist
    #LinkedList.reverse(node1)
    #llist = LinkedList(node4)
    #llist.print_list()

    print(llist.search('c'))
    print(llist.search('d'))
    print(llist.search('x'))
    print('')


    new_node = Node('zz')
    llist.insert(0, new_node)
    llist.print_list()

    llist.delete(1)
    llist.print_list()
    print(llist.last_node(new_node))
    print('')

    LinkedList.remove_access_node(node3)
    llist.print_list()
