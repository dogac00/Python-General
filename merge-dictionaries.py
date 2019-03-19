x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

# we have two dicts

# The desired result is to get a new dictionary (z) with the values merged, 
# and the second dict's values overwriting those from the first.
# 'a': 1, 'b': 3, 'c': 4}

def merge_two_dicts(x, y):
    """Given two dicts, merge them into a new dict as a shallow copy."""
    
    z = x.copy() # create a copy of the first dict
    z.update(y)  # update the dict with the second dict
    return z
