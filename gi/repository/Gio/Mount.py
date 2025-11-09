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


class Mount(__gobject.GInterface):
    # no doc
    def can_eject(self): # real signature unknown; restored from __doc__
        """ can_eject(self) -> bool """
        return False

    def can_unmount(self): # real signature unknown; restored from __doc__
        """ can_unmount(self) -> bool """
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

    def get_default_location(self): # real signature unknown; restored from __doc__
        """ get_default_location(self) -> Gio.File """
        pass

    def get_drive(self): # real signature unknown; restored from __doc__
        """ get_drive(self) -> Gio.Drive or None """
        pass

    def get_icon(self): # real signature unknown; restored from __doc__
        """ get_icon(self) -> Gio.Icon """
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_root(self): # real signature unknown; restored from __doc__
        """ get_root(self) -> Gio.File """
        pass

    def get_sort_key(self): # real signature unknown; restored from __doc__
        """ get_sort_key(self) -> str or None """
        return ""

    def get_symbolic_icon(self): # real signature unknown; restored from __doc__
        """ get_symbolic_icon(self) -> Gio.Icon """
        pass

    def get_uuid(self): # real signature unknown; restored from __doc__
        """ get_uuid(self) -> str or None """
        return ""

    def get_volume(self): # real signature unknown; restored from __doc__
        """ get_volume(self) -> Gio.Volume or None """
        pass

    def guess_content_type(self, force_rescan, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ guess_content_type(self, force_rescan:bool, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def guess_content_type_finish(self, result): # real signature unknown; restored from __doc__
        """ guess_content_type_finish(self, result:Gio.AsyncResult) -> list """
        return []

    def guess_content_type_sync(self, force_rescan, cancellable=None): # real signature unknown; restored from __doc__
        """ guess_content_type_sync(self, force_rescan:bool, cancellable:Gio.Cancellable=None) -> list """
        return []

    def is_shadowed(self): # real signature unknown; restored from __doc__
        """ is_shadowed(self) -> bool """
        return False

    def remount(self, flags, mount_operation=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ remount(self, flags:Gio.MountMountFlags, mount_operation:Gio.MountOperation=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def remount_finish(self, result): # real signature unknown; restored from __doc__
        """ remount_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def shadow(self): # real signature unknown; restored from __doc__
        """ shadow(self) """
        pass

    def unmount(self, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ unmount(self, flags:Gio.MountUnmountFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def unmount_finish(self, result): # real signature unknown; restored from __doc__
        """ unmount_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def unmount_with_operation(self, flags, mount_operation=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ unmount_with_operation(self, flags:Gio.MountUnmountFlags, mount_operation:Gio.MountOperation=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def unmount_with_operation_finish(self, result): # real signature unknown; restored from __doc__
        """ unmount_with_operation_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def unshadow(self): # real signature unknown; restored from __doc__
        """ unshadow(self) """
        pass

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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Mount), '__module__': 'gi.repository.Gio', '__gtype__': <GType GMount (2466387712)>, '__dict__': <attribute '__dict__' of 'Mount' objects>, '__weakref__': <attribute '__weakref__' of 'Mount' objects>, '__doc__': None, '__gsignals__': {}, 'can_eject': gi.FunctionInfo(can_eject, bound=None), 'can_unmount': gi.FunctionInfo(can_unmount, bound=None), 'eject': gi.FunctionInfo(eject, bound=None), 'eject_finish': gi.FunctionInfo(eject_finish, bound=None), 'eject_with_operation': gi.FunctionInfo(eject_with_operation, bound=None), 'eject_with_operation_finish': gi.FunctionInfo(eject_with_operation_finish, bound=None), 'get_default_location': gi.FunctionInfo(get_default_location, bound=None), 'get_drive': gi.FunctionInfo(get_drive, bound=None), 'get_icon': gi.FunctionInfo(get_icon, bound=None), 'get_name': gi.FunctionInfo(get_name, bound=None), 'get_root': gi.FunctionInfo(get_root, bound=None), 'get_sort_key': gi.FunctionInfo(get_sort_key, bound=None), 'get_symbolic_icon': gi.FunctionInfo(get_symbolic_icon, bound=None), 'get_uuid': gi.FunctionInfo(get_uuid, bound=None), 'get_volume': gi.FunctionInfo(get_volume, bound=None), 'guess_content_type': gi.FunctionInfo(guess_content_type, bound=None), 'guess_content_type_finish': gi.FunctionInfo(guess_content_type_finish, bound=None), 'guess_content_type_sync': gi.FunctionInfo(guess_content_type_sync, bound=None), 'is_shadowed': gi.FunctionInfo(is_shadowed, bound=None), 'remount': gi.FunctionInfo(remount, bound=None), 'remount_finish': gi.FunctionInfo(remount_finish, bound=None), 'shadow': gi.FunctionInfo(shadow, bound=None), 'unmount': gi.FunctionInfo(unmount, bound=None), 'unmount_finish': gi.FunctionInfo(unmount_finish, bound=None), 'unmount_with_operation': gi.FunctionInfo(unmount_with_operation, bound=None), 'unmount_with_operation_finish': gi.FunctionInfo(unmount_with_operation_finish, bound=None), 'unshadow': gi.FunctionInfo(unshadow, bound=None)})"
    __gdoc__ = 'Interface GMount\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GMount (2466387712)>'
    __info__ = InterfaceInfo(Mount)


