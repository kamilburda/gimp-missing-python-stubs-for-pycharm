# encoding: utf-8
# module gi.repository.cairo
# from C:\Program Files\GIMP 2.99\lib\girepository-1.0\cairo-1.0.typelib
# by generator 1.147
"""
An object which wraps an introspection typelib.

    This wrapping creates a python module like representation of the typelib
    using gi repository as a foundation. Accessing attributes of the module
    will dynamically pull them in and create wrappers for the members.
    These members are then cached on this introspection module.
"""

# imports
from _thread import _lock

import gi as __gi
import gobject as __gobject


# Variables with simple values

_namespace = 'cairo'

_version = '1.0'

__weakref__ = None

# functions

def image_surface_create(): # real signature unknown; restored from __doc__
    """ image_surface_create() """
    pass

def __delattr__(*args, **kwargs): # real signature unknown
    """ Implement delattr(self, name). """
    pass

def __dir__(*args, **kwargs): # real signature unknown
    pass

def __eq__(*args, **kwargs): # real signature unknown
    """ Return self==value. """
    pass

def __format__(*args, **kwargs): # real signature unknown
    """ Default object formatter. """
    pass

def __getattribute__(*args, **kwargs): # real signature unknown
    """ Return getattr(self, name). """
    pass

def __getattr__(*args, **kwargs): # real signature unknown
    pass

def __ge__(*args, **kwargs): # real signature unknown
    """ Return self>=value. """
    pass

def __gt__(*args, **kwargs): # real signature unknown
    """ Return self>value. """
    pass

def __hash__(*args, **kwargs): # real signature unknown
    """ Return hash(self). """
    pass

def __init_subclass__(*args, **kwargs): # real signature unknown
    """
    This method is called when a class is subclassed.
    
    The default implementation does nothing. It may be
    overridden to extend subclasses.
    """
    pass

def __init__(*args, **kwargs): # real signature unknown
    """ Might raise gi._gi.RepositoryError """
    pass

def __le__(*args, **kwargs): # real signature unknown
    """ Return self<=value. """
    pass

def __lt__(*args, **kwargs): # real signature unknown
    """ Return self<value. """
    pass

@staticmethod # known case of __new__
def __new__(*args, **kwargs): # real signature unknown
    """ Create and return a new object.  See help(type) for accurate signature. """
    pass

def __ne__(*args, **kwargs): # real signature unknown
    """ Return self!=value. """
    pass

def __reduce_ex__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __reduce__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __repr__(*args, **kwargs): # real signature unknown
    pass

def __setattr__(*args, **kwargs): # real signature unknown
    """ Implement setattr(self, name, value). """
    pass

def __sizeof__(*args, **kwargs): # real signature unknown
    """ Size of object in memory, in bytes. """
    pass

def __str__(*args, **kwargs): # real signature unknown
    """ Return str(self). """
    pass

def __subclasshook__(*args, **kwargs): # real signature unknown
    """
    Abstract classes can override this to customize issubclass().
    
    This is invoked early on by abc.ABCMeta.__subclasscheck__().
    It should return True, False or NotImplemented.  If it returns
    NotImplemented, the normal algorithm is used.  Otherwise, it
    overrides the normal algorithm (and the outcome is cached).
    """
    pass

# classes

from .Antialias import Antialias
from .Content import Content
from .Context import Context
from .Device import Device
from .Extend import Extend
from .FillRule import FillRule
from .Filter import Filter
from .FontFace import FontFace
from .FontOptions import FontOptions
from .FontSlant import FontSlant
from .FontType import FontType
from .FontWeight import FontWeight
from .HintMetrics import HintMetrics
from .HintStyle import HintStyle
from .LineCap import LineCap
from .LineJoin import LineJoin
from .Matrix import Matrix
from .Operator import Operator
from .Path import Path
from .PathDataType import PathDataType
from .Pattern import Pattern
from .Rectangle import Rectangle
from .RectangleInt import RectangleInt
from .Region import Region
from .RegionOverlap import RegionOverlap
from .ScaledFont import ScaledFont
from .Status import Status
from .SubpixelOrder import SubpixelOrder
from .Surface import Surface
from .TextClusterFlags import TextClusterFlags
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x000001a3cf569cc0>'

__path__ = [
    'C:\\Program Files\\GIMP 2.99\\lib\\girepository-1.0\\cairo-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.cairo', loader=<gi.importer.DynamicImporter object at 0x000001a3cf569cc0>)"

