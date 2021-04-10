class Node:
    def __init__(self, val):
        if isinstance(val, int):
            self.val = val
            self.__left = None
            self.__right = None
        else:
            raise TypeError('Node value must be an integer!')

    def __repr__(self):
        return Node.__wrapper_repr(self, 0, '', 'Root')

    @staticmethod
    def __wrapper_repr(node, indent, string, direction):
        string += ('\t' * indent) + direction + ' [ ' + str(node.val) + ' ]\n'

        if node.__left is not None:
            string = Node.__wrapper_repr(node.__left, indent + 1, string, 'Left')

        if node.__right is not None:
            string = Node.__wrapper_repr(node.__right, indent + 1, string, 'Right')

        return string

    def add_left(self, left):
        if isinstance(left, Node):
            self.__left = left
        else:
            raise TypeError('Node child (left) must be Node type!')

    def add_right(self, right):
        if isinstance(right, Node):
            self.__right = right
        else:
            raise TypeError('Node child (right) must be Node type!')

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right
