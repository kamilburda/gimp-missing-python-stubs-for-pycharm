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


class ContainerClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ContainerClass()
    """
    def find_child_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_child_property(self, property_name:str) -> GObject.ParamSpec or None """
        pass

    def handle_border_width(self): # real signature unknown; restored from __doc__
        """ handle_border_width(self) """
        pass

    def install_child_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_child_properties(self, pspecs:list) """
        pass

    def install_child_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_child_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def list_child_properties(self): # real signature unknown; restored from __doc__
        """ list_child_properties(self) -> list """
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

    add = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    check_resize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    child_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    composite_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forall = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_child_property = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_path_for_child = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_child_property = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_focus_child = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved7 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _handle_border_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ContainerClass), '__module__': 'gi.repository.Gtk', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ContainerClass' objects>, '__weakref__': <attribute '__weakref__' of 'ContainerClass' objects>, '__doc__': None, 'parent_class': <property object at 0x000002eceab82e80>, 'add': <property object at 0x000002eceab82f70>, 'remove': <property object at 0x000002eceab83060>, 'check_resize': <property object at 0x000002eceab83150>, 'forall': <property object at 0x000002eceab83240>, 'set_focus_child': <property object at 0x000002eceab83330>, 'child_type': <property object at 0x000002eceab83420>, 'composite_name': <property object at 0x000002eceab83510>, 'set_child_property': <property object at 0x000002eceab83600>, 'get_child_property': <property object at 0x000002eceab836f0>, 'get_path_for_child': <property object at 0x000002eceab837e0>, '_handle_border_width': <property object at 0x000002eceab838d0>, '_gtk_reserved1': <property object at 0x000002eceab839c0>, '_gtk_reserved2': <property object at 0x000002eceab83ab0>, '_gtk_reserved3': <property object at 0x000002eceab83ba0>, '_gtk_reserved4': <property object at 0x000002eceab83c90>, '_gtk_reserved5': <property object at 0x000002eceab83d80>, '_gtk_reserved6': <property object at 0x000002eceab83e70>, '_gtk_reserved7': <property object at 0x000002eceab83f60>, '_gtk_reserved8': <property object at 0x000002eceab78090>, 'find_child_property': gi.FunctionInfo(find_child_property, bound=None), 'handle_border_width': gi.FunctionInfo(handle_border_width, bound=None), 'install_child_properties': gi.FunctionInfo(install_child_properties, bound=None), 'install_child_property': gi.FunctionInfo(install_child_property, bound=None), 'list_child_properties': gi.FunctionInfo(list_child_properties, bound=None)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ContainerClass)


