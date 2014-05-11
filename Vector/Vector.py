# /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on Wed May  7 21:21:21 2014

@author: tobal
'''

from math import sqrt, acos, degrees, radians, cos, sin, fsum, hypot, atan2


class Vector(tuple):

    '''"Class to calculate the usual operations with vectors in bi and
    tridimensional coordinates. Too with n-dimmensinal.'''
    # __slots__=('V') #It's not possible because V is a variable list of param.
    def __new__(cls, *V):
        '''The new method, we initialize the coordinates of a vector.
        You can initialize a vector for example: V = Vector() or
        V = Vector(a,b) or V = Vector(v1, v2, ..., vn)'''
        if not V:
            V = (0, 0)
        elif len(V) == 1:
            raise ValueError('A vector must have at least 2 coordinates.')
        return tuple.__new__(cls, V)

    def __add__(self, V):
        '''The operator sum overloaded. You can add vectors writing V + W,
        where V and W are two vectors.'''
        if len(self) != len(V):
            raise IndexError('Vectors must have same dimmensions.')
        else:
            added = tuple(a + b for a, b in zip(self, V))
            return Vector(*added)

    __radd__ = __add__

    def __sub__(self, V):
        '''The operator subtraction overloaded. You can subtract vectors writing
        V - W, where V and W are two vectors.'''
        if len(self) != len(V):
            raise IndexError('Vectors must have same dimmensions.')
        else:
            subtracted = tuple(a - b for a, b in zip(self, V))
            return Vector(*subtracted)

    def __rsub__(self, V):
        '''The operator subtraction overloaded. You can subtract vectors writing
        W - V, where V and W are two vectors.'''
        if len(self) != len(V):
            raise IndexError('Vectors must have same dimmensions.')
        else:
            subtracted = tuple(b - a for a, b in zip(self, V))
            return Vector(*subtracted)        

    def __mul__(self, V):
        '''The operator mult overloaded. You can multipy 2 vectors coordinate
         by coordinate.'''
        if type(V) == type(self):
            if len(self) != len(V):
                raise IndexError('Vectors must have same dimmensions')
            else:
                multiplied = tuple(a * b for a, b in zip(self, V))
        elif isinstance(V, type(1)) or isinstance(V, type(1.0)):
            multiplied = tuple(a * V for a in self)
        return Vector(*multiplied)

    __rmul__ = __mul__

    def __truediv__(self, V):
        if type(V) == type(self):
            if len(self) != len(V):
                raise IndexError('Vectors must have same dimmensions.')
            if 0 in V:
                raise ZeroDivisionError('Division by 0.')
            divided = tuple(a / b for a, b in zip(self, V))
        elif isinstance(V, int) or isinstance(V, float):
            divided = tuple(a / V for a in self)
        return Vector(*divided)

    __rtruediv__ = __truediv__

    def __pow__(self, n):
        '''The operator pow overloaded. You can powering vectors writing
         V ** n, where V is a vector, and n is the power. If V = (a, b), then
         V ** n calculates (a ** n, b ** n)'''
        powered = tuple(a ** n for a in self)
        return Vector(*powered)

    def __iadd__(self, t):
        sumplus = tuple(a + t for a in self)
        return Vector(*sumplus)

    def __isub__(self, t):
        subminus = tuple(a - t for a in self)
        return Vector(*subminus)

    def __imul__(self, t):
        mulplus = tuple(a * t for a in self)
        return Vector(*mulplus)

    def __itruediv__(self, t):
        divplus = tuple(a / t for a in self)
        return Vector(*divplus)

    def __ipow__(self, t):
        powplus = tuple(a ** t for a in self)
        return Vector(*powplus)

    def __neg__(self):
        '''The operator negative overloaded. If V is a vector, you can
        calculate -V, the vector V changed its sign in its coordinates.'''
        opposite = tuple(-1 * a for a in self)
        return Vector(*opposite)

    def tofloat(self):
        ''' It converts a vector to float vector.'''
        tofloatin = tuple(float(a) for a in self)
        return Vector(*tofloatin)

    def toint(self):
        ''' It converts a vector to integer vector.'''
        tointeger = tuple(int(a) for a in self)
        return Vector(*tointeger)

    def inner(self, V):
        ''' Returns the dot product (inner product or scalar product) of self
        and V vector
        '''
        return fsum(a * b for a, b in zip(self, V))

    def isorthog(self, V):
        '''Return if two vectors are or not orthogonals.'''
        return self.inner(V) == 0

    def norm(self):
        '''Returns the norm (length, magnitude) of the vector'''
        return sqrt(fsum(comp ** 2 for comp in self))

    def isunit(self):
        '''Returns if a vector has got norm equal 1 or not respect the
        euclidian norm.'''
        return self.norm() == 1

    def pnorm(self, p):
        '''Returns the p-norm of the vector'''
        return pow(fsum(abs(comp) ** p for comp in self), p)

    def infnorm(self):
        '''Returns the infinity norm of the vector'''
        return max(abs(comp) for comp in self)

    def normalize(self):
        '''Returns a normalized unit vector'''
        norm = self.norm()
        normed = tuple(comp / norm for comp in self)
        return Vector(*normed)

    def projection(self, V):
        ''' Returns the projection of 2 vectors.'''
        if len(self) != len(V):
            raise IndexError('Two vectors must have the same dimmension.')
        else:
            A = self.inner(V) / self.inner(self)
            return A * self

    def anglerad(self, V):
        ''' Returns the angle for 2 vectors in radians mode.'''
        angle = acos(self.inner(V) / (self.norm() * V.norm()))
        return angle

    def angledeg(self, V):
        ''' Returns the angle for 2 vectors in radians mode.'''
        angle = acos(self.inner(V) / (self.norm() * V.norm()))
        return degrees(angle)

    def prodvect(self, V):
        ''' Find out the vectorial product between two vectors'''
        if len(self) > 3 or len(V) > 3 or len(self) != len(V):
            raise IndexError('Sorry, two vectors must be 3D dimmensional.')
        else:
            e1 = Vector(1, 0, 0)
            e2 = Vector(0, 1, 0)
            e3 = Vector(0, 0, 1)
            det1 = self[1] * V[2] - self[2] * V[1]
            det2 = self[0] * V[2] - self[2] * V[0]
            det3 = self[0] * V[1] - self[1] * V[0]
            prodv = det1 * e1 - det2 * e2 + det3 * e3
            return prodv

    def areaparal(self, V):
        '''Find out the area of a paralelogram from 2 vectors'''
        return (self.prodvect(V)).norm()

    def normalprodvect(self, V):
        ''' Find out n = (a x b) / |a x b|, normal unit vector to the plane.'''
        return self.prodvect(V) / (self.prodvect(V)).norm()

    def prodmixt(self, V, W):
        ''' Find out the mixt product between three vectors'''
        if len(self) > 3 or len(V) > 3 or len(W) > 3 or len(self) != len(V)\
                or len(self) != len(W) or len(V) != len(W):
            raise IndexError('Sorry, three vectors must be 3D dimmensional.')
        else:
            det1 = V[1] * W[2] - V[2] * W[1]
            det2 = V[0] * W[2] - V[2] * W[0]
            det3 = V[0] * W[1] - V[1] * W[0]
            prodm = det1 * self[0] - det2 * self[1] + det3 * self[2]

            return prodm

    def volparal(self, V, W):
        '''Find out the paral.lepiped from three vectors'''
        return abs(self.prodmixt(V, W))

    def translate(self, t):
        ''' Find out the transalation vector t units.'''
        V = list(self)
        for i in range(0, len(V)):
            V[i] += t
        return Vector(*V)

    def rot2d(self, deg):
        ''' Find out the rotated vector a certain number of degrees in 2D.'''
        if len(self) != 2:
            raise IndexError('Sorry, vector must be 2D dimmensional.')
        else:
            rad = radians(deg)
            rot1 = Vector(cos(rad), -sin(rad))
            rot2 = Vector(sin(rad), cos(rad))
            p1 = rot1.inner(self)
            p2 = rot2.inner(self)
            rotated = Vector(p1, p2)
            return rotated

    def rot3d(self, N, deg):
        ''' Find out the rotated vector a certain number of degrees in 3D.'''
        if len(self) != 3:
            raise IndexError('Sorry, vector must be 3D dimmensional.')
        else:
            rad = radians(deg)

            c11 = (1 - N[0] ** 2) * cos(rad) + N[0] ** 2
            c12 = -N[0] * N[1] * cos(rad) - N[2] * sin(rad)
            c13 = -N[0] * N[2] * cos(rad) + N[1] * sin(rad)
            rot1 = Vector(c11, c12, c13)

            c21 = -N[0] * N[1] * cos(rad) + N[2] * sin(rad)
            c22 = (1 - N[1] ** 2) * cos(rad) + N[1] ** 2
            c23 = -N[1] * N[2] * cos(rad) - N[0] * sin(rad)
            rot2 = Vector(c21, c22, c23)

            c31 = -N[0] * N[2] * cos(rad) - N[1] * sin(rad)
            c32 = -N[1] * N[2] * cos(rad) + N[0] * sin(rad)
            c33 = (1 - N[2] ** 2) * cos(rad) + N[2] ** 2
            rot3 = Vector(c31, c32, c33)

            p1 = rot1.inner(self)
            p2 = rot2.inner(self)
            p3 = rot3.inner(self)
            rotated = Vector(p1, p2, p3)
            return rotated

    def rect2pol(self):
        ''' Converts rectangular coordinates in a 2D vector to polar
        oordinates in radians way.'''
        if len(self) != 2:
            raise ValueError("The vector must be a 2D.")
        else:
            self0 = hypot(self[0], self[1])
            if self[0] == 0.:
                raise ZeroDivision("Error division, the denominator is zero.")
            else:
                self1 = atan2(self[1], self[0])
        return Vector(self0, self1)

    def rect2poldeg(self):
        ''' Converts rectangular coordinates in a 2D vector to polar
        coordinates in sexagesimal degrees way.'''
        V = self.rect2pol()
        V0 = V[0]
        V1 = degrees(V[1])
        return Vector(V0, V1)

    def pol2rect(self):
        ''' Converts polar coordinates in a 2D vector to rectangular
        coordinates in radians way.'''
        if len(self) != 2:
            raise ValueError("The vector must be a 2D.")
        else:
            if self[0] < 0.:
                raise ValueError("The radius must be positive.")
            else:
                self0 = self[0] * cos(self[1])
            self1 = self[0] * sin(self[1])
        return Vector(self0, self1)

    def pol2rectdeg(self):
        ''' Converts rectangular coordinates in a 2D vector to polar
        coordinates in sexagesimal degrees way.'''
        if len(self) != 2:
            raise ValueError("The vector must be a 2D.")
        else:
            if self[0] < 0.:
                raise ValueError("The radius must be positive.")
            else:
                self0 = self[0] * cos(radians(self[1]))
            self1 = self[0] * sin(radians(self[1]))
        return Vector(self0, self1)

    def rect2cyl(self):
        ''' Converts rectangular coordinates in a 3D vector to cylindrical
        coordinates in radians way.'''
        if len(self) != 3:
            raise ValueError("The vector must be a 3D.")
        else:
            V = Vector(self[0], self[1])
            W = V.rect2pol()
        return Vector(W[0], W[1], self[2])

    def rect2cyldeg(self):
        ''' Converts rectangular coordinates in a 3D vector to cylindrical
        coordinates in sexagesimal degrees way.'''
        if len(self) != 3:
            raise ValueError("The vector must be a 3D.")
        else:
            V = Vector(self[0], self[1])
            W = V.rect2poldeg()
        return Vector(W[0], W[1], self[2])

    def cyl2rect(self):
        ''' Converts cylindrical coordinates in a 3D vector to rectangular
        coordinates in radians way.'''
        if len(self) != 3:
            raise ValueError("The vector must be a 3D.")
        else:
            V = Vector(self[0], self[1])
            W = V.pol2rect()
        return Vector(W[0], W[1], self[2])

    def cyl2rectdeg(self):
        ''' Converts cylindrical coordinates in a 3D vector to rectangular
        coordinates in sexagesimal degrees way.'''
        if len(self) != 3:
            raise ValueError("The vector must be a 3D.")
        else:
            V = Vector(self[0], self[1])
            W = V.pol2rectdeg()
        return Vector(W[0], W[1], self[2])

    def rect2sph(self):
        ''' Converts rectangular coordinates in a 3D vector to spherical
        coordinates in radians way.'''
        if len(self) != 3:
            raise ValueError("The vector must be a 3D.")
        else:
            self0 = sqrt(pow(self[0], 2.) +
                         pow(self[1], 2.) + pow(self[2], 2.))
            self1 = atan2(sqrt(pow(self[0], 2.) + pow(self[1], 2.)), self[2])
            self2 = atan2(self[1], self[0])
            return Vector(self0, self1, self2)

    def rect2sphdeg(self):
        ''' Converts rectangular coordinates in a 3D vector to spherical
         coordinates in sexagesimal degrees way.'''
        if len(self) != 3:
            raise ValueError("The vector must be a 3D.")
        else:
            V = self.rect2sph()
            return Vector(V[0], degrees(V[1]), degrees(V[2]))

    def sph2rect(self):
        ''' Converts spherical coordinates in a 3D vector to rectangular
         coordinates in radians way.'''
        if len(self) != 3:
            raise IndexError('The vector must be 3D.')
        if self[0] < 0:
            raise ValueError('The radius must be positive.')
        else:
            self0 = self[0] * sin(self[1]) * cos(self[2])
            self1 = self[0] * sin(self[1]) * sin(self[2])
            self2 = self[0] * cos(self[1])
            return Vector(self0, self1, self2)

    def sph2rectdeg(self):
        ''' Converts spherical coordinates in a 3D vector to rectangular
         coordinates in sexagesimal degrees way.'''
        if len(self) != 3:
            raise IndexError('The vector must be 3D.')
        if self[0] < 0:
            raise ValueError('The radius must be positive.')
        else:
            self0 = self[0] * sin(radians(self[1])) * cos(radians(self[2]))
            self1 = self[0] * sin(radians(self[1])) * sin(radians(self[2]))
            self2 = self[0] * cos(radians(self[1]))
            return Vector(self0, self1, self2)

    def cyl2sph(self):
        ''' Converts cylindrical coordinates in a 3D vector to spherical
         coordinates.'''
        if len(self) != 3:
            raise IndexError('The vector must be 3D.')
        if self[0] < 0:
            raise ValueError('The radius must be positive.')
        else:
            self0 = sqrt(pow(self[0], 2.) + pow(self[2], 2.))
            self1 = atan2(self[0], self[2])
            self2 = self[1]
            return Vector(self0, self1, self2)

    def sph2cyl(self):
        ''' Converts spherical coordinates in a 3D vector to cylindrical
         coordinates.'''
        if len(self) != 3:
            raise IndexError('The vector must be 3D.')
        if self[0] < 0:
            raise ValueError('The radius must be positive.')
        else:
            self0 = self[0] * sin(self[1])
            self1 = self[2]
            self2 = self[0] * cos(self[1])
            return Vector(self0, self1, self2)

    def sph2cyldeg(self):
        ''' Converts spherical coordinates in a 3D vector to cylindrical
         coordinates in sexagesimal degrees way.'''
        if len(self) != 3:
            raise IndexError('The vector must be 3D.')
        if self[0] < 0:
            raise ValueError('The radius must be positive.')
        else:
            self0 = self[0] * sin(radians(self[1]))
            self1 = self[2]
            self2 = self[0] * cos(radians(self[1]))
            return Vector(self0, self1, self2)
