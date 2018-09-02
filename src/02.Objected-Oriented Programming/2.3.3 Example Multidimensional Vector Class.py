# 2.3.3 Example: Multidimensional Vector Class

class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self,d):
        """Create d-dimensional vector of zeros."""
        self._coords = [0] *d

    def __len_(self):
        """Return the dimension of the ventor."""
        return len(self._coords)

    def __getitem__(self,j):
        """Return jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self,j,val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self,other):
        """Return sum of two ventors."""
        if len(self._coords) != len(other._coords): # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self._coords))      # start with ventor of zeros
        for j in range(len(self._coords)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self,other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self,other):
        """Return True if vector differs from other."""
        return not self == other    # rely on existing __eq__ definition

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation

#----------------------------- my main function -----------------------------
my_str = Vector(6)
other = Vector(6)
for i in range(6):
    my_str[i] = i * (i + 1)
print('0: my_str = ',my_str._coords)
print('1: my_str[3] =',my_str.__getitem__(3))
k = Vector(6)
for i in range(6):
    k[i] += i
print('2: k =',k._coords)
k.__add__(my_str)
print('3: add =',k.__add__(my_str)._coords)
print('4: other',other)
print('5: my_str == other?',my_str.__eq__(other))