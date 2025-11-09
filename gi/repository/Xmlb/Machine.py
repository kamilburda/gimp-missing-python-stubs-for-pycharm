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


class Machine(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Machine(**properties)
        new() -> Xmlb.Machine
    """
    def add_method(self, name, n_opcodes, method_cb, user_data=None): # real signature unknown; restored from __doc__
        """ add_method(self, name:str, n_opcodes:int, method_cb:Xmlb.MachineMethodFunc, user_data=None) """
        pass

    def add_opcode_fixup(self, opcodes_sig, fixup_cb, user_data=None): # real signature unknown; restored from __doc__
        """ add_opcode_fixup(self, opcodes_sig:str, fixup_cb:Xmlb.MachineOpcodeFixupFunc, user_data=None) """
        pass

    def add_operator(self, p_str, name): # real signature unknown; restored from __doc__
        """ add_operator(self, str:str, name:str) """
        pass

    def add_text_handler(self, handler_cb, user_data=None): # real signature unknown; restored from __doc__
        """ add_text_handler(self, handler_cb:Xmlb.MachineTextHandlerFunc, user_data=None) """
        pass

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

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_stack_size(self): # real signature unknown; restored from __doc__
        """ get_stack_size(self) -> int """
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

    @classmethod
    def new(cls): # real signature unknown; restored from __doc__
        """ new() -> Xmlb.Machine """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def opcode_func_init(self, func_name): # real signature unknown; restored from __doc__
        """ opcode_func_init(self, func_name:str) -> bool, opcode:Xmlb.Opcode """
        return False

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def parse(self, text, text_len): # real signature unknown; restored from __doc__
        """ parse(self, text:str, text_len:int) -> Xmlb.Stack """
        pass

    def parse_full(self, text, text_len, flags): # real signature unknown; restored from __doc__
        """ parse_full(self, text:str, text_len:int, flags:Xmlb.MachineParseFlags) -> Xmlb.Stack """
        pass

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

    def run(self, opcodes, exec_data=None): # real signature unknown; restored from __doc__
        """ run(self, opcodes:Xmlb.Stack, exec_data=None) -> bool, result:bool """
        return False

    def run_dispose(self): # real signature unknown; restored from __doc__
        """ run_dispose(self) """
        pass

    def run_with_bindings(self, opcodes, bindings=None, exec_data=None): # real signature unknown; restored from __doc__
        """ run_with_bindings(self, opcodes:Xmlb.Stack, bindings:Xmlb.ValueBindings=None, exec_data=None) -> bool, result:bool """
        return False

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_debug_flags(self, flags): # real signature unknown; restored from __doc__
        """ set_debug_flags(self, flags:Xmlb.MachineDebugFlags) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_stack_size(self, stack_size): # real signature unknown; restored from __doc__
        """ set_stack_size(self, stack_size:int) """
        pass

    def stack_pop(self, stack): # real signature unknown; restored from __doc__
        """ stack_pop(self, stack:Xmlb.Stack) -> bool, opcode_out:Xmlb.Opcode """
        return False

    def stack_push(self, stack): # real signature unknown; restored from __doc__
        """ stack_push(self, stack:Xmlb.Stack) -> bool, opcode_out:Xmlb.Opcode """
        return False

    def stack_push_integer(self, stack, val): # real signature unknown; restored from __doc__
        """ stack_push_integer(self, stack:Xmlb.Stack, val:int) -> bool """
        return False

    def stack_push_text(self, stack, p_str): # real signature unknown; restored from __doc__
        """ stack_push_text(self, stack:Xmlb.Stack, str:str) -> bool """
        return False

    def stack_push_text_static(self, stack, p_str): # real signature unknown; restored from __doc__
        """ stack_push_text_static(self, stack:Xmlb.Stack, str:str) -> bool """
        return False

    def stack_push_text_steal(self, stack, p_str): # real signature unknown; restored from __doc__
        """ stack_push_text_steal(self, stack:Xmlb.Stack, str:str) -> bool """
        return False

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


    props = None # (!) real value is '<gi._gi.GProps object at 0x0000015431a48d00>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Machine), '__module__': 'gi.repository.Xmlb', '__gtype__': <GType XbMachine (844628848)>, '__doc__': None, '__gsignals__': {}, 'new': <classmethod(gi.FunctionInfo(new))>, 'add_method': gi.FunctionInfo(add_method), 'add_opcode_fixup': gi.FunctionInfo(add_opcode_fixup), 'add_operator': gi.FunctionInfo(add_operator), 'add_text_handler': gi.FunctionInfo(add_text_handler), 'get_stack_size': gi.FunctionInfo(get_stack_size), 'opcode_func_init': gi.FunctionInfo(opcode_func_init), 'parse': gi.FunctionInfo(parse), 'parse_full': gi.FunctionInfo(parse_full), 'run': gi.FunctionInfo(run), 'run_with_bindings': gi.FunctionInfo(run_with_bindings), 'set_debug_flags': gi.FunctionInfo(set_debug_flags), 'set_stack_size': gi.FunctionInfo(set_stack_size), 'stack_pop': gi.FunctionInfo(stack_pop), 'stack_push': gi.FunctionInfo(stack_push), 'stack_push_integer': gi.FunctionInfo(stack_push_integer), 'stack_push_text': gi.FunctionInfo(stack_push_text), 'stack_push_text_static': gi.FunctionInfo(stack_push_text_static), 'stack_push_text_steal': gi.FunctionInfo(stack_push_text_steal), 'parent_instance': <property object at 0x0000015434729d00>})"
    __gdoc__ = 'Object XbMachine\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType XbMachine (844628848)>'
    __info__ = ObjectInfo(Machine)


