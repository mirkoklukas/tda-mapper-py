from tdamapper.oneNerve import *

# ------------------------------------------------------

def test_non_empty_intersection():
	assert hasNonEmptyIntersection(set([1,2]), set([2,"two"])) == True
	assert hasNonEmptyIntersection(set([1,2]), set(["one","two"])) == False

# ------------------------------------------------------

def test_one_nerve():
	covering = {
		1: [1,2,3],
		2: [3,4,5],
		3: [5,6,1]
	}
	assert ({},[]) == compute_one_nerve({})
	
	nerve = compute_one_nerve(covering)
	simplices = [(1,2),(2,3),(1,3)]
	assert nerve[0] == covering

	for s in nerve[1]:
		assert s in simplices
	for s in simplices:
		assert s in nerve[1]

# ------------------------------------------------------



