

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    head = None

    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def pop(self):
        current = self.head
        previous = None
        while current.next:
            previous = current
            current = current.next
        previous.next = None
        return current.value

    def insert(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            node = Node(value)
            last_node.next = node

    def insert_sorted(self, value):
        if not self.head:
            self.head = Node(value)
        elif value < self.head.value:
            self.push(value)
        else:
            last_node = self.head
            while last_node.next and value > last_node.next.value:
                last_node = last_node.next
            node = Node(value)
            temp = None
            if last_node.next:
                temp = last_node.next
            last_node.next = node
            node.next = temp

    def insert_list_sorted(self, lst):
        for n in lst:
            self.insert_sorted(n)

    def reverse(self):
        current = self.head
        previous = None
        while current:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt
        self.head = previous

    def detect_loop(self):
        slow_p = self.head
        fast_p = self.head
        while slow_p and fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                print('Found Loop')
                return
        print('No Loop Found')

    def remove_loop(self):
        slow_p = self.head
        fast_p = self.head
        temp = None
        while slow_p and fast_p and fast_p.next:
            slow_p = slow_p.next
            temp = fast_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                temp.next = None
        print('Removed pointer to {}'.format(temp.value))

    def print_values(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next


if __name__ == '__main__':
    print('Linked List #1')
    llist1 = LinkedList()
    llist1.push(20)
    llist1.push(4)
    llist1.push(15)
    llist1.push(10)
    llist1.print_values()

    print('\n')
    print('-----------------')
    print('Linked List #2')
    llist2 = LinkedList()
    llist2.insert(20)
    llist2.insert(4)
    llist2.insert(15)
    llist2.insert(10)
    llist2.print_values()

    print('\n')
    print('-----------------')
    print('Linked List #3')
    llist3 = LinkedList()
    llist3.insert(20)
    llist3.insert(4)
    llist3.insert(15)
    llist3.insert(10)
    print('Popped {} from the queue.'.format(llist3.pop()))
    print('Popped {} from the queue.'.format(llist3.pop()))
    llist3.print_values()

    print('\n')
    print('-----------------')
    print('Linked List #4')
    llist4 = LinkedList()
    llist4.insert(20)
    llist4.insert(4)
    llist4.insert(15)
    llist4.insert(10)
    llist4.print_values()
    print('----Reversed-----')
    llist4.reverse()
    llist4.print_values()

    print('\n')
    print('-----------------')
    print('Linked List #5')
    llist5 = LinkedList()
    llist5.insert(20)
    llist5.insert(4)
    llist5.insert(15)
    llist5.insert(10)
    llist5.detect_loop()
    print('Adding loop')
    llist5.head.next.next.next.next = llist5.head.next
    llist5.detect_loop()
    print('Removing loop')
    llist5.remove_loop()
    llist5.detect_loop()
    llist4.print_values()

    print('\n')
    print('-----------------')
    print('Linked List #6')
    llist6 = LinkedList()
    llist6.insert_sorted(20)
    llist6.insert_sorted(4)
    llist6.insert_sorted(15)
    llist6.insert_sorted(10)
    llist6.print_values()

    print('\n')
    print('-----------------')
    print('Linked List #7')
    llist7 = LinkedList()
    ar = [35, 54, 18, 72, 37, 96, 24, 15, 18, 26, 37, 49, 82]
    llist7.insert_list_sorted(ar)
    llist7.print_values()
