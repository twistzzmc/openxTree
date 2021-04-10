"""Test calculating average of node"""
from main.Calculate import Calculate
from tests.tests_calculate.fixture_calculate_tree import tree


def test_calculation_average(tree):
    assert Calculate.calculate_node_average(tree) == 3.8
    assert round(Calculate.calculate_node_average(tree.get_left()), 5) == 3.33333
    assert Calculate.calculate_node_average(tree.get_left().get_left()) == 2
    assert round(Calculate.calculate_node_average(tree.get_right()), 5) == 3.83333
    assert Calculate.calculate_node_average(tree.get_right().get_right()) == 3.75
    assert Calculate.calculate_node_average(tree.get_right().get_right().get_right()) == 6.5
