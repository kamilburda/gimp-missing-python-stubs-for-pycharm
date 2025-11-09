# encoding: utf-8
# module gi.repository.Gegl
# from C:/Program Files/GIMP 3/lib/girepository-1.0\Gegl-0.4.typelib
# by generator 1.147
"""
An object which wraps an introspection typelib.

    This wrapping creates a python module like representation of the typelib
    using gi repository as a foundation. Accessing attributes of the module
    will dynamically pull them in and create wrappers for the members.
    These members are then cached on this introspection module.
"""

# imports
from _thread import _lock

import gi as __gi
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class Path(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Path(**properties)
        new() -> Gegl.Path
        new_from_string(instructions:str) -> Gegl.Path
    """
    def add_type(self, type, items, description): # real signature unknown; restored from __doc__
        """ add_type(type:int, items:int, description:str) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def calc(self, pos): # real signature unknown; restored from __doc__
        """ calc(self, pos:float) -> bool, x:float, y:float """
        return False

    def calc_y_for_x(self, x): # real signature unknown; restored from __doc__
        """ calc_y_for_x(self, x:float) -> int, y:float """
        return 0

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def closest_point(self, x, y): # real signature unknown; restored from __doc__
        """ closest_point(self, x:float, y:float) -> float, on_path_x:float, on_path_y:float, node_pos_before:int """
        return 0.0

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_data(self, detailed_signal, handler, *data, **kwargs): # reliably restored by inspect
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

    def dirty(self): # real signature unknown; restored from __doc__
        """ dirty(self) """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def foreach(self, each_item, user_data=None): # real signature unknown; restored from __doc__
        """ foreach(self, each_item:Gegl.NodeFunction, user_data=None) """
        pass

    def foreach_flat(self, each_item, user_data=None): # real signature unknown; restored from __doc__
        """ foreach_flat(self, each_item:Gegl.NodeFunction, user_data=None) """
        pass

    def freeze(self): # real signature unknown; restored from __doc__
        """ freeze(self) """
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

    def get_bounds(self): # real signature unknown; restored from __doc__
        """ get_bounds(self) -> min_x:float, max_x:float, min_y:float, max_y:float """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_length(self): # real signature unknown; restored from __doc__
        """ get_length(self) -> float """
        return 0.0

    def get_matrix(self): # real signature unknown; restored from __doc__
        """ get_matrix(self) -> matrix:Gegl.Matrix3 """
        pass

    def get_node(self, index): # real signature unknown; restored from __doc__
        """ get_node(self, index:int) -> bool, node:Gegl.PathItem """
        return False

    def get_n_nodes(self): # real signature unknown; restored from __doc__
        """ get_n_nodes(self) -> int """
        return 0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

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

    def insert_node(self, pos, node): # real signature unknown; restored from __doc__
        """ insert_node(self, pos:int, node:Gegl.PathItem) """
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

    def is_empty(self): # real signature unknown; restored from __doc__
        """ is_empty(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Gegl.Path """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_from_string(self, instructions): # real signature unknown; restored from __doc__
        """ new_from_string(instructions:str) -> Gegl.Path """
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

    def parse_string(self, instructions): # real signature unknown; restored from __doc__
        """ parse_string(self, instructions:str) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_node(self, pos): # real signature unknown; restored from __doc__
        """ remove_node(self, pos:int) """
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_node(self, pos, node): # real signature unknown; restored from __doc__
        """ replace_node(self, pos:int, node:Gegl.PathItem) """
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self): # real signature unknown; restored from __doc__
        """ run_dispose(self) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_matrix(self, matrix): # real signature unknown; restored from __doc__
        """ set_matrix(self, matrix:Gegl.Matrix3) """
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

    def thaw(self): # real signature unknown; restored from __doc__
        """ thaw(self) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def _force_floating(self, *args, **kwargs): # real signature unknown
        """ force_floating(self) """
        pass

    def _ref(self, *args, **kwargs): # real signature unknown
        """ ref(self) -> GObject.Object """
        pass

    def _ref_sink(self, *args, **kwargs): # real signature unknown
        """ ref_sink(self) -> GObject.Object """
        pass

    def _unref(self, *args, **kwargs): # real signature unknown
        """ unref(self) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x000002761950cbb0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Path), '__module__': 'gi.repository.Gegl', '__gtype__': <GType GeglPath (420744496)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new, bound=None), 'new_from_string': gi.FunctionInfo(new_from_string, bound=None), 'add_type': gi.FunctionInfo(add_type, bound=None), 'calc': gi.FunctionInfo(calc, bound=None), 'calc_y_for_x': gi.FunctionInfo(calc_y_for_x, bound=None), 'clear': gi.FunctionInfo(clear, bound=None), 'closest_point': gi.FunctionInfo(closest_point, bound=None), 'dirty': gi.FunctionInfo(dirty, bound=None), 'foreach': gi.FunctionInfo(foreach, bound=None), 'foreach_flat': gi.FunctionInfo(foreach_flat, bound=None), 'freeze': gi.FunctionInfo(freeze, bound=None), 'get_bounds': gi.FunctionInfo(get_bounds, bound=None), 'get_length': gi.FunctionInfo(get_length, bound=None), 'get_matrix': gi.FunctionInfo(get_matrix, bound=None), 'get_n_nodes': gi.FunctionInfo(get_n_nodes, bound=None), 'get_node': gi.FunctionInfo(get_node, bound=None), 'insert_node': gi.FunctionInfo(insert_node, bound=None), 'is_empty': gi.FunctionInfo(is_empty, bound=None), 'parse_string': gi.FunctionInfo(parse_string, bound=None), 'remove_node': gi.FunctionInfo(remove_node, bound=None), 'replace_node': gi.FunctionInfo(replace_node, bound=None), 'set_matrix': gi.FunctionInfo(set_matrix, bound=None), 'thaw': gi.FunctionInfo(thaw, bound=None), 'to_string': gi.FunctionInfo(to_string, bound=None), 'parent_instance': <property object at 0x000002761b9085e0>})"
    __gdoc__ = 'Object GeglPath\n\nSignals from GeglPath:\n  changed (gpointer)\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GeglPath (420744496)>'
    __info__ = ObjectInfo(Path)


