from mapper.clusterfunctions import VietorisRipsClustering
from mapper import mapper
from mapper.referenceMap import create_functional_cover, coordinate_projection
import matplotlib.pyplot as plt
import math
import json

def plot_data(data):
    plt.scatter(map(lambda x: x[0], data), map(lambda x: x[1], data))
    plt.show()

def write_graph(graph):
	d3Graph = {
	    "nodes": [],
	    "links": []
	}
	filename = "graph"

	with open(filename + ".json","w") as output_file:
	    output_file.write(json.dumps(d3Graph))



# Example data set
n = 40
data = [ (math.cos(x), math.sin(x)) for x in [ k*2*math.pi/n for k in range(n)] ]


VR = VietorisRipsClustering(epsilon = 0.3) 
yAxis = coordinate_projection(axis=1, domain=data)
funcCover = create_functional_cover(endpoints=[-1.5,-1,-0.5,0,0.5,1], overlap=0.2)

S = mapper(VR, yAxis, funcCover)

print 'Mapper result:'
print S
