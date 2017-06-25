

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str('Node: {}'.format(self.data))


class BinaryTree:
    def __init__(self):
        self.root = None

    def add_node(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._add_node(self.root, value)

    def _add_node(self, node, value):
        if value < node.data:
            if node.left:
                self._add_node(node.left, value)
            else:
                node.left = Node(value)
        elif value > node.data:
            if node.right:
                self._add_node(node.right, value)
            else:
                node.right = Node(value)

    def add_list(self, n_list):
        for n in n_list:
            self.add_node(n)

    def add_list_balanced(self, n_list):
        pass

    def _traverse_search(self, node, value):
        print('Searching for ' + str(value) + ' in Node ' + str(node.data))
        if node.data == value:
            return node
        else:
            if value < node.data and node.left:
                lft = self._traverse_search(node.left, value)
                if lft:
                    return lft
            if value > node.data and node.right:
                rght = self._traverse_search(node.right, value)
                if rght:
                    return rght

    def _traverse(self, node):
        if node.left:
            yield from self._traverse(node.left)

        yield node.data

        if node.right:
            yield from self._traverse(node.right)

    def _traverse_left(self, node):
        if node.left:
            yield from self._traverse(node.left)
        yield node.data

    def _traverse_right(self, node):
        yield node.data
        if node.right:
            yield from self._traverse(node.right)

    def ordered(self):
        return list(self._traverse(self.root))

    def traverse_left(self):
        return list(self._traverse_left(self.root))

    def traverse_right(self):
        return list(self._traverse_right(self.root))

    def search(self, value):
        return self._traverse_search(self.root, value)


def is_bst(node, min_num=-4294967296, max_num=4294967296):
    if not node:
        return True
    if node.data < min_num or node.data > max_num:
        return False
    return is_bst(node.left, min_num, node.data - 1) and is_bst(node.right, node.data + 1, max_num)

if __name__ == '__main__':
    tree = BinaryTree()
    numbers = [11, 2, 5, 6, 10, 20, 18, 15, 8, 9, 1, 3]
    tree.add_list(numbers)

    print(is_bst(tree.root))
    print(tree.ordered())
    print(tree.traverse_left())
    print(tree.traverse_right())
    srch = tree.search(10)
    print(srch)
    print(srch.left)
    print(srch.right)
