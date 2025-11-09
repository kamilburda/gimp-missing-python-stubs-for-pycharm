# encoding: utf-8
# module gi.repository.Gtk
# from C:/Program Files/GIMP 3/lib/girepository-1.0\Gtk-3.0.typelib
# by generator 1.147
# no doc

# imports
from _thread import _lock

import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Atk as __gi_repository_Atk
import gi.repository.Gio as __gi_repository_Gio
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class CellAreaClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        CellAreaClass()
    """
    def find_cell_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_cell_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def install_cell_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_cell_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def list_cell_properties(self): # real signature unknown; restored from __doc__
        """ list_cell_properties(self) -> list """
        return []

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """
        Default object formatter.
        
        Return str(self) if format_spec is empty. Raise TypeError otherwise.
        """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Size of object in memory, in bytes. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __subclasshook__(self, *args, **kwargs): # real signature unknown
        """
        Abstract classes can override this to customize issubclass().
        
        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        pass

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    activate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    add = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    apply_attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    copy_context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    create_context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    focus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    foreach = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    foreach_alloc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_cell_property = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_preferred_height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_preferred_height_for_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_preferred_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_preferred_width_for_height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_request_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_activatable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    render = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_cell_property = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved7 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(CellAreaClass), '__module__': 'gi.repository.Gtk', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'CellAreaClass' objects>, '__weakref__': <attribute '__weakref__' of 'CellAreaClass' objects>, '__doc__': None, 'parent_class': <property object at 0x000002ece8ff6f70>, 'add': <property object at 0x000002ece8ff7060>, 'remove': <property object at 0x000002ece8ff7150>, 'foreach': <property object at 0x000002ece8ff7240>, 'foreach_alloc': <property object at 0x000002ece8ff7330>, 'event': <property object at 0x000002ece8ff7420>, 'render': <property object at 0x000002ece8ff7510>, 'apply_attributes': <property object at 0x000002ece8ff7600>, 'create_context': <property object at 0x000002ece8ff76f0>, 'copy_context': <property object at 0x000002ece8ff77e0>, 'get_request_mode': <property object at 0x000002ece8ff78d0>, 'get_preferred_width': <property object at 0x000002ece8ff79c0>, 'get_preferred_height_for_width': <property object at 0x000002ece8ff7b00>, 'get_preferred_height': <property object at 0x000002ece8ff7ba0>, 'get_preferred_width_for_height': <property object at 0x000002ece8ff7ce0>, 'set_cell_property': <property object at 0x000002ece8ff7d80>, 'get_cell_property': <property object at 0x000002ece8ff7e70>, 'focus': <property object at 0x000002ece8ff7f60>, 'is_activatable': <property object at 0x000002ece9004090>, 'activate': <property object at 0x000002ece9004180>, '_gtk_reserved1': <property object at 0x000002ece9004270>, '_gtk_reserved2': <property object at 0x000002ece9004360>, '_gtk_reserved3': <property object at 0x000002ece9004450>, '_gtk_reserved4': <property object at 0x000002ece9004540>, '_gtk_reserved5': <property object at 0x000002ece9004630>, '_gtk_reserved6': <property object at 0x000002ece9004720>, '_gtk_reserved7': <property object at 0x000002ece9004810>, '_gtk_reserved8': <property object at 0x000002ece9004900>, 'find_cell_property': gi.FunctionInfo(find_cell_property, bound=None), 'install_cell_property': gi.FunctionInfo(install_cell_property, bound=None), 'list_cell_properties': gi.FunctionInfo(list_cell_properties, bound=None)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(CellAreaClass)


