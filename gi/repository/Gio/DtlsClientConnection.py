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


class DtlsClientConnection(__gobject.GInterface):
    # no doc
    def get_accepted_cas(self): # real signature unknown; restored from __doc__
        """ get_accepted_cas(self) -> list """
        return []

    def get_server_identity(self): # real signature unknown; restored from __doc__
        """ get_server_identity(self) -> Gio.SocketConnectable """
        pass

    def get_validation_flags(self): # real signature unknown; restored from __doc__
        """ get_validation_flags(self) -> Gio.TlsCertificateFlags """
        pass

    def new(self, base_socket, server_identity=None): # real signature unknown; restored from __doc__
        """ new(base_socket:Gio.DatagramBased, server_identity:Gio.SocketConnectable=None) -> Gio.DtlsClientConnection """
        pass

    def set_server_identity(self, identity): # real signature unknown; restored from __doc__
        """ set_server_identity(self, identity:Gio.SocketConnectable) """
        pass

    def set_validation_flags(self, flags): # real signature unknown; restored from __doc__
        """ set_validation_flags(self, flags:Gio.TlsCertificateFlags) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(DtlsClientConnection), '__module__': 'gi.repository.Gio', '__gtype__': <GType GDtlsClientConnection (2472623808)>, '__dict__': <attribute '__dict__' of 'DtlsClientConnection' objects>, '__weakref__': <attribute '__weakref__' of 'DtlsClientConnection' objects>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new, bound=None), 'get_accepted_cas': gi.FunctionInfo(get_accepted_cas, bound=None), 'get_server_identity': gi.FunctionInfo(get_server_identity, bound=None), 'get_validation_flags': gi.FunctionInfo(get_validation_flags, bound=None), 'set_server_identity': gi.FunctionInfo(set_server_identity, bound=None), 'set_validation_flags': gi.FunctionInfo(set_validation_flags, bound=None)})"
    __gdoc__ = 'Interface GDtlsClientConnection\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GDtlsClientConnection (2472623808)>'
    __info__ = InterfaceInfo(DtlsClientConnection)


