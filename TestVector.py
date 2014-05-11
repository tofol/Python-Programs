# /usr/bin/env python3
# -*- coding: utf-8 -*-


from Vector import Vector
import math
from math import pi


def main():
    V1 = Vector(3, 2, -1, 5)
    V2 = Vector(4, 5, -2, -5)
    V3 = Vector()
    V4 = Vector(5, 6.7, 8, 4)
    print(V1)
    print(V2)
    print(V3)
    print(V1 + V2)
    print(V1 + V2 + V4)
    print(V1 - V2)
    print(V1 * V2)
    print(3 * V1)
    print(V1 / V2)
    print(V1 / 3)
    print(pow(V1, 2))
    print(-V1)
    print(V1.inner(V2))
    print(len(V1))
    print(V1[2])
    print(V1.norm())
    print(V1.pnorm(3))
    print(V1.infnorm())
    print(V1.normalize())
    print(V1.anglerad(V2))
    print(V1.angledeg(V2))
    print(Vector(3, 2, -1).prodvect(Vector(4, 5, 4)))
    print(Vector(3, 2, -1).areaparal(Vector(4, 5, 4)))
    print(Vector(3, 2, -1).prodmixt(Vector(4, 5, 4), Vector(1, 2, 1)))
    print(Vector(3, 2, -1).volparal(Vector(4, 5, 4), Vector(1, 2, 1)))
    print(V1.translate(3))
    print(Vector(3, 2).rot2d(45))
    print(Vector(3, 2, -1).rot3d(Vector(1, 0, 0), 45))
    print(Vector(3, 2, -1).normalprodvect(Vector(3, 1, 3)))
    print(Vector(3, 2).rect2pol())
    print(Vector(3, 2).rect2poldeg())
    print(Vector(3, pi).pol2rect())
    print(Vector(3, 180).pol2rectdeg())
    print(Vector(3, 2, -5).rect2cyl())
    print(Vector(3, 2, -5).rect2cyldeg())
    print(Vector(5.0, 0.927295218002, 5).cyl2rect())
    print(Vector(5.0, 53.1301023542, 5).cyl2rectdeg())
    print(Vector(3, 2, -5).rect2sph())
    print(Vector(3, 2, -5).rect2sphdeg())
    print(Vector(3, 2, -5).sph2rect())
    print(Vector(3, 45, 35).sph2rectdeg())
    print(Vector(3, 2, -5).tofloat())
    print(Vector(3., 2., -5.).toint())
    print(V1.isorthog(V2))
    print(Vector(1, 0).isorthog(Vector(0, 1)))
    print(V1.isunit())
    print(V1.projection(V2))

if __name__ == '__main__':
    main()
