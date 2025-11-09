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


class __class__(__gi_overrides.OverridesProxyModule):
    # no doc
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self): # reliably restored by inspect
        # no doc
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

    def __getattr__(self, name): # reliably restored by inspect
        # no doc
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

    def __init__(self, introspection_module): # reliably restored by inspect
        # no doc
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

    def __repr__(self): # reliably restored by inspect
        # no doc
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

    __annotations__ = {}
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides', '__doc__': None, 'markup_escape_text': <gi.overrides._DeprecatedAttribute object at 0x0000010b051a0690>, 'get_application_name': <gi.overrides._DeprecatedAttribute object at 0x0000010b078e1d90>, 'set_application_name': <gi.overrides._DeprecatedAttribute object at 0x0000010b07917ad0>, 'get_prgname': <gi.overrides._DeprecatedAttribute object at 0x0000010b06f8b7d0>, 'set_prgname': <gi.overrides._DeprecatedAttribute object at 0x0000010b078e1c50>, 'main_depth': <gi.overrides._DeprecatedAttribute object at 0x0000010b07915b50>, 'filename_display_basename': <gi.overrides._DeprecatedAttribute object at 0x0000010b070354d0>, 'filename_display_name': <gi.overrides._DeprecatedAttribute object at 0x0000010b0784c890>, 'filename_from_utf8': <gi.overrides._DeprecatedAttribute object at 0x0000010b0784c710>, 'uri_list_extract_uris': <gi.overrides._DeprecatedAttribute object at 0x0000010b0784cb90>, 'MainLoop': <gi.overrides._DeprecatedAttribute object at 0x0000010b0784cf90>, 'MainContext': <gi.overrides._DeprecatedAttribute object at 0x0000010b0784ee10>, 'main_context_default': <gi.overrides._DeprecatedAttribute object at 0x0000010b07899850>, 'source_remove': <gi.overrides._DeprecatedAttribute object at 0x0000010b07899190>, 'Source': <gi.overrides._DeprecatedAttribute object at 0x0000010b07876b90>, 'Idle': <gi.overrides._DeprecatedAttribute object at 0x0000010b07876950>, 'Timeout': <gi.overrides._DeprecatedAttribute object at 0x0000010b078c2c90>, 'PollFD': <gi.overrides._DeprecatedAttribute object at 0x0000010b078c2d10>, 'idle_add': <gi.overrides._DeprecatedAttribute object at 0x0000010b051be690>, 'timeout_add': <gi.overrides._DeprecatedAttribute object at 0x0000010b078c1610>, 'timeout_add_seconds': <gi.overrides._DeprecatedAttribute object at 0x0000010b06eb1350>, 'io_add_watch': <gi.overrides._DeprecatedAttribute object at 0x0000010b078c2290>, 'child_watch_add': <gi.overrides._DeprecatedAttribute object at 0x0000010b078c3890>, 'get_current_time': <gi.overrides._DeprecatedAttribute object at 0x0000010b078c38d0>, 'spawn_async': <gi.overrides._DeprecatedAttribute object at 0x0000010b078c3910>, 'PRIORITY_DEFAULT': <gi.overrides._DeprecatedAttribute object at 0x0000010b078c3950>, 'PRIORITY_DEFAULT_IDLE': <gi.overrides._DeprecatedAttribute object at 0x0000010b078e1550>, 'PRIORITY_HIGH': <gi.overrides._DeprecatedAttribute object at 0x0000010b078c3990>, 'PRIORITY_HIGH_IDLE': <gi.overrides._DeprecatedAttribute object at 0x0000010b078c39d0>, 'PRIORITY_LOW': <gi.overrides._DeprecatedAttribute object at 0x0000010b078c3a10>, 'IO_IN': <gi.overrides._DeprecatedAttribute object at 0x0000010b078c3a50>, 'IO_OUT': <gi.overrides._DeprecatedAttribute object at 0x0000010b078e0f10>, 'IO_PRI': <gi.overrides._DeprecatedAttribute object at 0x0000010b078e07d0>, 'IO_ERR': <gi.overrides._DeprecatedAttribute object at 0x0000010b078c3a90>, 'IO_HUP': <gi.overrides._DeprecatedAttribute object at 0x0000010b078c3b50>, 'IO_NVAL': <gi.overrides._DeprecatedAttribute object at 0x0000010b078c3b90>, 'IO_STATUS_ERROR': <gi.overrides._DeprecatedAttribute object at 0x0000010b078c3bd0>, 'IO_STATUS_NORMAL': <gi.overrides._DeprecatedAttribute object at 0x0000010b078c3c10>, 'IO_STATUS_EOF': <gi.overrides._DeprecatedAttribute object at 0x0000010b078c3c90>, 'IO_STATUS_AGAIN': <gi.overrides._DeprecatedAttribute object at 0x0000010b078e0b50>, 'IO_FLAG_APPEND': <gi.overrides._DeprecatedAttribute object at 0x0000010b078c3d10>, 'IO_FLAG_NONBLOCK': <gi.overrides._DeprecatedAttribute object at 0x0000010b078c3d90>, 'IO_FLAG_IS_READABLE': <gi.overrides._DeprecatedAttribute object at 0x0000010b078c3dd0>, 'IO_FLAG_IS_WRITEABLE': <gi.overrides._DeprecatedAttribute object at 0x0000010b078c3e10>, 'IO_FLAG_IS_SEEKABLE': <gi.overrides._DeprecatedAttribute object at 0x0000010b06f82110>, 'IO_FLAG_MASK': <gi.overrides._DeprecatedAttribute object at 0x0000010b05001e10>, 'IO_FLAG_GET_MASK': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792d750>, 'IO_FLAG_SET_MASK': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792d550>, 'SPAWN_LEAVE_DESCRIPTORS_OPEN': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792d010>, 'SPAWN_DO_NOT_REAP_CHILD': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792e450>, 'SPAWN_SEARCH_PATH': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792d450>, 'SPAWN_STDOUT_TO_DEV_NULL': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792d3d0>, 'SPAWN_STDERR_TO_DEV_NULL': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792d610>, 'SPAWN_CHILD_INHERITS_STDIN': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792d5d0>, 'SPAWN_FILE_AND_ARGV_ZERO': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792d790>, 'OPTION_FLAG_HIDDEN': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792e810>, 'OPTION_FLAG_IN_MAIN': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792d690>, 'OPTION_FLAG_REVERSE': <gi.overrides._DeprecatedAttribute object at 0x0000010b078c2e50>, 'OPTION_FLAG_NO_ARG': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792d6d0>, 'OPTION_FLAG_FILENAME': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792da90>, 'OPTION_FLAG_OPTIONAL_ARG': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792dad0>, 'OPTION_FLAG_NOALIAS': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792db10>, 'OPTION_ERROR_UNKNOWN_OPTION': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792db50>, 'OPTION_ERROR_BAD_VALUE': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792db90>, 'OPTION_ERROR_FAILED': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792dbd0>, 'OPTION_REMAINING': <gi.overrides._DeprecatedAttribute object at 0x0000010b078c2ed0>, 'glib_version': <gi.overrides._DeprecatedAttribute object at 0x0000010b0489cb10>, 'G_MININT8': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792dc10>, 'G_MAXINT8': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792dc50>, 'G_MAXUINT8': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792dc90>, 'G_MININT16': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792dcd0>, 'G_MAXINT16': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792dd10>, 'G_MAXUINT16': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792dd50>, 'G_MININT32': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792dd90>, 'G_MAXINT32': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792ddd0>, 'G_MAXUINT32': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792de10>, 'G_MININT64': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792de50>, 'G_MAXINT64': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792de90>, 'G_MAXUINT64': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792ded0>, 'G_MINFLOAT': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792df10>, 'G_MAXFLOAT': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792df50>, 'G_MINDOUBLE': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792df90>, 'G_MAXDOUBLE': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792dfd0>, 'G_MINSHORT': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792e010>, 'G_MAXSHORT': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792e050>, 'G_MAXUSHORT': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792e090>, 'G_MININT': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792e0d0>, 'G_MAXINT': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792e110>, 'G_MAXUINT': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792e150>, 'G_MINLONG': <gi.overrides._DeprecatedAttribute object at 0x0000010b078e1310>, 'G_MAXLONG': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792e190>, 'G_MAXULONG': <gi.overrides._DeprecatedAttribute object at 0x0000010b078e1290>, 'G_MAXSIZE': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792e1d0>, 'G_MINSSIZE': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792e210>, 'G_MAXSSIZE': <gi.overrides._DeprecatedAttribute object at 0x0000010b078e0a90>, 'G_MINOFFSET': <gi.overrides._DeprecatedAttribute object at 0x0000010b07915bd0>, 'G_MAXOFFSET': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792e250>, 'Pid': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792e290>, 'GError': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792e2d0>, 'OptionGroup': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792f750>, 'OptionContext': <gi.overrides._DeprecatedAttribute object at 0x0000010b078e12d0>, 'PARAM_CONSTRUCT': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792f790>, 'PARAM_CONSTRUCT_ONLY': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792f7d0>, 'PARAM_LAX_VALIDATION': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792f810>, 'PARAM_READABLE': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792f850>, 'PARAM_WRITABLE': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792f890>, 'PARAM_READWRITE': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792f8d0>, 'SIGNAL_ACTION': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792f910>, 'SIGNAL_DETAILED': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792f950>, 'SIGNAL_NO_HOOKS': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792f990>, 'SIGNAL_NO_RECURSE': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792f9d0>, 'SIGNAL_RUN_CLEANUP': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792fa10>, 'SIGNAL_RUN_FIRST': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792fa50>, 'SIGNAL_RUN_LAST': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792fa90>, 'property': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792fad0>, 'GParamSpec': <gi.overrides._DeprecatedAttribute object at 0x0000010b0792fb10>, '__annotations__': {}})"


