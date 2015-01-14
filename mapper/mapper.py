# ------------------------------------------------------
# A straightforward implementation of the mapper construction by Carlsson--Memoli--Singh.
# (I wrote a little blog post about it at http://mapsfunctionsandarrows.blogspot.de)
# ------------------------------------------------------

from oneNerve import compute_one_nerve

def mapper(clusterer, referenceFct, funcCover):
    """Mapper is a construction that uses a given cluster-algorithm to 
    associate a simplicial complex to a reference map on a given data set.

    Args:
        clusterer: A class that inherits from AbstractClusterFunction. 
        refFct: A ReferenceFunction class. A callable class that can be called with elements form the dataset.
        funcCover: A dict of boolean functions (characteristic functions), 
            that are defined on the target space of the given filter.
    Returns:
        A simplicial complex.
    """
    clusterCover = clusterer.push_forward(referenceFct.pull_back(funcCover))
    oneNerve = compute_one_nerve(clusterCover)

    return (clusterCover, oneNerve)

