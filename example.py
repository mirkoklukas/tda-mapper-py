from tdamapper.clusterfunctions import VietorisRipsClustering
from tdamapper import mapper
from tdamapper.referenceMap import create_functional_cover, coordinate_projection
import json

# ------------------------------------------------------

def write_d3graph(cover, simplicies, data, filename ):
    keys = cover.keys()
    lookup = dict(zip(keys, range(len(keys))))
    d3Graph = { 
        "count": len(data),
        "nodes": map(lambda key: {"name": key, "group": key[0], "size": len(cover[key]), "index": key} ,keys),
        "links": map(lambda (a,b): { "source": lookup[a], "target": lookup[b], "value": 1}, simplicies)
    }

    with open(filename + ".json","w") as output_file:
        output_file.write('var graph =')
        output_file.write(json.dumps(d3Graph))

# ------------------------------------------------------

def loadDataSet(filename):
    data = {}
    with open(filename) as f:
        data = json.load(f);
    return data

# ------------------------------------------------------

# Example data set
data = loadDataSet("./datasets/testDataSet_1.json")
data = [ tuple(p) for p in data ]


# Gather the mapper input
VR = VietorisRipsClustering(epsilon = 0.6) 
zAxis = coordinate_projection(axis=2, domain=data)
funcCover = create_functional_cover(endpoints=range(-12,12), overlap=0.5)

# Run the alogrithm
S = mapper(VR, zAxis, funcCover)

# Print the result
print 'Mapper result:'
print 'Cover by clusters:'
print S.nodes
print '1-simplicies:'
print S.links

# Write a json object that can be plotted with d3js.
# (open the index.html file in a browser to view a (very basic) visualization of the graph)
filename = "graph"
with open(filename + ".json","w") as output_file:
    output_file.write('var graph =')
    output_file.write(json.dumps(S.cast_to_d3js()))



