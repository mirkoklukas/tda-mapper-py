from tdamapper.combinatoricalHelper import *

# ------------------------------------------------------

def test_extract_unordered_pairs():
    assert [] == extract_unordered_pairs([])
    assert [(1,"two"),(1,(3,3)),("two",(3,3))] == extract_unordered_pairs([1,"two",(3,3)])

# ------------------------------------------------------

def test_get_horizontal_paths():
    assert [] == get_horizontal_paths([])
    assert [] == get_horizontal_paths([[],[]])
    assert [(1, 2, {"three":3}), (1, "two", {"three":3})] == get_horizontal_paths([[1], [2,"two"], [{"three":3}]])

# ------------------------------------------------------