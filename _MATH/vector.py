import math

"""
    Class for vector representation. NOT exhaustively tested (yet).
"""

class Vector:
    def __init__(self, *args):
        self.coords = list(args)
    
    @property
    def x(self):
        return self.coords[0]
    
    @property
    def y(self):
        return self.coords[1]
    
    @property
    def z(self):
        return self.coords[2]
    
    @property
    def length(self):
        return math.sqrt(sum(a**2 for a in self.coords))
    
    def normalize(self, in_place=True):
        if not in_place:
            return self / self.length
        self /= self.length
    
    def dot(self, other):
        return sum(a*b for a, b in zip(self.coords, other.coords))
    
    def cross(self, other):
        return self.x*other.y - self.y*other.x
    
    def orient(self, v1, v2):
        v3 = v1 - self
        v4 = v2 - self
        return v3.cross(v4)
    
    def rotate(self, theta: float | int, radians=False):
        """
            theta is assumed to be a value between 0-360 with radians=False. 
            Otherwise, theta is assumed to be between 0 and 2*pi.
            Rotates counter-clockwise.
        """
        if len(self.coords) != 2:
            raise Exception("Rotate is currently only implemented for 2D")
        if radians is False:
            if theta == 90:
                return self.__class__(-self.y, self.x)
            if theta == 180:
                return -self
            if theta == 270:
                return self.__class__(self.y, -self.x)
            theta = math.radians(theta)


        cos_theta = math.cos(theta)
        sin_theta = math.sin(theta)
        return self.__class__(
            self.x*cos_theta - self.y*sin_theta,
            self.x*sin_theta + self.y*cos_theta
        )
    
    def dist(self, other):
        return math.dist(self.coords, other.coords)

    def __mul__(self, other):
        if isinstance(other, Vector):
            raise Exception("Not implemented")
        elif isinstance(other, (int, float)):
            return self.__class__(*(a*other for a in self.coords))
        
    def __truediv__(self, other):
        if isinstance(other, Vector):
            raise Exception("Not implemented")
        elif isinstance(other, (int, float)):
            return self.__class__(*(a/other for a in self.coords))

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise Exception()
        return self.__class__(*(a+b for a, b in zip(self.coords, other.coords)))
    
    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise Exception()
        return self.__class__(*(a-b for a, b in zip(self.coords, other.coords)))

    def __neg__(self):
        return self.__class__(*(-a for a in self.coords))

    def __imul__(self, other):
        if isinstance(other, Vector):
            raise Exception("Not implemented")
        for i in range(len(self.coords)):
            self.coords[i] *= other
        return self

    def __itruediv__(self, other):
        if isinstance(other, Vector):
            raise Exception("Not implemented")
        for i in range(len(self.coords)):
            self.coords[i] /= other
        return self

    def __iadd__(self, other):
        for i in range(len(self.coords)):
            self.coords[i] += other.coords[i]
        return self

    def __isub__(self, other):
        for i in range(len(self.coords)):
            self.coords[i] -= other.coords[i]
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __iter__(self):
        return iter(self.coords)

    def __repr__(self):
        return str(self.coords)