# encoding: utf-8
# module gi.repository.GLib
# from C:/Program Files/GIMP 3/lib/girepository-1.0\GLib-2.0.typelib
# by generator 1.147
# no doc

# imports
import gi._option as option # C:\Program Files\GIMP 3\lib\python3.12\site-packages\gi\_option.py
from gi._gi import OptionContext, OptionGroup, Pid, spawn_async

from _thread import _lock

import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.GLib as __gi_overrides_GLib
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
        """
        Default object formatter.
        
        Return str(self) if format_spec is empty. Raise TypeError otherwise.
        """
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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides', '__doc__': None, 'USER_DIRECTORY_DESKTOP': <gi.overrides._DeprecatedAttribute object at 0x000002830964b530>, 'USER_DIRECTORY_DOCUMENTS': <gi.overrides._DeprecatedAttribute object at 0x0000028309663a10>, 'USER_DIRECTORY_DOWNLOAD': <gi.overrides._DeprecatedAttribute object at 0x0000028309662cf0>, 'USER_DIRECTORY_MUSIC': <gi.overrides._DeprecatedAttribute object at 0x000002830bbc7950>, 'USER_DIRECTORY_PICTURES': <gi.overrides._DeprecatedAttribute object at 0x0000028308f0a1b0>, 'USER_DIRECTORY_PUBLIC_SHARE': <gi.overrides._DeprecatedAttribute object at 0x00000283095fc0b0>, 'USER_DIRECTORY_TEMPLATES': <gi.overrides._DeprecatedAttribute object at 0x0000028309b3a030>, 'USER_DIRECTORY_VIDEOS': <gi.overrides._DeprecatedAttribute object at 0x0000028309b36540>, 'IO_FLAG_APPEND': <gi.overrides._DeprecatedAttribute object at 0x000002830bb71970>, 'IO_FLAG_GET_MASK': <gi.overrides._DeprecatedAttribute object at 0x000002830bb72450>, 'IO_FLAG_IS_READABLE': <gi.overrides._DeprecatedAttribute object at 0x000002830bb718b0>, 'IO_FLAG_IS_SEEKABLE': <gi.overrides._DeprecatedAttribute object at 0x000002830bca6330>, 'IO_FLAG_MASK': <gi.overrides._DeprecatedAttribute object at 0x000002830bca63c0>, 'IO_FLAG_NONBLOCK': <gi.overrides._DeprecatedAttribute object at 0x000002830bca6480>, 'IO_FLAG_SET_MASK': <gi.overrides._DeprecatedAttribute object at 0x000002830bca64e0>, 'IO_FLAG_IS_WRITEABLE': <gi.overrides._DeprecatedAttribute object at 0x000002830bca6510>, 'IO_STATUS_AGAIN': <gi.overrides._DeprecatedAttribute object at 0x000002830bca6570>, 'IO_STATUS_EOF': <gi.overrides._DeprecatedAttribute object at 0x000002830bca65d0>, 'IO_STATUS_ERROR': <gi.overrides._DeprecatedAttribute object at 0x000002830bca6630>, 'IO_STATUS_NORMAL': <gi.overrides._DeprecatedAttribute object at 0x000002830bca6690>, 'SPAWN_CHILD_INHERITS_STDIN': <gi.overrides._DeprecatedAttribute object at 0x000002830bca66f0>, 'SPAWN_DO_NOT_REAP_CHILD': <gi.overrides._DeprecatedAttribute object at 0x000002830bca6720>, 'SPAWN_FILE_AND_ARGV_ZERO': <gi.overrides._DeprecatedAttribute object at 0x000002830bca67e0>, 'SPAWN_LEAVE_DESCRIPTORS_OPEN': <gi.overrides._DeprecatedAttribute object at 0x000002830bca6810>, 'SPAWN_SEARCH_PATH': <gi.overrides._DeprecatedAttribute object at 0x000002830bca6930>, 'SPAWN_STDERR_TO_DEV_NULL': <gi.overrides._DeprecatedAttribute object at 0x000002830bca6b40>, 'SPAWN_STDOUT_TO_DEV_NULL': <gi.overrides._DeprecatedAttribute object at 0x000002830bca6e40>, 'OPTION_FLAG_HIDDEN': <gi.overrides._DeprecatedAttribute object at 0x000002830bca6f00>, 'OPTION_FLAG_IN_MAIN': <gi.overrides._DeprecatedAttribute object at 0x000002830bca6f90>, 'OPTION_FLAG_REVERSE': <gi.overrides._DeprecatedAttribute object at 0x000002830bca7020>, 'OPTION_FLAG_NO_ARG': <gi.overrides._DeprecatedAttribute object at 0x000002830bca70b0>, 'OPTION_FLAG_FILENAME': <gi.overrides._DeprecatedAttribute object at 0x000002830bb72180>, 'OPTION_FLAG_OPTIONAL_ARG': <gi.overrides._DeprecatedAttribute object at 0x000002830bca71a0>, 'OPTION_FLAG_NOALIAS': <gi.overrides._DeprecatedAttribute object at 0x000002830bca7230>, 'OPTION_ERROR_UNKNOWN_OPTION': <gi.overrides._DeprecatedAttribute object at 0x000002830bca72c0>, 'OPTION_ERROR_BAD_VALUE': <gi.overrides._DeprecatedAttribute object at 0x000002830bca7350>, 'OPTION_ERROR_FAILED': <gi.overrides._DeprecatedAttribute object at 0x000002830bca73e0>, 'glib_version': <gi.overrides._DeprecatedAttribute object at 0x000002830bca74a0>, 'pyglib_version': <gi.overrides._DeprecatedAttribute object at 0x000002830bca74d0>, '__annotations__': {}})"


