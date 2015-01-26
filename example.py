from mapper.clusterfunctions import VietorisRipsClustering
from mapper import mapper
from mapper.referenceMap import create_functional_cover, coordinate_projection
import matplotlib.pyplot as plt
import math
import json

def plot_data(data):
    plt.scatter(map(lambda x: x[0], data), map(lambda x: x[1], data))
    plt.show()

def write_d3graph(keys, simplicies,filename):
    lookup = dict(zip(keys, range(len(keys))))
    d3Graph = { 
        "nodes": map(lambda key: {"name": key, "group": key[0]} ,keys),
        "links": map(lambda (a,b): { "source": lookup[a], "target": lookup[b], "value": 1}, simplicies)
    }

    with open(filename + ".json","w") as output_file:
        output_file.write('var graph =')
        output_file.write(json.dumps(d3Graph))



# Example data set
n = 100
m = 400
circle = [ (math.cos(x), math.sin(x)) for x in [ k*2*math.pi/n for k in range(n)] ]
cosine = [ (x , math.cos(x)) for x in [ (float(k)/m)*20 for k in range(m)] ]
data = circle + cosine



VR = VietorisRipsClustering(epsilon = 0.1) 
yAxis = coordinate_projection(axis=1, domain=data)
funcCover = create_functional_cover(endpoints=[-1.1,-0.5,0,0.5,1.1], overlap=0.1)


S = mapper(VR, yAxis, funcCover)
print 'Mapper result:'
print 'Cover by clusters:'
print S[0]
print '1-simplicies:'
print S[1]

write_d3graph(S[0].keys(),S[1], 'graph')


