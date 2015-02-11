# ------------------------------------------------------
# Some Helper. 
# ------------------------------------------------------

def extract_unordered_pairs(ids):
    """Given a list of n ids it returns a list of all n-over-2 unordered pairs."""
    pairs = []
    for i in range(len(ids)):
        for j in range(i+1, len(ids)):
            pairs.append((ids[i],ids[j]))
    return pairs

# ------------------------------------------------------

def get_horizontal_paths(listOfLists):
    """Given a list of lists it returns a list of tuples whose k'th entry is in the k'th list."""
    if len(listOfLists) == 0:
        return []
    if len(listOfLists) == 1:
        return [ (x,) for x in listOfLists[0]] 
    else:
        shortTuples = get_horizontal_paths(listOfLists[1:])
        return [ (x,) + shortTuple for x in listOfLists[0] for shortTuple in shortTuples]

# ------------------------------------------------------