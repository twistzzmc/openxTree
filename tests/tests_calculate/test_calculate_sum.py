"""Test calculating sum of node"""
from main.Calculate import Calculate
from tests.tests_calculate.fixture_calculate_tree import tree


def test_calculation_total_sum(tree):
    assert Calculate.calculate_node_sum(tree) == 38
    assert Calculate.calculate_node_sum(tree.get_left()) == 10
    assert Calculate.calculate_node_sum(tree.get_left().get_left()) == 2
    assert Calculate.calculate_node_sum(tree.get_right()) == 23
    assert Calculate.calculate_node_sum(tree.get_right().get_right()) == 15
    assert Calculate.calculate_node_sum(tree.get_right().get_right().get_right()) == 13
