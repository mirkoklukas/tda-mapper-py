from tdamapper.referenceMap import *
import pytest


# ------------------------------------------------------

def test_reference_map_with_values():
    values = [
        (1,0),
        (2,0),
        (3,0),
        (4,1),
        (5,1),
        (6,1)
    ]
    refmap = ReferenceMap(values)

    with pytest.raises(LookupError):
        refmap(100)

    assert refmap(1) == 0
    assert refmap(5) == 1

# ------------------------------------------------------


def test_reference_map_with_function():
    def f(x):
        return x*2;

    refmap = ReferenceMap(functionExpression=f, domain=range(100))

    assert refmap(1) == 2
    assert refmap(5) == 10

# ------------------------------------------------------

def test_reference_map_methods():

    refmap = ReferenceMap(functionExpression=lambda x: x*0.5, domain=range(100))
    funcCover = { 
        "lower": lambda x: x < 10,
        "higher": lambda x: x > 10
        }

    assert refmap.pre_image(lambda x: 0<= x and x < 10) == range(20)
    assert refmap.pull_back(funcCover) == { 
        "lower": range(20),
        "higher": range(21,100)
        }

# ------------------------------------------------------

# ------------------------------------------------------

# ------------------------------------------------------

# ------------------------------------------------------

# ------------------------------------------------------





