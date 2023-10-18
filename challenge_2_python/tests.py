from .bst import Node, contains


class TestBST:
    def test_contains_value_in_bst(self):
        n1 = Node(value=1, left=None, right=None)
        n3 = Node(value=3, left=None, right=None)
        n2 = Node(value=2, left=n1, right=n3)
        assert contains(n2, 3)

    def test_does_not_contain_value_in_bst(self):
        n1 = Node(value=1, left=None, right=None)
        n3 = Node(value=3, left=None, right=None)
        n2 = Node(value=2, left=n1, right=n3)
        assert not contains(n2, 4)

    def test_contains_value_in_empty_bst(self):
        assert not contains(None, 1)

    def test_contains_value_in_single_node_bst(self):
        n1 = Node(value=1, left=None, right=None)
        assert contains(n1, 1)
        assert not contains(n1, 2)
