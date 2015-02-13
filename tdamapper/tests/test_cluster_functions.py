from tdamapper.abstractClusterFunction import AbstractClusterFunction
from tdamapper.clusterfunctions.vietorisRipsClustering import *

# ------------------------------------------------------

def test_abstract_cluster_function():
    class StupidClustering(AbstractClusterFunction):
        def cluster(self, data):
            return [data[:len(data)/2], data[len(data)/2:]]

    clusterer = StupidClustering()

    cover = {
        1: [1, 2, 3, 4],
        "two": [2, 3, {5: 5}, 6]
    }
    expectedPushForward = {
        (1, 0): [1, 2],
        (1, 1): [3, 4],
        ("two", 0): [2, 3],
        ("two", 1): [{5: 5}, 6]
    }

    assert [] == clusterer([])
    assert expectedPushForward == clusterer.push_forward(cover)
    assert {} == clusterer.push_forward({})

# ------------------------------------------------------

def test_vietoris_rips_clustering_with_given_distance():
    VR = VietorisRipsClustering(epsilon=2.0, distance=lambda a,b: abs(a-b))
    
    clusters = VR([1,2,3,4,5,10,12,20])
    expected = [
        set([1,2,3,4,5]),  
        set([10,12]), 
        set([20])
        ]

    assert [] == VR([])

    for c in clusters:
        assert c in expected
    for c in expected:
        assert c in clusters


# ------------------------------------------------------

def test_vietoris_rips_clustering_with_default_distance():
    VR = VietorisRipsClustering(epsilon=1.6)

    clusters = VR([
            (0,0),
            (1,0),
            (1,1),
            (4,0),
            (4,.1),
            (3.5,0.4)
        ])
    expected = [
        set([(0,0), (1,0), (1,1)]),  
        set([(4,0), (3.5,0.4), (4,0.1)])
        ]

    assert [] == VR([])

    for c in clusters:
        assert c in expected
    for c in expected:
        assert c in clusters

# ------------------------------------------------------

def test_graph_functions():
    G = {
        1:[2,3],
        2:[1,3],
        3:[1,2],
        4:[5],
        5:[4],
        6:[]    
    }

    assert set([1,2,3]) == getConnectedComponent(1,G)

    components = getAllConnectedComponents(G)
    expected = [set([1,2,3]), set([4,5]), set([6])] 

    for c in components:
        assert c in expected
    for c in expected:
        assert c in components


# ------------------------------------------------------

def test_euclidian_distance():
    assert math.sqrt(2) == euclidianDistance((1,0,0),(0,1,0))
    assert math.sqrt(2) == euclidianDistance([1,0,0],[0,0,1])

# ------------------------------------------------------





