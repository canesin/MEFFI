# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 21:09:50 2014

@author: Fabio
"""
from mayavi import mlab
import scipy.spatial as spa
import scipy as sp
import sympy as sy


def recgrid(xmin=0, xmax=1, ymin=0, ymax=1, ni=10, nj=10):
    """
    Gera malha triangular regular retangular de ni x nj nós.
    """
    x, y = sp.mgrid[xmin:xmax:complex(0, ni), ymin:ymax:complex(0, nj)]
    return spa.Delaunay(sp.vstack((x.flatten(), y.flatten())).T)

def viewgrid(grid, scalar=None, mode='wireframe'):
    """
    Mostra grid
    """
    return mlab.triangular_mesh(grid.points[:, 0],
                                grid.points[:, 1],
                                sp.zeros(len(grid.points[:, 0])),
                                grid.simplices,
                                scalars=scalar,
                                representation=mode)

malha = recgrid()
viewgrid(malha)
