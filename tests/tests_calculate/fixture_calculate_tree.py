"""Create bigger tree for calculate testing"""
import pytest
from main.Node import Node


@pytest.fixture(scope='package')
def tree():
    root = Node(5)
    first_left = Node(3)
    first_right = Node(7)
    second_right = Node(0)

    second_right.add_left(Node(2))
    second_right.add_right(Node(8))
    second_right.get_right().add_right(Node(5))

    first_right.add_left(Node(1))
    first_right.add_right(second_right)

    first_left.add_left(Node(2))
    first_left.add_right(Node(5))

    root.add_left(first_left)
    root.add_right(first_right)

    return root
