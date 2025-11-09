# encoding: utf-8
# module gi.repository.Xmlb
# from C:/Program Files/GIMP 3/lib/girepository-1.0\Xmlb-2.0.typelib
# by generator 1.147
# no doc

# imports
from _thread import _lock

import enum as __enum
import gi as __gi
import gi.overrides.GObject as __gi_overrides_GObject


class Node(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Node(**properties)
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_data(self, detailed_signal, handler, *data, connect_flags=0): # reliably restored by inspect
        """
        Connect a callback to the given signal with optional user data.
        
                :param str detailed_signal:
                    A detailed signal to connect to.
                :param callable handler:
                    Callback handler to connect to the signal.
                :param *data:
                    Variable data which is passed through to the signal handler.
                :param GObject.ConnectFlags connect_flags:
                    Flags used for connection options.
                :returns:
                    A signal id which can be used with disconnect.
        """
        pass

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_dispose(self, *args, **kwargs): # real signature unknown
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def export(self, flags): # real signature unknown; restored from __doc__
        """ export(self, flags:Xmlb.NodeExportFlags) -> str """
        return ""

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def freeze_notify(self): # reliably restored by inspect
        """
        Freezes the object's property-changed notification queue.
        
                :returns:
                    A context manager which optionally can be used to
                    automatically thaw notifications.
        
                This will freeze the object so that "notify" signals are blocked until
                the thaw_notify() method is called.
        
                .. code-block:: python
        
                    with obj.freeze_notify():
                        pass
        """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_attr(self, name): # real signature unknown; restored from __doc__
        """ get_attr(self, name:str) -> str """
        return ""

    def get_attr_as_uint(self, name): # real signature unknown; restored from __doc__
        """ get_attr_as_uint(self, name:str) -> int """
        return 0

    def get_child(self): # real signature unknown; restored from __doc__
        """ get_child(self) -> Xmlb.Node """
        pass

    def get_children(self): # real signature unknown; restored from __doc__
        """ get_children(self) -> list """
        return []

    def get_data(self, key): # real signature unknown; restored from __doc__
        """ get_data(self, key:str) -> GLib.Bytes """
        pass

    def get_depth(self): # real signature unknown; restored from __doc__
        """ get_depth(self) -> int """
        return 0

    def get_element(self): # real signature unknown; restored from __doc__
        """ get_element(self) -> str """
        return ""

    def get_next(self): # real signature unknown; restored from __doc__
        """ get_next(self) -> Xmlb.Node """
        pass

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Xmlb.Node """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_root(self): # real signature unknown; restored from __doc__
        """ get_root(self) -> Xmlb.Node """
        pass

    def get_silo(self): # real signature unknown; restored from __doc__
        """ get_silo(self) -> Xmlb.Silo """
        pass

    def get_tail(self): # real signature unknown; restored from __doc__
        """ get_tail(self) -> str """
        return ""

    def get_text(self): # real signature unknown; restored from __doc__
        """ get_text(self) -> str """
        return ""

    def get_text_as_uint(self): # real signature unknown; restored from __doc__
        """ get_text_as_uint(self) -> int """
        return 0

    def handler_block(obj, handler_id): # reliably restored by inspect
        """
        Blocks the signal handler from being invoked until
            handler_unblock() is called.
        
            :param GObject.Object obj:
                Object instance to block handlers for.
            :param int handler_id:
                Id of signal to block.
            :returns:
                A context manager which optionally can be used to
                automatically unblock the handler:
        
            .. code-block:: python
        
                with GObject.signal_handler_block(obj, id):
                    pass
        """
        pass

    def handler_block_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def handler_disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def handler_is_connected(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_is_connected(instance:GObject.Object, handler_id:int) -> bool """
        pass

    def handler_unblock(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_unblock(instance:GObject.Object, handler_id:int) """
        pass

    def handler_unblock_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def interface_find_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_install_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_list_properties(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def query(self, xpath, limit): # real signature unknown; restored from __doc__
        """ query(self, xpath:str, limit:int) -> list """
        return []

    def query_attr(self, xpath, name): # real signature unknown; restored from __doc__
        """ query_attr(self, xpath:str, name:str) -> str """
        return ""

    def query_attr_as_uint(self, xpath, name): # real signature unknown; restored from __doc__
        """ query_attr_as_uint(self, xpath:str, name:str) -> int """
        return 0

    def query_export(self, xpath): # real signature unknown; restored from __doc__
        """ query_export(self, xpath:str) -> str """
        return ""

    def query_first(self, xpath): # real signature unknown; restored from __doc__
        """ query_first(self, xpath:str) -> Xmlb.Node """
        pass

    def query_first_full(self, query): # real signature unknown; restored from __doc__
        """ query_first_full(self, query:Xmlb.Query) -> Xmlb.Node """
        pass

    def query_first_with_context(self, query, context=None): # real signature unknown; restored from __doc__
        """ query_first_with_context(self, query:Xmlb.Query, context:Xmlb.QueryContext=None) -> Xmlb.Node """
        pass

    def query_full(self, query): # real signature unknown; restored from __doc__
        """ query_full(self, query:Xmlb.Query) -> list """
        return []

    def query_text(self, xpath): # real signature unknown; restored from __doc__
        """ query_text(self, xpath:str) -> str """
        return ""

    def query_text_as_uint(self, xpath): # real signature unknown; restored from __doc__
        """ query_text_as_uint(self, xpath:str) -> int """
        return 0

    def query_with_context(self, query, context=None): # real signature unknown; restored from __doc__
        """ query_with_context(self, query:Xmlb.Query, context:Xmlb.QueryContext=None) -> list """
        return []

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self): # real signature unknown; restored from __doc__
        """ run_dispose(self) """
        pass

    def set_data(self, key, data): # real signature unknown; restored from __doc__
        """ set_data(self, key:str, data:GLib.Bytes) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stop_emission(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def stop_emission_by_name(*args, **kwargs): # reliably restored by inspect
        """ signal_stop_emission_by_name(instance:GObject.Object, detailed_signal:str) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def transmogrify(self, func_text, func_tail, user_data=None): # real signature unknown; restored from __doc__
        """ transmogrify(self, func_text:Xmlb.NodeTransmogrifyFunc, func_tail:Xmlb.NodeTransmogrifyFunc, user_data=None) -> bool """
        return False

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def _force_floating(self): # reliably restored by inspect
        """ Deprecated, do not explicitly float GObjects. """
        pass

    def _ref(self): # reliably restored by inspect
        """ Deprecated, do not explicitly reference GObjects. """
        pass

    def _ref_sink(self): # reliably restored by inspect
        """ Deprecated, do not explicitly reference GObjects. """
        pass

    def _unref(self): # reliably restored by inspect
        """ Deprecated, do not explicitly reference GObjects. """
        pass

    def _unsupported_data_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def _unsupported_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, **properties): # real signature unknown; restored from __doc__
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x0000015431a49390>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Node), '__module__': 'gi.repository.Xmlb', '__gtype__': <GType XbNode (844627888)>, '__doc__': None, '__gsignals__': {}, 'export': gi.FunctionInfo(export), 'get_attr': gi.FunctionInfo(get_attr), 'get_attr_as_uint': gi.FunctionInfo(get_attr_as_uint), 'get_child': gi.FunctionInfo(get_child), 'get_children': gi.FunctionInfo(get_children), 'get_data': gi.FunctionInfo(get_data), 'get_depth': gi.FunctionInfo(get_depth), 'get_element': gi.FunctionInfo(get_element), 'get_next': gi.FunctionInfo(get_next), 'get_parent': gi.FunctionInfo(get_parent), 'get_root': gi.FunctionInfo(get_root), 'get_silo': gi.FunctionInfo(get_silo), 'get_tail': gi.FunctionInfo(get_tail), 'get_text': gi.FunctionInfo(get_text), 'get_text_as_uint': gi.FunctionInfo(get_text_as_uint), 'query': gi.FunctionInfo(query), 'query_attr': gi.FunctionInfo(query_attr), 'query_attr_as_uint': gi.FunctionInfo(query_attr_as_uint), 'query_export': gi.FunctionInfo(query_export), 'query_first': gi.FunctionInfo(query_first), 'query_first_full': gi.FunctionInfo(query_first_full), 'query_first_with_context': gi.FunctionInfo(query_first_with_context), 'query_full': gi.FunctionInfo(query_full), 'query_text': gi.FunctionInfo(query_text), 'query_text_as_uint': gi.FunctionInfo(query_text_as_uint), 'query_with_context': gi.FunctionInfo(query_with_context), 'set_data': gi.FunctionInfo(set_data), 'transmogrify': gi.FunctionInfo(transmogrify), 'parent_instance': <property object at 0x000001543472a700>})"
    __gdoc__ = 'Object XbNode\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType XbNode (844627888)>'
    __info__ = ObjectInfo(Node)


