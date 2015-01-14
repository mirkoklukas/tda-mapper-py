# ------------------------------------------------------
# Computing the 1-nerve of a cover.
# ------------------------------------------------------

from combinatoricalHelper import extract_unordered_pairs

# ------------------------------------------------------

def hasNonEmptyIntersection (A, B):
    """Given two iterables it checks wether they have a common element."""
    return len(set(A)&set(A)) > 0

# ------------------------------------------------------

def compute_one_nerve(covering, simplexCondition = hasNonEmptyIntersection):
    """
    Given a covering compute the associated 1-nerve.

    Args:
        covering: A dict of iterables.
        simplexCondition(A, B): A boolean function that returns true iff a 1-simplex between the two 
            iterables A,B should be added.
    Returns:
        A list of pairs (2-tuples) of indices/keys representing the 1-simplex connecting the indices/keys.
        The indices correspond to the entry in the covering at the respective position.
    """
    indices = covering.keys()
    pairs = extract_unordered_pairs(indices)
    simplices = [(i,j) for (i,j) in pairs if simplexCondition(covering[i],covering[j]) == True ] 

    return simplices



