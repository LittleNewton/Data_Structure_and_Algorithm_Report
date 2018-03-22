# 2.3.3 Example: Multidimensional Vector Class

class Vector:
    def __init__(self,d):
        self._coords = [0] *d
    def __len_(self):
        return len(self._coords)
    def __getitem__(self,j):
        return self._coords[j]
    def __setitem__(self,j,val):
        self._coords[j] = val
    def __add__(self,other):
        if len(self._coords) != len(other._coords):
            raise ValueError('dimensions must agree')
        result = Vector(len(self._coords))
        for j in range(len(self._coords)):
            result[j] = self[j] + other[j]
        return result
    def __eq__(self,other):
        return self._coords == other._coords
    def __ne__(self,other):
        return not self == other
    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'

#------------------------------ my main function ------------------------------
my_str = Vector(6)
for i in range(6):
    my_str[i] = i * (i + 1)
print('0: my_str = ',my_str._coords)
print('1: my_str[3] =',my_str.__getitem__(3))
k = Vector(6)
for i in range(6):
    k[i] += i
print('2: k =',k._coords)
k._coords.__add__(my_str._coords)
print('3: add =',k.__add__(my_str)._coords)