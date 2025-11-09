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


class FileIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        FileIface()
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

    append_to = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    append_to_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    append_to_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    copy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    copy_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    copy_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    create = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    create_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    create_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    create_readwrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    create_readwrite_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    create_readwrite_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    delete_file = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    delete_file_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    delete_file_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eject_mountable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eject_mountable_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eject_mountable_with_operation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eject_mountable_with_operation_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    enumerate_children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    enumerate_children_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    enumerate_children_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    equal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    find_enclosing_mount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    find_enclosing_mount_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    find_enclosing_mount_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_basename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_child_for_display_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_parse_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_relative_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_uri_scheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hash = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_uri_scheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_native = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    make_directory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    make_directory_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    make_directory_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    make_symbolic_link = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    make_symbolic_link_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    make_symbolic_link_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    measure_disk_usage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    measure_disk_usage_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    measure_disk_usage_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    monitor_dir = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    monitor_file = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mount_enclosing_volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mount_enclosing_volume_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mount_mountable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mount_mountable_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    move = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    move_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    move_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    open_readwrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    open_readwrite_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    open_readwrite_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    poll_mountable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    poll_mountable_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    prefix_matches = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query_filesystem_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query_filesystem_info_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query_filesystem_info_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query_info_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query_info_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query_settable_attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query_writable_namespaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    read_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    read_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    read_fn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    replace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    replace_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    replace_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    replace_readwrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    replace_readwrite_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    replace_readwrite_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    resolve_relative_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_attribute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_attributes_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_attributes_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_attributes_from_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_display_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_display_name_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_display_name_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start_mountable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start_mountable_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stop_mountable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stop_mountable_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_thread_contexts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    trash = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    trash_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    trash_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unmount_mountable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unmount_mountable_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unmount_mountable_with_operation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unmount_mountable_with_operation_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _query_settable_attributes_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _query_settable_attributes_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _query_writable_namespaces_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _query_writable_namespaces_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(FileIface), '__module__': 'gi.repository.Gio', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'FileIface' objects>, '__weakref__': <attribute '__weakref__' of 'FileIface' objects>, '__doc__': None, 'g_iface': <property object at 0x000001a793e1bd80>, 'dup': <property object at 0x000001a793e1be70>, 'hash': <property object at 0x000001a793e1bf60>, 'equal': <property object at 0x000001a793e10090>, 'is_native': <property object at 0x000001a793e10180>, 'has_uri_scheme': <property object at 0x000001a793e10270>, 'get_uri_scheme': <property object at 0x000001a793e10360>, 'get_basename': <property object at 0x000001a793e10450>, 'get_path': <property object at 0x000001a793e10540>, 'get_uri': <property object at 0x000001a793e10630>, 'get_parse_name': <property object at 0x000001a793e10720>, 'get_parent': <property object at 0x000001a793e10810>, 'prefix_matches': <property object at 0x000001a793e10900>, 'get_relative_path': <property object at 0x000001a793e10a40>, 'resolve_relative_path': <property object at 0x000001a793e10b30>, 'get_child_for_display_name': <property object at 0x000001a793e10c20>, 'enumerate_children': <property object at 0x000001a793e10d10>, 'enumerate_children_async': <property object at 0x000001a793e10e00>, 'enumerate_children_finish': <property object at 0x000001a793e10ef0>, 'query_info': <property object at 0x000001a793e10f90>, 'query_info_async': <property object at 0x000001a793e110d0>, 'query_info_finish': <property object at 0x000001a793e111c0>, 'query_filesystem_info': <property object at 0x000001a793e112b0>, 'query_filesystem_info_async': <property object at 0x000001a793e113a0>, 'query_filesystem_info_finish': <property object at 0x000001a793e11490>, 'find_enclosing_mount': <property object at 0x000001a793e11580>, 'find_enclosing_mount_async': <property object at 0x000001a793e11670>, 'find_enclosing_mount_finish': <property object at 0x000001a793e11760>, 'set_display_name': <property object at 0x000001a793e11850>, 'set_display_name_async': <property object at 0x000001a793e11940>, 'set_display_name_finish': <property object at 0x000001a793e11a30>, 'query_settable_attributes': <property object at 0x000001a793e11b20>, '_query_settable_attributes_async': <property object at 0x000001a793e11bc0>, '_query_settable_attributes_finish': <property object at 0x000001a793e11cb0>, 'query_writable_namespaces': <property object at 0x000001a793e11da0>, '_query_writable_namespaces_async': <property object at 0x000001a793e11e40>, '_query_writable_namespaces_finish': <property object at 0x000001a793e11f30>, 'set_attribute': <property object at 0x000001a793e12020>, 'set_attributes_from_info': <property object at 0x000001a793e12160>, 'set_attributes_async': <property object at 0x000001a793e12250>, 'set_attributes_finish': <property object at 0x000001a793e12340>, 'read_fn': <property object at 0x000001a793e123e0>, 'read_async': <property object at 0x000001a793e124d0>, 'read_finish': <property object at 0x000001a793e125c0>, 'append_to': <property object at 0x000001a793e126b0>, 'append_to_async': <property object at 0x000001a793e127a0>, 'append_to_finish': <property object at 0x000001a793e128e0>, 'create': <property object at 0x000001a793e12980>, 'create_async': <property object at 0x000001a793e12a70>, 'create_finish': <property object at 0x000001a793e12b60>, 'replace': <property object at 0x000001a793e12c50>, 'replace_async': <property object at 0x000001a793e12d40>, 'replace_finish': <property object at 0x000001a793e12e30>, 'delete_file': <property object at 0x000001a793e12f20>, 'delete_file_async': <property object at 0x000001a793e13060>, 'delete_file_finish': <property object at 0x000001a793e131a0>, 'trash': <property object at 0x000001a793e13290>, 'trash_async': <property object at 0x000001a793e13380>, 'trash_finish': <property object at 0x000001a793e13470>, 'make_directory': <property object at 0x000001a793e13560>, 'make_directory_async': <property object at 0x000001a793e136a0>, 'make_directory_finish': <property object at 0x000001a793e13790>, 'make_symbolic_link': <property object at 0x000001a793e13880>, 'make_symbolic_link_async': <property object at 0x000001a793e13970>, 'make_symbolic_link_finish': <property object at 0x000001a793e13a60>, 'copy': <property object at 0x000001a793e13b00>, 'copy_async': <property object at 0x000001a793e13bf0>, 'copy_finish': <property object at 0x000001a793e13ce0>, 'move': <property object at 0x000001a793e13dd0>, 'move_async': <property object at 0x000001a793e13ec0>, 'move_finish': <property object at 0x000001a793e13fb0>, 'mount_mountable': <property object at 0x000001a793e0c0e0>, 'mount_mountable_finish': <property object at 0x000001a793e0c220>, 'unmount_mountable': <property object at 0x000001a793e0c310>, 'unmount_mountable_finish': <property object at 0x000001a793e0c400>, 'eject_mountable': <property object at 0x000001a793e0c4a0>, 'eject_mountable_finish': <property object at 0x000001a793e0c5e0>, 'mount_enclosing_volume': <property object at 0x000001a793e0c6d0>, 'mount_enclosing_volume_finish': <property object at 0x000001a793e0c7c0>, 'monitor_dir': <property object at 0x000001a793e0c860>, 'monitor_file': <property object at 0x000001a793e0c950>, 'open_readwrite': <property object at 0x000001a793e0ca40>, 'open_readwrite_async': <property object at 0x000001a793e0cb80>, 'open_readwrite_finish': <property object at 0x000001a793e0cc70>, 'create_readwrite': <property object at 0x000001a793e0cd60>, 'create_readwrite_async': <property object at 0x000001a793e0ce50>, 'create_readwrite_finish': <property object at 0x000001a793e0cf40>, 'replace_readwrite': <property object at 0x000001a793e0d030>, 'replace_readwrite_async': <property object at 0x000001a793e0d120>, 'replace_readwrite_finish': <property object at 0x000001a793e0d210>, 'start_mountable': <property object at 0x000001a793e0d2b0>, 'start_mountable_finish': <property object at 0x000001a793e0d3f0>, 'stop_mountable': <property object at 0x000001a793e0d490>, 'stop_mountable_finish': <property object at 0x000001a793e0d5d0>, 'supports_thread_contexts': <property object at 0x000001a793e0d6c0>, 'unmount_mountable_with_operation': <property object at 0x000001a793e0d760>, 'unmount_mountable_with_operation_finish': <property object at 0x000001a793e0d850>, 'eject_mountable_with_operation': <property object at 0x000001a793e0d990>, 'eject_mountable_with_operation_finish': <property object at 0x000001a793e0da30>, 'poll_mountable': <property object at 0x000001a793e0db20>, 'poll_mountable_finish': <property object at 0x000001a793e0dc60>, 'measure_disk_usage': <property object at 0x000001a793e0dd50>, 'measure_disk_usage_async': <property object at 0x000001a793e0de40>, 'measure_disk_usage_finish': <property object at 0x000001a793e0df80>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(FileIface)


