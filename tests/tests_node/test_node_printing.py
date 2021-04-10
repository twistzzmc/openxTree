"""Test printing of Node class"""
import pytest
from main.Node import Node


def test_node_printing():
    root = Node(10)
    root.add_left(Node(20))
    root.add_right(Node(30))
    root.get_right().add_left(Node(40))

    assert root.get_left().__repr__() == 'Root [ 20 ]\n'
    assert root.get_right().__repr__() == 'Root [ 30 ]\n\tLeft [ 40 ]\n'
    assert root.__repr__() == 'Root [ 10 ]\n\tLeft [ 20 ]\n\tRight [ 30 ]' \
                              '\n\t\tLeft [ 40 ]\n'
