"""Test calculating median of node"""
from main.Calculate import Calculate
from tests.tests_calculate.fixture_calculate_tree import tree


def test_calculation_median(tree):
    assert Calculate.calculate_node_median(tree) == 4
    assert Calculate.calculate_node_median(tree.get_left()) == 3
    assert Calculate.calculate_node_median(tree.get_left().get_left()) == 2
    assert Calculate.calculate_node_median(tree.get_right()) == 3.5
    assert Calculate.calculate_node_median(tree.get_right().get_right()) == 3.5
    assert Calculate.calculate_node_median(tree.get_right().get_right().get_right()) == 6.5
