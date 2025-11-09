# encoding: utf-8
# module gi.repository.GDesktopEnums
# from C:/Program Files/GIMP 3/lib/girepository-1.0\GDesktopEnums-3.0.typelib
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

import gobject as __gobject


# Variables with simple values

_namespace = 'GDesktopEnums'

_version = '3.0'

__weakref__ = None

# functions

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

def __getstate__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
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

from .AccentColor import AccentColor
from .BackgroundShading import BackgroundShading
from .BackgroundStyle import BackgroundStyle
from .ClockFormat import ClockFormat
from .ColorScheme import ColorScheme
from .DeviceSendEvents import DeviceSendEvents
from .FocusMode import FocusMode
from .FocusNewWindows import FocusNewWindows
from .FontAntialiasingMode import FontAntialiasingMode
from .FontHinting import FontHinting
from .FontRendering import FontRendering
from .FontRgbaOrder import FontRgbaOrder
from .LocationAccuracyLevel import LocationAccuracyLevel
from .MagnifierCaretTrackingMode import MagnifierCaretTrackingMode
from .MagnifierFocusTrackingMode import MagnifierFocusTrackingMode
from .MagnifierMouseTrackingMode import MagnifierMouseTrackingMode
from .MagnifierScreenPosition import MagnifierScreenPosition
from .MouseDwellDirection import MouseDwellDirection
from .MouseDwellMode import MouseDwellMode
from .PadButtonAction import PadButtonAction
from .PointerAccelProfile import PointerAccelProfile
from .PointingStickScrollMethod import PointingStickScrollMethod
from .ProxyMode import ProxyMode
from .ScreensaverMode import ScreensaverMode
from .StylusButtonAction import StylusButtonAction
from .TabletMapping import TabletMapping
from .TitlebarAction import TitlebarAction
from .ToolbarIconSize import ToolbarIconSize
from .ToolbarStyle import ToolbarStyle
from .TouchpadClickMethod import TouchpadClickMethod
from .TouchpadHandedness import TouchpadHandedness
from .TouchpadTapButtonMap import TouchpadTapButtonMap
from .UsbProtection import UsbProtection
from .VisualBellType import VisualBellType
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x000001f81e092090>'

__path__ = []

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.GDesktopEnums', loader=<gi.importer.DynamicImporter object at 0x000001f81e092090>)"

