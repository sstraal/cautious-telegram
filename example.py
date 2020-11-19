import numpy as np

def add(a,b):
    return a + b

def test_add():
    assert add(2,3) == 5
    assert add("space", "ship") == "spaceship"

# uncomment the following test in step 5
def test_subtract():
    assert np.subtract(2, 3) == -1

