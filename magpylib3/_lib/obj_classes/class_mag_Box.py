"""Magnet Box class code"""

import numpy as np
from magpylib3._lib.obj_classes.class_BaseGeo import BaseGeo
from magpylib3._lib.obj_classes.class_Collection import Collection
from magpylib3._lib.fields.field_BHwrapper import getB, getH

class Box(BaseGeo):
    """ Homogeneous Cuboid magnet.

    init_state: the geometric center is in the CS origin, the sides
        of the box are parallel to the x/y/z basis vectors
    
    ### Properties
    - mag (vec3): Magnetization vector (remanence field) of magnet
        in units of mT.
    - dim (vec3): Dimension/Size of the Cuboid with sides [a,b,c] 
        in units of mm.
    - pos (vec3): Position of the geometric center of the magnet 
        in units of mm. Defaults to (0,0,0).
    - rot (rotation input): Relative rotation of magnet to init_state.
        Input can either be a pair (angle, axis) with angle a scalar 
        given in deg and axis an arbitrary 3-vector, or a 
        scipy..Rotation object. Defaults to (0,0,0) rotation vector.

    ### Methods
    - move: move magnet by argument vector
    - rotate: rotate magnet
    - display: graphically display magnet
    - getB: compute B-field of magnet
    - getH: compute H-field of magnet

    ### Returns:
    - (Box source object)

    ### Info
    Addition of sources returns a Collection.
    """

    def __init__(self, 
        mag = '(mx,my,mz)', 
        dim = '(a,b,c)',
        pos = (0,0,0), 
        rot = None
        ):

        # inherit base_geo class
        BaseGeo.__init__(self, pos, rot)

        # set mag and dim attributes
        self.mag = mag
        self.dim = dim

    # properties ----------------------------------------------------
    @property
    def mag(self):
        """ magnet magnetization in mT
        """
        return self._mag

    @mag.setter
    def mag(self, value):
        """ set magnetization vector, vec3, mT
        """
        self._mag = np.array(value,dtype=np.float)


    @property
    def dim(self):
        """ box dimension (a,b,c) in mm
        """
        return self._dim

    @dim.setter
    def dim(self, value):
        """ set box dimension (a,b,c), vec3, mm
        """
        self._dim = np.array(value,dtype=np.float)


    # dunders -------------------------------------------------------
    def __add__(self, source):
        """ sources add up to a Collection object
        """
        return Collection(self,source)


    # methods -------------------------------------------------------
    def getB(self, pos_obs):
        """ Compute B-field of magnet at observer positions.

        ### Args:
        - pos_obs (N1 x N2 x ... x 3 vec): single position or set of 
            observer positions in units of mm.

        ### Returns:
        - (N1 x N2 x ... x 3 ndarray): B-field at observer positions
            in units of mT.
        """
        B = getB(self, pos_obs=pos_obs)
        return B


    def getH(self, pos_obs):
        """ Compute H-field of source at observer positions.

        ### Args:
        - pos_obs (N1 x N2 x ... x 3 vec): single position or set of 
            observer positions in units of mm.

        ### Returns:
        - (N1 x N2 x ... x 3 ndarray): H-field at observer positions
            in units of kA/m.
        """
        H = getH(self, pos_obs=pos_obs)
        return H
