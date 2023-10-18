import collections

Node = collections.namedtuple("Node", ["left", "right", "value"])


def contains(node, value):
    """
    Checks if the given binary search tree (BST) contains the given value.

    :param node: The root node of the BST.
    :param value: The value to search for in the BST.
    :returns: True if the BST contains the value, False otherwise.
    """
    if node is None:
        return False

    if node.value == value:
        return True

    if value < node.value:
        return contains(node.left, value)
    else:
        return contains(node.right, value)
