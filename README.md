# TDA-Mapper-py

[![Build Status](https://travis-ci.org/mirkoklukas/tda-mapper-py.svg?branch=master)](https://travis-ci.org/mirkoklukas/tda-mapper-py)

A straightforward implementation of the mapper construction by Carlsson-Memoli-Singh. I wrote a little blog post about it at http://mapsfunctionsandarrows.blogspot.de

## Example


``` python
from tdamapper.clusterfunctions import VietorisRipsClustering
from tdamapper import mapper
from tdamapper.referenceMap import create_functional_cover, coordinate_projection
import json

# Example data set
with open("./example/dataset.json") as f:
	data = json.load(f);
	data = [ tuple(p) for p in data ]

# Gather the mapper input
VR = VietorisRipsClustering(epsilon = 0.6) 
zAxis = coordinate_projection(axis=2, domain=data)
funcCover = create_functional_cover(endpoints=range(-12,12), overlap=0.5)

# Run the alogrithm
result = mapper(VR, zAxis, funcCover)

```

Below you see a visualization of the mapper result. The graph is colored by the values of ```zAxis```, the projection on the z-axis. The size of the nodes
reflects the size of the associated clusters.

The take away should be that there are actually two separate branches growing out of a bigger cluster.
You shouldn't focus to much on the fact that the two branches cross each other. Although it reflects the reality of the situation pretty well, it is rather a bi-product of the fact that the data set lives in so few dimensions.  

![The result of the mapper construction](https://github.com/mirkoklukas/tda-mapper-py/blob/master/example/result.png "The result of the mapper construction")

And indeed (what a terrible example it would have been if that was not the case) looking at a 3d plot of the original dataset we see that this reflects the shape pretty well. 

![An example data set](https://github.com/mirkoklukas/tda-mapper-py/blob/master/example/dataset.png "An example data set")