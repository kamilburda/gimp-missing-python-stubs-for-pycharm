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


class VolumeIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        VolumeIface()
    """
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

    can_eject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    can_mount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eject_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eject_with_operation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eject_with_operation_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    enumerate_identifiers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_activation_root = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_drive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_identifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_mount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_sort_key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_symbolic_icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_uuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mount_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mount_fn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    removed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    should_automount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(VolumeIface), '__module__': 'gi.repository.Gio', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'VolumeIface' objects>, '__weakref__': <attribute '__weakref__' of 'VolumeIface' objects>, '__doc__': None, 'g_iface': <property object at 0x000001a793d73920>, 'changed': <property object at 0x000001a793d73a10>, 'removed': <property object at 0x000001a793d73b00>, 'get_name': <property object at 0x000001a793d73ba0>, 'get_icon': <property object at 0x000001a793d73c90>, 'get_uuid': <property object at 0x000001a793d73d80>, 'get_drive': <property object at 0x000001a793d73e70>, 'get_mount': <property object at 0x000001a793d73f60>, 'can_mount': <property object at 0x000001a793e70090>, 'can_eject': <property object at 0x000001a793e70180>, 'mount_fn': <property object at 0x000001a793e70270>, 'mount_finish': <property object at 0x000001a793e70360>, 'eject': <property object at 0x000001a793e70450>, 'eject_finish': <property object at 0x000001a793e70540>, 'get_identifier': <property object at 0x000001a793e70630>, 'enumerate_identifiers': <property object at 0x000001a793e70770>, 'should_automount': <property object at 0x000001a793e70860>, 'get_activation_root': <property object at 0x000001a793e70950>, 'eject_with_operation': <property object at 0x000001a793e70a40>, 'eject_with_operation_finish': <property object at 0x000001a793e70b30>, 'get_sort_key': <property object at 0x000001a793e70bd0>, 'get_symbolic_icon': <property object at 0x000001a793e70d10>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(VolumeIface)


