"""Test basic creation of Node class"""
import pytest
from main.Node import Node


def test_basic_node_creation():
    with pytest.raises(TypeError):
        Node(5.0)

    node = Node(5)
    assert node.val == 5
    assert node.get_left() is None
    assert node.get_right() is None


def test_adding_and_getting_left_and_right():
    with pytest.raises(TypeError):
        Node(1).add_left(1)
        Node(1).add_right("right")

    node = Node(1)
    left = Node(10)
    right = Node(20)

    node.add_left(left)
    assert node.get_left() == left
    assert node.get_left().val == 10

    node.add_right(right)
    assert node.get_right() == right
    assert node.get_right().val == 20
