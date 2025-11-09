# encoding: utf-8
# module gi.repository.Atk
# from C:/Program Files/GIMP 3/lib/girepository-1.0\Atk-1.0.typelib
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
import gi.overrides.GObject as __gi_overrides_GObject
import gobject as __gobject


# Variables with simple values

BINARY_AGE = 25411

INTERFACE_AGE = 1

MAJOR_VERSION = 2

MICRO_VERSION = 1

MINOR_VERSION = 54

VERSION_MIN_REQUIRED = 2

_namespace = 'Atk'

_version = '1.0'

__weakref__ = None

# functions

def attribute_set_free(attrib_set): # real signature unknown; restored from __doc__
    """ attribute_set_free(attrib_set:list) """
    pass

def focus_tracker_notify(p_object): # real signature unknown; restored from __doc__
    """ focus_tracker_notify(object:Atk.Object) """
    pass

def get_binary_age(): # real signature unknown; restored from __doc__
    """ get_binary_age() -> int """
    return 0

def get_default_registry(): # real signature unknown; restored from __doc__
    """ get_default_registry() -> Atk.Registry """
    pass

def get_focus_object(): # real signature unknown; restored from __doc__
    """ get_focus_object() -> Atk.Object """
    pass

def get_interface_age(): # real signature unknown; restored from __doc__
    """ get_interface_age() -> int """
    return 0

def get_major_version(): # real signature unknown; restored from __doc__
    """ get_major_version() -> int """
    return 0

def get_micro_version(): # real signature unknown; restored from __doc__
    """ get_micro_version() -> int """
    return 0

def get_minor_version(): # real signature unknown; restored from __doc__
    """ get_minor_version() -> int """
    return 0

def get_root(): # real signature unknown; restored from __doc__
    """ get_root() -> Atk.Object """
    pass

def get_toolkit_name(): # real signature unknown; restored from __doc__
    """ get_toolkit_name() -> str """
    return ""

def get_toolkit_version(): # real signature unknown; restored from __doc__
    """ get_toolkit_version() -> str """
    return ""

def get_version(): # real signature unknown; restored from __doc__
    """ get_version() -> str """
    return ""

def relation_type_for_name(name): # real signature unknown; restored from __doc__
    """ relation_type_for_name(name:str) -> Atk.RelationType """
    pass

def relation_type_get_name(type): # real signature unknown; restored from __doc__
    """ relation_type_get_name(type:Atk.RelationType) -> str """
    return ""

def relation_type_register(name): # real signature unknown; restored from __doc__
    """ relation_type_register(name:str) -> Atk.RelationType """
    pass

def remove_focus_tracker(tracker_id): # real signature unknown; restored from __doc__
    """ remove_focus_tracker(tracker_id:int) """
    pass

def remove_global_event_listener(listener_id): # real signature unknown; restored from __doc__
    """ remove_global_event_listener(listener_id:int) """
    pass

def remove_key_event_listener(listener_id): # real signature unknown; restored from __doc__
    """ remove_key_event_listener(listener_id:int) """
    pass

def role_for_name(name): # real signature unknown; restored from __doc__
    """ role_for_name(name:str) -> Atk.Role """
    pass

def role_get_localized_name(role): # real signature unknown; restored from __doc__
    """ role_get_localized_name(role:Atk.Role) -> str """
    return ""

def role_get_name(role): # real signature unknown; restored from __doc__
    """ role_get_name(role:Atk.Role) -> str """
    return ""

def role_register(name): # real signature unknown; restored from __doc__
    """ role_register(name:str) -> Atk.Role """
    pass

def state_type_for_name(name): # real signature unknown; restored from __doc__
    """ state_type_for_name(name:str) -> Atk.StateType """
    pass

def state_type_get_name(type): # real signature unknown; restored from __doc__
    """ state_type_get_name(type:Atk.StateType) -> str """
    return ""

def state_type_register(name): # real signature unknown; restored from __doc__
    """ state_type_register(name:str) -> Atk.StateType """
    pass

def text_attribute_for_name(name): # real signature unknown; restored from __doc__
    """ text_attribute_for_name(name:str) -> Atk.TextAttribute """
    pass

def text_attribute_get_name(attr): # real signature unknown; restored from __doc__
    """ text_attribute_get_name(attr:Atk.TextAttribute) -> str """
    return ""

def text_attribute_get_value(attr, index_): # real signature unknown; restored from __doc__
    """ text_attribute_get_value(attr:Atk.TextAttribute, index_:int) -> str or None """
    return ""

def text_attribute_register(name): # real signature unknown; restored from __doc__
    """ text_attribute_register(name:str) -> Atk.TextAttribute """
    pass

def text_free_ranges(ranges): # real signature unknown; restored from __doc__
    """ text_free_ranges(ranges:list) """
    pass

def value_type_get_localized_name(value_type): # real signature unknown; restored from __doc__
    """ value_type_get_localized_name(value_type:Atk.ValueType) -> str """
    return ""

def value_type_get_name(value_type): # real signature unknown; restored from __doc__
    """ value_type_get_name(value_type:Atk.ValueType) -> str """
    return ""

def __delattr__(*args, **kwargs): # real signature unknown
    """ Implement delattr(self, name). """
    pass

def __dir__(*args, **kwargs): # real signature unknown
    pass

def __eq__(*args, **kwargs): # real signature unknown
    """ Return self==value. """
    pass

def __format__(*args, **kwargs): # real signature unknown
    """
    Default object formatter.
    
    Return str(self) if format_spec is empty. Raise TypeError otherwise.
    """
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

from .Action import Action
from .ActionIface import ActionIface
from .Attribute import Attribute
from .Component import Component
from .ComponentIface import ComponentIface
from .CoordType import CoordType
from .Document import Document
from .DocumentIface import DocumentIface
from .EditableText import EditableText
from .EditableTextIface import EditableTextIface
from .Object import Object
from .GObjectAccessible import GObjectAccessible
from .GObjectAccessibleClass import GObjectAccessibleClass
from .Hyperlink import Hyperlink
from .HyperlinkClass import HyperlinkClass
from .HyperlinkImpl import HyperlinkImpl
from .HyperlinkImplIface import HyperlinkImplIface
from .HyperlinkStateFlags import HyperlinkStateFlags
from .Hypertext import Hypertext
from .HypertextIface import HypertextIface
from .Image import Image
from .ImageIface import ImageIface
from .Implementor import Implementor
from .ImplementorIface import ImplementorIface
from .KeyEventStruct import KeyEventStruct
from .KeyEventType import KeyEventType
from .Layer import Layer
from .Live import Live
from .Misc import Misc
from .MiscClass import MiscClass
from .Selection import Selection
from .Table import Table
from .TableCell import TableCell
from .Text import Text
from .Value import Value
from .Window import Window
from .NoOpObject import NoOpObject
from .NoOpObjectClass import NoOpObjectClass
from .ObjectFactory import ObjectFactory
from .NoOpObjectFactory import NoOpObjectFactory
from .NoOpObjectFactoryClass import NoOpObjectFactoryClass
from .ObjectClass import ObjectClass
from .ObjectFactoryClass import ObjectFactoryClass
from .Plug import Plug
from .PlugClass import PlugClass
from .PropertyValues import PropertyValues
from .Range import Range
from .Rectangle import Rectangle
from .Registry import Registry
from .RegistryClass import RegistryClass
from .Relation import Relation
from .RelationClass import RelationClass
from .RelationSet import RelationSet
from .RelationSetClass import RelationSetClass
from .RelationType import RelationType
from .Role import Role
from .ScrollType import ScrollType
from .SelectionIface import SelectionIface
from .Socket import Socket
from .SocketClass import SocketClass
from .StateSet import StateSet
from .StateSetClass import StateSetClass
from .StateType import StateType
from .StreamableContent import StreamableContent
from .StreamableContentIface import StreamableContentIface
from .TableCellIface import TableCellIface
from .TableIface import TableIface
from .TextAttribute import TextAttribute
from .TextBoundary import TextBoundary
from .TextClipType import TextClipType
from .TextGranularity import TextGranularity
from .TextIface import TextIface
from .TextRange import TextRange
from .TextRectangle import TextRectangle
from .TextSelection import TextSelection
from .Util import Util
from .UtilClass import UtilClass
from .ValueIface import ValueIface
from .ValueType import ValueType
from .WindowIface import WindowIface
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x0000017335b87890>'

__path__ = []

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Atk', loader=<gi.importer.DynamicImporter object at 0x0000017335b87890>)"

