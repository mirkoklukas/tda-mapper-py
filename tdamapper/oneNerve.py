# ------------------------------------------------------
# Computing the 1-nerve of a cover.
# ------------------------------------------------------

from tdamapper.combinatoricalHelper import extract_unordered_pairs

# ------------------------------------------------------

def hasNonEmptyIntersection (A, B):
    """Given two iterables it checks wether they have a common element."""
    return len(set(A)&set(B)) > 0

# ------------------------------------------------------

class OneSimplex(tuple, object):
    def __init__(self, *args):
        super(tuple, self).__init__(*args)
        self.node = self[0]
        self.links = self[1]

    def nodes(self):
        return self(0)

    def links(self):
        return self(1)

    def cast_to_d3js(self):
        cover = self[0]
        simplicies = self[1]
        keys = cover.keys()
        lookup = dict(zip(keys, range(len(keys))))
        d3jsGraph = { 
            "nodes": [
                {
                    "name": key, 
                    "group": key[0], 
                    "size": len(cover[key])
                } 
                for key in keys],
            "links": [
                { 
                    "source": lookup[i], 
                    "target": lookup[j],
                    "size": len(set(cover[i])&set(cover[j])),
                    "value": 1
                }
                for (i, j) in simplicies]
        }

        return d3jsGraph


def compute_one_nerve(covering, simplexCondition = hasNonEmptyIntersection):
    """
    Given a covering it computes the associated 1-nerve.

    Args:
        covering: A dict of iterables.
        simplexCondition(A, B): A boolean function that returns true iff 
            a 1-simplex between the two iterables A,B should be added.
    Returns:
        A tuple (C,S), where C is the given covering, and S is 
        a list of 2-tuples (i,j), with i<j, of indices/keys representing 
        the 1-simplex connecting the indices/keys. The indices correspond 
        to the entry in the covering at the respective position.
    """
    indices = covering.keys()
    pairs = extract_unordered_pairs(indices)
    simplices = [(i,j) for (i,j) in pairs if simplexCondition(covering[i],covering[j]) == True ] 

    return OneSimplex((covering, simplices))

# ------------------------------------------------------





