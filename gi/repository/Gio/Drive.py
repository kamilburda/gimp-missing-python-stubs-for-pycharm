# encoding: utf-8
# module gi.repository.Gio
# from C:/Program Files/GIMP 3/lib/girepository-1.0\Gio-2.0.typelib
# by generator 1.147
# no doc

# imports
from _thread import _lock

import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class Drive(__gobject.GInterface):
    # no doc
    def can_eject(self): # real signature unknown; restored from __doc__
        """ can_eject(self) -> bool """
        return False

    def can_poll_for_media(self): # real signature unknown; restored from __doc__
        """ can_poll_for_media(self) -> bool """
        return False

    def can_start(self): # real signature unknown; restored from __doc__
        """ can_start(self) -> bool """
        return False

    def can_start_degraded(self): # real signature unknown; restored from __doc__
        """ can_start_degraded(self) -> bool """
        return False

    def can_stop(self): # real signature unknown; restored from __doc__
        """ can_stop(self) -> bool """
        return False

    def eject(self, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ eject(self, flags:Gio.MountUnmountFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def eject_finish(self, result): # real signature unknown; restored from __doc__
        """ eject_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def eject_with_operation(self, flags, mount_operation=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ eject_with_operation(self, flags:Gio.MountUnmountFlags, mount_operation:Gio.MountOperation=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def eject_with_operation_finish(self, result): # real signature unknown; restored from __doc__
        """ eject_with_operation_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def enumerate_identifiers(self): # real signature unknown; restored from __doc__
        """ enumerate_identifiers(self) -> list """
        return []

    def get_icon(self): # real signature unknown; restored from __doc__
        """ get_icon(self) -> Gio.Icon """
        pass

    def get_identifier(self, kind): # real signature unknown; restored from __doc__
        """ get_identifier(self, kind:str) -> str or None """
        return ""

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_sort_key(self): # real signature unknown; restored from __doc__
        """ get_sort_key(self) -> str or None """
        return ""

    def get_start_stop_type(self): # real signature unknown; restored from __doc__
        """ get_start_stop_type(self) -> Gio.DriveStartStopType """
        pass

    def get_symbolic_icon(self): # real signature unknown; restored from __doc__
        """ get_symbolic_icon(self) -> Gio.Icon """
        pass

    def get_volumes(self): # real signature unknown; restored from __doc__
        """ get_volumes(self) -> list """
        return []

    def has_media(self): # real signature unknown; restored from __doc__
        """ has_media(self) -> bool """
        return False

    def has_volumes(self): # real signature unknown; restored from __doc__
        """ has_volumes(self) -> bool """
        return False

    def is_media_check_automatic(self): # real signature unknown; restored from __doc__
        """ is_media_check_automatic(self) -> bool """
        return False

    def is_media_removable(self): # real signature unknown; restored from __doc__
        """ is_media_removable(self) -> bool """
        return False

    def is_removable(self): # real signature unknown; restored from __doc__
        """ is_removable(self) -> bool """
        return False

    def poll_for_media(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ poll_for_media(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def poll_for_media_finish(self, result): # real signature unknown; restored from __doc__
        """ poll_for_media_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def start(self, flags, mount_operation=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ start(self, flags:Gio.DriveStartFlags, mount_operation:Gio.MountOperation=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def start_finish(self, result): # real signature unknown; restored from __doc__
        """ start_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def stop(self, flags, mount_operation=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ stop(self, flags:Gio.MountUnmountFlags, mount_operation:Gio.MountOperation=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def stop_finish(self, result): # real signature unknown; restored from __doc__
        """ stop_finish(self, result:Gio.AsyncResult) -> bool """
        return False

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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Drive), '__module__': 'gi.repository.Gio', '__gtype__': <GType GDrive (2472618544)>, '__dict__': <attribute '__dict__' of 'Drive' objects>, '__weakref__': <attribute '__weakref__' of 'Drive' objects>, '__doc__': None, '__gsignals__': {}, 'can_eject': gi.FunctionInfo(can_eject, bound=None), 'can_poll_for_media': gi.FunctionInfo(can_poll_for_media, bound=None), 'can_start': gi.FunctionInfo(can_start, bound=None), 'can_start_degraded': gi.FunctionInfo(can_start_degraded, bound=None), 'can_stop': gi.FunctionInfo(can_stop, bound=None), 'eject': gi.FunctionInfo(eject, bound=None), 'eject_finish': gi.FunctionInfo(eject_finish, bound=None), 'eject_with_operation': gi.FunctionInfo(eject_with_operation, bound=None), 'eject_with_operation_finish': gi.FunctionInfo(eject_with_operation_finish, bound=None), 'enumerate_identifiers': gi.FunctionInfo(enumerate_identifiers, bound=None), 'get_icon': gi.FunctionInfo(get_icon, bound=None), 'get_identifier': gi.FunctionInfo(get_identifier, bound=None), 'get_name': gi.FunctionInfo(get_name, bound=None), 'get_sort_key': gi.FunctionInfo(get_sort_key, bound=None), 'get_start_stop_type': gi.FunctionInfo(get_start_stop_type, bound=None), 'get_symbolic_icon': gi.FunctionInfo(get_symbolic_icon, bound=None), 'get_volumes': gi.FunctionInfo(get_volumes, bound=None), 'has_media': gi.FunctionInfo(has_media, bound=None), 'has_volumes': gi.FunctionInfo(has_volumes, bound=None), 'is_media_check_automatic': gi.FunctionInfo(is_media_check_automatic, bound=None), 'is_media_removable': gi.FunctionInfo(is_media_removable, bound=None), 'is_removable': gi.FunctionInfo(is_removable, bound=None), 'poll_for_media': gi.FunctionInfo(poll_for_media, bound=None), 'poll_for_media_finish': gi.FunctionInfo(poll_for_media_finish, bound=None), 'start': gi.FunctionInfo(start, bound=None), 'start_finish': gi.FunctionInfo(start_finish, bound=None), 'stop': gi.FunctionInfo(stop, bound=None), 'stop_finish': gi.FunctionInfo(stop_finish, bound=None)})"
    __gdoc__ = 'Interface GDrive\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GDrive (2472618544)>'
    __info__ = InterfaceInfo(Drive)


