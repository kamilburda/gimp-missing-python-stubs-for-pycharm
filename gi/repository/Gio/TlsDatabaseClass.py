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


class TlsDatabaseClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        TlsDatabaseClass()
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

    create_certificate_handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lookup_certificates_issued_by = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lookup_certificates_issued_by_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lookup_certificates_issued_by_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lookup_certificate_for_handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lookup_certificate_for_handle_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lookup_certificate_for_handle_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lookup_certificate_issuer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lookup_certificate_issuer_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lookup_certificate_issuer_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    verify_chain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    verify_chain_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    verify_chain_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TlsDatabaseClass), '__module__': 'gi.repository.Gio', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'TlsDatabaseClass' objects>, '__weakref__': <attribute '__weakref__' of 'TlsDatabaseClass' objects>, '__doc__': None, 'parent_class': <property object at 0x000001a793dabab0>, 'verify_chain': <property object at 0x000001a793dabba0>, 'verify_chain_async': <property object at 0x000001a793dabce0>, 'verify_chain_finish': <property object at 0x000001a793dabdd0>, 'create_certificate_handle': <property object at 0x000001a793dabec0>, 'lookup_certificate_for_handle': <property object at 0x000001a793dabfb0>, 'lookup_certificate_for_handle_async': <property object at 0x000001a793da4090>, 'lookup_certificate_for_handle_finish': <property object at 0x000001a793da4180>, 'lookup_certificate_issuer': <property object at 0x000001a793da42c0>, 'lookup_certificate_issuer_async': <property object at 0x000001a793da43b0>, 'lookup_certificate_issuer_finish': <property object at 0x000001a793da4450>, 'lookup_certificates_issued_by': <property object at 0x000001a793da4590>, 'lookup_certificates_issued_by_async': <property object at 0x000001a793da4630>, 'lookup_certificates_issued_by_finish': <property object at 0x000001a793da4720>, 'padding': <property object at 0x000001a793da4810>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(TlsDatabaseClass)


