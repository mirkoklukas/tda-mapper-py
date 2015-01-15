

class ReferenceMap(dict, object):

    """
    A ReferenceMap is a callable class that can be applied to points in a data set.
    """

    def __init__(self, values=[], functionExpression=None, domain=None):
        """
        Initializes ReferenceMap with a list of key-value pairs, or 
        a function and a domain (where the domain it usually the data set, 
        and is needed when we want to compute the preimage of a set.)
        """
        if len(values) > 0:
            dict.__init__(self, values)
            self.domain = values.keys()
        else:
            self.func = functionExpression
            self.domain = domain

    def __call__(self, x):
        """
        Given a data point x it returns the associated value.
        """
    	if self.has_key(x):
    		return self[x]
    	elif self.func is not None:
    		y = self.func(x)
    		self[x] = y
    		return y
        else:
            msg = "There is no function expression defined " \
                  "nor does an entry with that key exist..."
            raise LookupError(msg)

    def set_domain(self, data):
        self.domain = data
        return self

    def pre_image(self, condition):
        return [ x for x in self.domain if condition(self(x))]

    def pull_back(self, conditionDict):
        """
        Given a dictionary whose values are characteristic functions 
        it returns a covering of the domain.
        """
        entries = [ (i, self.pre_image(condition)) for i,condition in conditionDict.iteritems()]
        return dict(entries)

# ------------------------------------------------------
# Some reference maps and factories
# ------------------------------------------------------

def coordinate_projection(axis, domain):
    """
    Creates a ReferenceMap that corresponds to the projection to the specified 
    coordinate axis.
    """
    return ReferenceMap(functionExpression=lambda v: v[axis], domain=domain)

# ------------------------------------------------------
# Helper to create filter conditions.
# ------------------------------------------------------

def turn_interval_into_function(I):
    """
    Given an interval, i.e. a list with two entries [a,b], 
    it returns its characteristic function.
    """
    def f_I(x):
        return I[0] <= x and x <= I[1]
    return f_I


def create_intervals(endpoints, overlap):
    """
    Creates a list of overlapping intervals, where the endpoints are 
    chosen near the entries in a list of values.
    """
    delta = overlap/2
    intervals = []
    endpoints = sorted(endpoints)
    for i in range(len(endpoints) - 1):
        intervals.append([endpoints[i] - delta, endpoints[i+1] + delta])

    return intervals


def create_functional_cover(endpoints, overlap):
    """
    Creates a dict of characteristic functions corresponding to overlapping intervals,
    whose endpoints are chosen near the entries in a list of values.
    """
    intervals = create_intervals(endpoints, overlap)
    fcts = map(turn_interval_into_function, intervals)
    funcCover = dict(zip(range(len(fcts)), fcts))
    return funcCover


def cond_and(*conditions):
    return lambda x: reduce(lambda b,f: b and f(x),conditions, True)





