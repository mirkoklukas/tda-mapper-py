# ------------------------------------------------------
# A super simple cluster algorithm. 
# ------------------------------------------------------
from ..abstractClusterFunction import AbstractClusterFunction
from ..combinatoricalHelper import extract_unordered_pairs
import math

# ------------------------------------------------------
# Some Helper. 
# ------------------------------------------------------
def euclidianDistance(xs,ys):
    return math.sqrt(sum(map(lambda (x,y): (x-y)**2,zip(xs,ys))))

def getConnectedComponent(x, G):
    if x not in G:
        raise LookupError("This is NOT a vertex of the complex!")

    visited = set([x])
    targets = G[x][:]

    while len(targets)>0:
        y = targets.pop()
        if y not in visited:
            visited.add(y)
            targets.extend(G[y])

    return visited

def getAllConnectedComponents(G):
    keys = set(G.keys())
    components = []

    while len(keys) > 0:
        x = keys.pop()
        component = getConnectedComponent(x,G)
        keys = keys - component
        components.append(component)

    return components

# ------------------------------------------------------
# The cluster class. 
# ------------------------------------------------------
class VietorisRipsClustering(AbstractClusterFunction):
    def __init__(self, epsilon, distance = euclidianDistance):
        self.epsilon = epsilon
        self.distance = distance

    def cluster(self, data):
        G = dict([(x, []) for x in data])
        pairs = extract_unordered_pairs(data)

        for (p,q) in pairs:
            if(self.distance(p, q) <= self.epsilon):
                G[p].append(q)
                G[q].append(p)

        return getAllConnectedComponents(G)



