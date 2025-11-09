# encoding: utf-8
# module gi.repository.GObject
# from C:/Program Files/GIMP 3/lib/girepository-1.0\GObject-2.0.typelib
# by generator 1.147
# no doc

# imports
from gi.repository.GLib import (Error, GError, IOCondition, IO_ERR, 
    IO_FLAG_APPEND, IO_FLAG_GET_MASK, IO_FLAG_IS_READABLE, 
    IO_FLAG_IS_SEEKABLE, IO_FLAG_IS_WRITEABLE, IO_FLAG_MASK, IO_FLAG_NONBLOCK, 
    IO_FLAG_SET_MASK, IO_HUP, IO_IN, IO_NVAL, IO_OUT, IO_PRI, IO_STATUS_AGAIN, 
    IO_STATUS_EOF, IO_STATUS_ERROR, IO_STATUS_NORMAL, OPTION_ERROR_BAD_VALUE, 
    OPTION_ERROR_FAILED, OPTION_ERROR_UNKNOWN_OPTION, OPTION_FLAG_FILENAME, 
    OPTION_FLAG_HIDDEN, OPTION_FLAG_IN_MAIN, OPTION_FLAG_NOALIAS, 
    OPTION_FLAG_NO_ARG, OPTION_FLAG_OPTIONAL_ARG, OPTION_FLAG_REVERSE, 
    SPAWN_CHILD_INHERITS_STDIN, SPAWN_DO_NOT_REAP_CHILD, 
    SPAWN_FILE_AND_ARGV_ZERO, SPAWN_LEAVE_DESCRIPTORS_OPEN, SPAWN_SEARCH_PATH, 
    SPAWN_STDERR_TO_DEV_NULL, SPAWN_STDOUT_TO_DEV_NULL, 
    filename_display_basename, filename_display_name, get_application_name, 
    get_prgname, main_context_default, main_depth, set_application_name, 
    set_prgname, source_remove, uri_list_extract_uris)

from gi._gi import (GObjectWeakRef, OptionContext, OptionGroup, Pid, 
    add_emission_hook, list_properties, new, signal_new, spawn_async, 
    type_register)

from gobject import (GBoxed, GEnum, GFlags, GInterface, GPointer, GType, 
    Warning)

from _thread import _lock

import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.GLib as __gi_overrides_GLib
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GLib as __gi_repository_GLib
import gi._signalhelper as __gi__signalhelper
import gobject as __gobject


class TypeInterface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        TypeInterface()
    """
    def add_prerequisite(self, interface_type, prerequisite_type): # real signature unknown; restored from __doc__
        """ add_prerequisite(interface_type:GType, prerequisite_type:GType) """
        pass

    def get_plugin(self, instance_type, interface_type): # real signature unknown; restored from __doc__
        """ get_plugin(instance_type:GType, interface_type:GType) -> GObject.TypePlugin """
        pass

    def instantiatable_prerequisite(self, interface_type): # real signature unknown; restored from __doc__
        """ instantiatable_prerequisite(interface_type:GType) -> GType """
        return GType

    def peek(self, instance_class, iface_type): # real signature unknown; restored from __doc__
        """ peek(instance_class:GObject.TypeClass, iface_type:GType) -> GObject.TypeInterface """
        pass

    def peek_parent(self): # real signature unknown; restored from __doc__
        """ peek_parent(self) -> GObject.TypeInterface """
        pass

    def prerequisites(self, interface_type): # real signature unknown; restored from __doc__
        """ prerequisites(interface_type:GType) -> list """
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
        """ Default object formatter. """
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

    g_instance_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TypeInterface), '__module__': 'gi.repository.GObject', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'TypeInterface' objects>, '__weakref__': <attribute '__weakref__' of 'TypeInterface' objects>, '__doc__': None, 'g_type': <property object at 0x0000010b07a889a0>, 'g_instance_type': <property object at 0x0000010b07a88a90>, 'peek_parent': gi.FunctionInfo(peek_parent, bound=None), 'add_prerequisite': gi.FunctionInfo(add_prerequisite, bound=None), 'get_plugin': gi.FunctionInfo(get_plugin, bound=None), 'instantiatable_prerequisite': gi.FunctionInfo(instantiatable_prerequisite, bound=None), 'peek': gi.FunctionInfo(peek, bound=None), 'prerequisites': gi.FunctionInfo(prerequisites, bound=None)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(TypeInterface)


