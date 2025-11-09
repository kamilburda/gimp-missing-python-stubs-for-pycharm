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


class DtlsConnection(__gobject.GInterface):
    # no doc
    def close(self, cancellable=None): # real signature unknown; restored from __doc__
        """ close(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def close_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ close_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def close_finish(self, result): # real signature unknown; restored from __doc__
        """ close_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def emit_accept_certificate(self, peer_cert, errors): # real signature unknown; restored from __doc__
        """ emit_accept_certificate(self, peer_cert:Gio.TlsCertificate, errors:Gio.TlsCertificateFlags) -> bool """
        return False

    def get_certificate(self): # real signature unknown; restored from __doc__
        """ get_certificate(self) -> Gio.TlsCertificate or None """
        pass

    def get_channel_binding_data(self, type): # real signature unknown; restored from __doc__
        """ get_channel_binding_data(self, type:Gio.TlsChannelBindingType) -> bool, data:list """
        return False

    def get_ciphersuite_name(self): # real signature unknown; restored from __doc__
        """ get_ciphersuite_name(self) -> str or None """
        return ""

    def get_database(self): # real signature unknown; restored from __doc__
        """ get_database(self) -> Gio.TlsDatabase or None """
        pass

    def get_interaction(self): # real signature unknown; restored from __doc__
        """ get_interaction(self) -> Gio.TlsInteraction or None """
        pass

    def get_negotiated_protocol(self): # real signature unknown; restored from __doc__
        """ get_negotiated_protocol(self) -> str or None """
        return ""

    def get_peer_certificate(self): # real signature unknown; restored from __doc__
        """ get_peer_certificate(self) -> Gio.TlsCertificate or None """
        pass

    def get_peer_certificate_errors(self): # real signature unknown; restored from __doc__
        """ get_peer_certificate_errors(self) -> Gio.TlsCertificateFlags """
        pass

    def get_protocol_version(self): # real signature unknown; restored from __doc__
        """ get_protocol_version(self) -> Gio.TlsProtocolVersion """
        pass

    def get_rehandshake_mode(self): # real signature unknown; restored from __doc__
        """ get_rehandshake_mode(self) -> Gio.TlsRehandshakeMode """
        pass

    def get_require_close_notify(self): # real signature unknown; restored from __doc__
        """ get_require_close_notify(self) -> bool """
        return False

    def handshake(self, cancellable=None): # real signature unknown; restored from __doc__
        """ handshake(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def handshake_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ handshake_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def handshake_finish(self, result): # real signature unknown; restored from __doc__
        """ handshake_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def set_advertised_protocols(self, protocols=None): # real signature unknown; restored from __doc__
        """ set_advertised_protocols(self, protocols:list=None) """
        pass

    def set_certificate(self, certificate): # real signature unknown; restored from __doc__
        """ set_certificate(self, certificate:Gio.TlsCertificate) """
        pass

    def set_database(self, database=None): # real signature unknown; restored from __doc__
        """ set_database(self, database:Gio.TlsDatabase=None) """
        pass

    def set_interaction(self, interaction=None): # real signature unknown; restored from __doc__
        """ set_interaction(self, interaction:Gio.TlsInteraction=None) """
        pass

    def set_rehandshake_mode(self, mode): # real signature unknown; restored from __doc__
        """ set_rehandshake_mode(self, mode:Gio.TlsRehandshakeMode) """
        pass

    def set_require_close_notify(self, require_close_notify): # real signature unknown; restored from __doc__
        """ set_require_close_notify(self, require_close_notify:bool) """
        pass

    def shutdown(self, shutdown_read, shutdown_write, cancellable=None): # real signature unknown; restored from __doc__
        """ shutdown(self, shutdown_read:bool, shutdown_write:bool, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def shutdown_async(self, shutdown_read, shutdown_write, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ shutdown_async(self, shutdown_read:bool, shutdown_write:bool, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def shutdown_finish(self, result): # real signature unknown; restored from __doc__
        """ shutdown_finish(self, result:Gio.AsyncResult) -> bool """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(DtlsConnection), '__module__': 'gi.repository.Gio', '__gtype__': <GType GDtlsConnection (2472623920)>, '__dict__': <attribute '__dict__' of 'DtlsConnection' objects>, '__weakref__': <attribute '__weakref__' of 'DtlsConnection' objects>, '__doc__': None, '__gsignals__': {}, 'close': gi.FunctionInfo(close, bound=None), 'close_async': gi.FunctionInfo(close_async, bound=None), 'close_finish': gi.FunctionInfo(close_finish, bound=None), 'emit_accept_certificate': gi.FunctionInfo(emit_accept_certificate, bound=None), 'get_certificate': gi.FunctionInfo(get_certificate, bound=None), 'get_channel_binding_data': gi.FunctionInfo(get_channel_binding_data, bound=None), 'get_ciphersuite_name': gi.FunctionInfo(get_ciphersuite_name, bound=None), 'get_database': gi.FunctionInfo(get_database, bound=None), 'get_interaction': gi.FunctionInfo(get_interaction, bound=None), 'get_negotiated_protocol': gi.FunctionInfo(get_negotiated_protocol, bound=None), 'get_peer_certificate': gi.FunctionInfo(get_peer_certificate, bound=None), 'get_peer_certificate_errors': gi.FunctionInfo(get_peer_certificate_errors, bound=None), 'get_protocol_version': gi.FunctionInfo(get_protocol_version, bound=None), 'get_rehandshake_mode': gi.FunctionInfo(get_rehandshake_mode, bound=None), 'get_require_close_notify': gi.FunctionInfo(get_require_close_notify, bound=None), 'handshake': gi.FunctionInfo(handshake, bound=None), 'handshake_async': gi.FunctionInfo(handshake_async, bound=None), 'handshake_finish': gi.FunctionInfo(handshake_finish, bound=None), 'set_advertised_protocols': gi.FunctionInfo(set_advertised_protocols, bound=None), 'set_certificate': gi.FunctionInfo(set_certificate, bound=None), 'set_database': gi.FunctionInfo(set_database, bound=None), 'set_interaction': gi.FunctionInfo(set_interaction, bound=None), 'set_rehandshake_mode': gi.FunctionInfo(set_rehandshake_mode, bound=None), 'set_require_close_notify': gi.FunctionInfo(set_require_close_notify, bound=None), 'shutdown': gi.FunctionInfo(shutdown, bound=None), 'shutdown_async': gi.FunctionInfo(shutdown_async, bound=None), 'shutdown_finish': gi.FunctionInfo(shutdown_finish, bound=None)})"
    __gdoc__ = 'Interface GDtlsConnection\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GDtlsConnection (2472623920)>'
    __info__ = InterfaceInfo(DtlsConnection)


