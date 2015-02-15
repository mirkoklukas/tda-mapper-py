from tdamapper.clusterfunctions import VietorisRipsClustering
from tdamapper import mapper
from tdamapper.referenceMap import create_functional_cover, coordinate_projection
import json


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
result = mapper(VR, zAxis, funcCover)

# Print the result
print 'Mapper result:'
print 'Cover by clusters:'
print result.nodes
print '1-simplicies:'
print result.links

# Write a json object that can be plotted with d3js.
# (open the index.html file in a browser to view a (very basic) visualization of the graph)
filename = "graph"
with open(filename + ".json","w") as output_file:
    output_file.write('var graph =')
    output_file.write(json.dumps(result.cast_to_d3js()))



