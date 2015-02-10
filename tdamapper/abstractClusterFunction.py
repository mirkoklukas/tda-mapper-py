# ------------------------------------------------------
# An abstract base class for a cluster function.
# ------------------------------------------------------

import operator

def extendIndex(i, Us):
    return [ ((i,j),U) for j,U in enumerate(Us)]

class AbstractClusterFunction(object):
    def __call__(self, data):
        """Given a list of data points it returns a list of clusters, 
        where a cluster is list of data points.
        
        Args:
            data: A list of data points, e.g. tuples in R**n or unique identifiers.
        Returns:
            A list of clusters, where a cluster is a list of data points.
        """
        raise NotImplementedError("Should have implemented this")

    def push_forward(self, cover):
        """Takes a cover and applies the cluster function to each element, 
        and collects the clusters to form a new cover.

        Args:
            cover: A dictionary whose values are lists of elements.
        Returns:
            Another cover, where the new sets are clusters.
        """
        listOfIndexedClusters = [ extendIndex(i,self(U)) for i,U in cover.iteritems()]
        return dict(reduce(operator.add , listOfIndexedClusters))








