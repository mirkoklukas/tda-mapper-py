


def create_d3_graph(cover, simplicies):
    keys = cover.keys()
    keyLookup = dict(zip(keys, range(len(keys))))
    d3Graph = { 
        "nodes": [ 
        	{
        		"name": key, 
        		"group": key[0], 
        		"volume": len(cover[key]), 
        		"index": key
        	}
        	for key in keys
        ],
        "links": [
        	{ 
        		"source": keyLookup[a], 
        		"target": keyLookup[b], 
        		"value": 1
        	} 
        	for (a,b) in simplicies 
        ]
    }
    return d3Graph;