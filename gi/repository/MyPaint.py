# encoding: utf-8
# module gi.repository.MyPaint
# from C:/Program Files/GIMP 3/lib/girepository-1.0\MyPaint-1.6.typelib
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
import gobject as __gobject


# Variables with simple values

_namespace = 'MyPaint'

_version = '1.6'

__weakref__ = None

# functions

def brush_input_from_cname(cname): # real signature unknown; restored from __doc__
    """ brush_input_from_cname(cname:str) -> MyPaint.BrushInput """
    pass

def brush_input_info(id): # real signature unknown; restored from __doc__
    """ brush_input_info(id:MyPaint.BrushInput) -> MyPaint.BrushInputInfo """
    pass

def brush_setting_from_cname(cname): # real signature unknown; restored from __doc__
    """ brush_setting_from_cname(cname:str) -> MyPaint.BrushSetting """
    pass

def brush_setting_info(id): # real signature unknown; restored from __doc__
    """ brush_setting_info(id:MyPaint.BrushSetting) -> MyPaint.BrushSettingInfo """
    pass

def __delattr__(*args, **kwargs): # real signature unknown
    """ Implement delattr(self, name). """
    pass

def __dir__(*args, **kwargs): # real signature unknown
    pass

def __eq__(*args, **kwargs): # real signature unknown
    """ Return self==value. """
    pass

def __format__(*args, **kwargs): # real signature unknown
    """ Default object formatter. """
    pass

def __getattribute__(*args, **kwargs): # real signature unknown
    """ Return getattr(self, name). """
    pass

def __getattr__(*args, **kwargs): # real signature unknown
    pass

def __getstate__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __ge__(*args, **kwargs): # real signature unknown
    """ Return self>=value. """
    pass

def __gt__(*args, **kwargs): # real signature unknown
    """ Return self>value. """
    pass

def __hash__(*args, **kwargs): # real signature unknown
    """ Return hash(self). """
    pass

def __init_subclass__(*args, **kwargs): # real signature unknown
    """
    This method is called when a class is subclassed.
    
    The default implementation does nothing. It may be
    overridden to extend subclasses.
    """
    pass

def __init__(*args, **kwargs): # real signature unknown
    """ Might raise gi._gi.RepositoryError """
    pass

def __le__(*args, **kwargs): # real signature unknown
    """ Return self<=value. """
    pass

def __lt__(*args, **kwargs): # real signature unknown
    """ Return self<value. """
    pass

@staticmethod # known case of __new__
def __new__(*args, **kwargs): # real signature unknown
    """ Create and return a new object.  See help(type) for accurate signature. """
    pass

def __ne__(*args, **kwargs): # real signature unknown
    """ Return self!=value. """
    pass

def __reduce_ex__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __reduce__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __repr__(*args, **kwargs): # real signature unknown
    pass

def __setattr__(*args, **kwargs): # real signature unknown
    """ Implement setattr(self, name, value). """
    pass

def __sizeof__(*args, **kwargs): # real signature unknown
    """ Size of object in memory, in bytes. """
    pass

def __str__(*args, **kwargs): # real signature unknown
    """ Return str(self). """
    pass

def __subclasshook__(*args, **kwargs): # real signature unknown
    """
    Abstract classes can override this to customize issubclass().
    
    This is invoked early on by abc.ABCMeta.__subclasscheck__().
    It should return True, False or NotImplemented.  If it returns
    NotImplemented, the normal algorithm is used.  Otherwise, it
    overrides the normal algorithm (and the outcome is cached).
    """
    pass

# classes

class Brush(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new() -> MyPaint.Brush
        new_with_buckets(num_smudge_buckets:int) -> MyPaint.Brush
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def from_defaults(self): # real signature unknown; restored from __doc__
        """ from_defaults(self) """
        pass

    def from_string(self, string): # real signature unknown; restored from __doc__
        """ from_string(self, string:str) -> bool """
        return False

    def get_base_value(self, id): # real signature unknown; restored from __doc__
        """ get_base_value(self, id:MyPaint.BrushSetting) -> float """
        return 0.0

    def get_inputs_used_n(self, id): # real signature unknown; restored from __doc__
        """ get_inputs_used_n(self, id:MyPaint.BrushSetting) -> int """
        return 0

    def get_mapping_n(self, id, input): # real signature unknown; restored from __doc__
        """ get_mapping_n(self, id:MyPaint.BrushSetting, input:MyPaint.BrushInput) -> int """
        return 0

    def get_mapping_point(self, id, input, index): # real signature unknown; restored from __doc__
        """ get_mapping_point(self, id:MyPaint.BrushSetting, input:MyPaint.BrushInput, index:int) -> x:float, y:float """
        pass

    def get_state(self, i): # real signature unknown; restored from __doc__
        """ get_state(self, i:MyPaint.BrushState) -> float """
        return 0.0

    def get_total_stroke_painting_time(self): # real signature unknown; restored from __doc__
        """ get_total_stroke_painting_time(self) -> float """
        return 0.0

    def input_from_cname(self, cname): # real signature unknown; restored from __doc__
        """ input_from_cname(cname:str) -> MyPaint.BrushInput """
        pass

    def is_constant(self, id): # real signature unknown; restored from __doc__
        """ is_constant(self, id:MyPaint.BrushSetting) -> bool """
        return False

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> MyPaint.Brush """
        pass

    def new_stroke(self): # real signature unknown; restored from __doc__
        """ new_stroke(self) """
        pass

    def new_with_buckets(self, num_smudge_buckets): # real signature unknown; restored from __doc__
        """ new_with_buckets(num_smudge_buckets:int) -> MyPaint.Brush """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def setting_from_cname(self, cname): # real signature unknown; restored from __doc__
        """ setting_from_cname(cname:str) -> MyPaint.BrushSetting """
        pass

    def set_base_value(self, id, value): # real signature unknown; restored from __doc__
        """ set_base_value(self, id:MyPaint.BrushSetting, value:float) """
        pass

    def set_mapping_n(self, id, input, n): # real signature unknown; restored from __doc__
        """ set_mapping_n(self, id:MyPaint.BrushSetting, input:MyPaint.BrushInput, n:int) """
        pass

    def set_mapping_point(self, id, input, index, x, y): # real signature unknown; restored from __doc__
        """ set_mapping_point(self, id:MyPaint.BrushSetting, input:MyPaint.BrushInput, index:int, x:float, y:float) """
        pass

    def set_print_inputs(self, enabled): # real signature unknown; restored from __doc__
        """ set_print_inputs(self, enabled:bool) """
        pass

    def set_state(self, i, value): # real signature unknown; restored from __doc__
        """ set_state(self, i:MyPaint.BrushState, value:float) """
        pass

    def stroke_to(self, surface, x, y, pressure, xtilt, ytilt, dtime): # real signature unknown; restored from __doc__
        """ stroke_to(self, surface:MyPaint.Surface, x:float, y:float, pressure:float, xtilt:float, ytilt:float, dtime:float) -> int """
        return 0

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
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

    def __init__(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ new() -> MyPaint.Brush """
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Brush), '__module__': 'gi.repository.MyPaint', '__gtype__': <GType MyPaintBrush (3895785760)>, '__dict__': <attribute '__dict__' of 'Brush' objects>, '__weakref__': <attribute '__weakref__' of 'Brush' objects>, '__doc__': None, 'new': gi.FunctionInfo(new, bound=None), 'new_with_buckets': gi.FunctionInfo(new_with_buckets, bound=None), 'from_defaults': gi.FunctionInfo(from_defaults, bound=None), 'from_string': gi.FunctionInfo(from_string, bound=None), 'get_base_value': gi.FunctionInfo(get_base_value, bound=None), 'get_inputs_used_n': gi.FunctionInfo(get_inputs_used_n, bound=None), 'get_mapping_n': gi.FunctionInfo(get_mapping_n, bound=None), 'get_mapping_point': gi.FunctionInfo(get_mapping_point, bound=None), 'get_state': gi.FunctionInfo(get_state, bound=None), 'get_total_stroke_painting_time': gi.FunctionInfo(get_total_stroke_painting_time, bound=None), 'is_constant': gi.FunctionInfo(is_constant, bound=None), 'new_stroke': gi.FunctionInfo(new_stroke, bound=None), 'reset': gi.FunctionInfo(reset, bound=None), 'set_base_value': gi.FunctionInfo(set_base_value, bound=None), 'set_mapping_n': gi.FunctionInfo(set_mapping_n, bound=None), 'set_mapping_point': gi.FunctionInfo(set_mapping_point, bound=None), 'set_print_inputs': gi.FunctionInfo(set_print_inputs, bound=None), 'set_state': gi.FunctionInfo(set_state, bound=None), 'stroke_to': gi.FunctionInfo(stroke_to, bound=None), 'input_from_cname': gi.FunctionInfo(input_from_cname, bound=None), 'setting_from_cname': gi.FunctionInfo(setting_from_cname, bound=None), '__new__': <staticmethod(gi.FunctionInfo(new, bound=None))>, '__init__': <function nothing at 0x00000230e89d8680>})"
    __gtype__ = None # (!) real value is '<GType MyPaintBrush (3895785760)>'
    __info__ = StructInfo(Brush)


class BrushInput(__gobject.GEnum):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_count(self): # real signature unknown; restored from __doc__
        """
        Number of ones in the binary representation of the absolute value of self.
        
        Also known as the population count.
        
        >>> bin(13)
        '0b1101'
        >>> (13).bit_count()
        3
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.  Default is to use 'big'.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.  Default
            is length 1.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.  Default is to use 'big'.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    INPUTS_COUNT = 18
    INPUT_ATTACK_ANGLE = 10
    INPUT_BARREL_ROTATION = 16
    INPUT_BRUSH_RADIUS = 17
    INPUT_CUSTOM = 8
    INPUT_DIRECTION = 5
    INPUT_DIRECTION_ANGLE = 9
    INPUT_GRIDMAP_X = 13
    INPUT_GRIDMAP_Y = 14
    INPUT_PRESSURE = 0
    INPUT_RANDOM = 3
    INPUT_SPEED1 = 1
    INPUT_SPEED2 = 2
    INPUT_STROKE = 4
    INPUT_TILT_ASCENSION = 7
    INPUT_TILT_DECLINATION = 6
    INPUT_TILT_DECLINATIONX = 11
    INPUT_TILT_DECLINATIONY = 12
    INPUT_VIEWZOOM = 15
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.MyPaint', '__dict__': <attribute '__dict__' of 'BrushInput' objects>, '__doc__': None, '__gtype__': <GType PyMyPaintBrushInput (3895786320)>, '__enum_values__': {0: <enum MYPAINT_BRUSH_INPUT_PRESSURE of type MyPaint.BrushInput>, 1: <enum MYPAINT_BRUSH_INPUT_SPEED1 of type MyPaint.BrushInput>, 2: <enum MYPAINT_BRUSH_INPUT_SPEED2 of type MyPaint.BrushInput>, 3: <enum MYPAINT_BRUSH_INPUT_RANDOM of type MyPaint.BrushInput>, 4: <enum MYPAINT_BRUSH_INPUT_STROKE of type MyPaint.BrushInput>, 5: <enum MYPAINT_BRUSH_INPUT_DIRECTION of type MyPaint.BrushInput>, 6: <enum MYPAINT_BRUSH_INPUT_TILT_DECLINATION of type MyPaint.BrushInput>, 7: <enum MYPAINT_BRUSH_INPUT_TILT_ASCENSION of type MyPaint.BrushInput>, 8: <enum MYPAINT_BRUSH_INPUT_CUSTOM of type MyPaint.BrushInput>, 9: <enum MYPAINT_BRUSH_INPUT_DIRECTION_ANGLE of type MyPaint.BrushInput>, 10: <enum MYPAINT_BRUSH_INPUT_ATTACK_ANGLE of type MyPaint.BrushInput>, 11: <enum MYPAINT_BRUSH_INPUT_TILT_DECLINATIONX of type MyPaint.BrushInput>, 12: <enum MYPAINT_BRUSH_INPUT_TILT_DECLINATIONY of type MyPaint.BrushInput>, 13: <enum MYPAINT_BRUSH_INPUT_GRIDMAP_X of type MyPaint.BrushInput>, 14: <enum MYPAINT_BRUSH_INPUT_GRIDMAP_Y of type MyPaint.BrushInput>, 15: <enum MYPAINT_BRUSH_INPUT_VIEWZOOM of type MyPaint.BrushInput>, 16: <enum MYPAINT_BRUSH_INPUT_BARREL_ROTATION of type MyPaint.BrushInput>, 17: <enum MYPAINT_BRUSH_INPUT_BRUSH_RADIUS of type MyPaint.BrushInput>, 18: <enum MYPAINT_BRUSH_INPUTS_COUNT of type MyPaint.BrushInput>}, '__info__': gi.EnumInfo(BrushInput), 'INPUT_PRESSURE': <enum MYPAINT_BRUSH_INPUT_PRESSURE of type MyPaint.BrushInput>, 'INPUT_SPEED1': <enum MYPAINT_BRUSH_INPUT_SPEED1 of type MyPaint.BrushInput>, 'INPUT_SPEED2': <enum MYPAINT_BRUSH_INPUT_SPEED2 of type MyPaint.BrushInput>, 'INPUT_RANDOM': <enum MYPAINT_BRUSH_INPUT_RANDOM of type MyPaint.BrushInput>, 'INPUT_STROKE': <enum MYPAINT_BRUSH_INPUT_STROKE of type MyPaint.BrushInput>, 'INPUT_DIRECTION': <enum MYPAINT_BRUSH_INPUT_DIRECTION of type MyPaint.BrushInput>, 'INPUT_TILT_DECLINATION': <enum MYPAINT_BRUSH_INPUT_TILT_DECLINATION of type MyPaint.BrushInput>, 'INPUT_TILT_ASCENSION': <enum MYPAINT_BRUSH_INPUT_TILT_ASCENSION of type MyPaint.BrushInput>, 'INPUT_CUSTOM': <enum MYPAINT_BRUSH_INPUT_CUSTOM of type MyPaint.BrushInput>, 'INPUT_DIRECTION_ANGLE': <enum MYPAINT_BRUSH_INPUT_DIRECTION_ANGLE of type MyPaint.BrushInput>, 'INPUT_ATTACK_ANGLE': <enum MYPAINT_BRUSH_INPUT_ATTACK_ANGLE of type MyPaint.BrushInput>, 'INPUT_TILT_DECLINATIONX': <enum MYPAINT_BRUSH_INPUT_TILT_DECLINATIONX of type MyPaint.BrushInput>, 'INPUT_TILT_DECLINATIONY': <enum MYPAINT_BRUSH_INPUT_TILT_DECLINATIONY of type MyPaint.BrushInput>, 'INPUT_GRIDMAP_X': <enum MYPAINT_BRUSH_INPUT_GRIDMAP_X of type MyPaint.BrushInput>, 'INPUT_GRIDMAP_Y': <enum MYPAINT_BRUSH_INPUT_GRIDMAP_Y of type MyPaint.BrushInput>, 'INPUT_VIEWZOOM': <enum MYPAINT_BRUSH_INPUT_VIEWZOOM of type MyPaint.BrushInput>, 'INPUT_BARREL_ROTATION': <enum MYPAINT_BRUSH_INPUT_BARREL_ROTATION of type MyPaint.BrushInput>, 'INPUT_BRUSH_RADIUS': <enum MYPAINT_BRUSH_INPUT_BRUSH_RADIUS of type MyPaint.BrushInput>, 'INPUTS_COUNT': <enum MYPAINT_BRUSH_INPUTS_COUNT of type MyPaint.BrushInput>})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 11,
        12: 12,
        13: 13,
        14: 14,
        15: 15,
        16: 16,
        17: 17,
        18: 18,
    }
    __gtype__ = None # (!) real value is '<GType PyMyPaintBrushInput (3895786320)>'
    __info__ = gi.EnumInfo(BrushInput)


class BrushInputInfo(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        BrushInputInfo()
    """
    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_tooltip(self): # real signature unknown; restored from __doc__
        """ get_tooltip(self) -> str """
        return ""

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

    cname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hard_max = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hard_min = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    soft_max = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    soft_min = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tooltip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(BrushInputInfo), '__module__': 'gi.repository.MyPaint', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'BrushInputInfo' objects>, '__weakref__': <attribute '__weakref__' of 'BrushInputInfo' objects>, '__doc__': None, 'cname': <property object at 0x00000230e8ca1da0>, 'hard_min': <property object at 0x00000230e8ca1e90>, 'soft_min': <property object at 0x00000230e8ca1f80>, 'normal': <property object at 0x00000230e8ca2070>, 'soft_max': <property object at 0x00000230e8ca2160>, 'hard_max': <property object at 0x00000230e8ca2250>, 'name': <property object at 0x00000230e8ca2340>, 'tooltip': <property object at 0x00000230e8ca2430>, 'get_name': gi.FunctionInfo(get_name, bound=None), 'get_tooltip': gi.FunctionInfo(get_tooltip, bound=None)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(BrushInputInfo)


class BrushSetting(__gobject.GEnum):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_count(self): # real signature unknown; restored from __doc__
        """
        Number of ones in the binary representation of the absolute value of self.
        
        Also known as the population count.
        
        >>> bin(13)
        '0b1101'
        >>> (13).bit_count()
        3
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.  Default is to use 'big'.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.  Default
            is length 1.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.  Default is to use 'big'.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    SETTINGS_COUNT = 64
    SETTING_ANTI_ALIASING = 5
    SETTING_CHANGE_COLOR_H = 24
    SETTING_CHANGE_COLOR_HSL_S = 26
    SETTING_CHANGE_COLOR_HSV_S = 28
    SETTING_CHANGE_COLOR_L = 25
    SETTING_CHANGE_COLOR_V = 27
    SETTING_COLORIZE = 42
    SETTING_COLOR_H = 20
    SETTING_COLOR_S = 21
    SETTING_COLOR_V = 22
    SETTING_CUSTOM_INPUT = 36
    SETTING_CUSTOM_INPUT_SLOWNESS = 37
    SETTING_DABS_PER_ACTUAL_RADIUS = 7
    SETTING_DABS_PER_BASIC_RADIUS = 6
    SETTING_DABS_PER_SECOND = 8
    SETTING_DIRECTION_FILTER = 40
    SETTING_ELLIPTICAL_DAB_ANGLE = 39
    SETTING_ELLIPTICAL_DAB_RATIO = 38
    SETTING_ERASER = 32
    SETTING_GRIDMAP_SCALE = 45
    SETTING_GRIDMAP_SCALE_X = 46
    SETTING_GRIDMAP_SCALE_Y = 47
    SETTING_HARDNESS = 4
    SETTING_LOCK_ALPHA = 41
    SETTING_OFFSET_ANGLE = 53
    SETTING_OFFSET_ANGLE_2 = 56
    SETTING_OFFSET_ANGLE_2_ASC = 57
    SETTING_OFFSET_ANGLE_2_VIEW = 58
    SETTING_OFFSET_ANGLE_ADJ = 59
    SETTING_OFFSET_ANGLE_ASC = 54
    SETTING_OFFSET_ANGLE_VIEW = 55
    SETTING_OFFSET_BY_RANDOM = 14
    SETTING_OFFSET_BY_SPEED = 15
    SETTING_OFFSET_BY_SPEED_SLOWNESS = 16
    SETTING_OFFSET_MULTIPLIER = 60
    SETTING_OFFSET_X = 52
    SETTING_OFFSET_Y = 51
    SETTING_OPAQUE = 0
    SETTING_OPAQUE_LINEARIZE = 2
    SETTING_OPAQUE_MULTIPLY = 1
    SETTING_PAINT_MODE = 63
    SETTING_POSTERIZE = 61
    SETTING_POSTERIZE_NUM = 62
    SETTING_PRESSURE_GAIN_LOG = 44
    SETTING_RADIUS_BY_RANDOM = 9
    SETTING_RADIUS_LOGARITHMIC = 3
    SETTING_RESTORE_COLOR = 23
    SETTING_SLOW_TRACKING = 17
    SETTING_SLOW_TRACKING_PER_DAB = 18
    SETTING_SMUDGE = 29
    SETTING_SMUDGE_BUCKET = 49
    SETTING_SMUDGE_LENGTH = 30
    SETTING_SMUDGE_LENGTH_LOG = 48
    SETTING_SMUDGE_RADIUS_LOG = 31
    SETTING_SMUDGE_TRANSPARENCY = 50
    SETTING_SNAP_TO_PIXEL = 43
    SETTING_SPEED1_GAMMA = 12
    SETTING_SPEED1_SLOWNESS = 10
    SETTING_SPEED2_GAMMA = 13
    SETTING_SPEED2_SLOWNESS = 11
    SETTING_STROKE_DURATION_LOGARITHMIC = 34
    SETTING_STROKE_HOLDTIME = 35
    SETTING_STROKE_THRESHOLD = 33
    SETTING_TRACKING_NOISE = 19
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.MyPaint', '__dict__': <attribute '__dict__' of 'BrushSetting' objects>, '__doc__': None, '__gtype__': <GType PyMyPaintBrushSetting (3895786432)>, '__enum_values__': {0: <enum MYPAINT_BRUSH_SETTING_OPAQUE of type MyPaint.BrushSetting>, 1: <enum MYPAINT_BRUSH_SETTING_OPAQUE_MULTIPLY of type MyPaint.BrushSetting>, 2: <enum MYPAINT_BRUSH_SETTING_OPAQUE_LINEARIZE of type MyPaint.BrushSetting>, 3: <enum MYPAINT_BRUSH_SETTING_RADIUS_LOGARITHMIC of type MyPaint.BrushSetting>, 4: <enum MYPAINT_BRUSH_SETTING_HARDNESS of type MyPaint.BrushSetting>, 5: <enum MYPAINT_BRUSH_SETTING_ANTI_ALIASING of type MyPaint.BrushSetting>, 6: <enum MYPAINT_BRUSH_SETTING_DABS_PER_BASIC_RADIUS of type MyPaint.BrushSetting>, 7: <enum MYPAINT_BRUSH_SETTING_DABS_PER_ACTUAL_RADIUS of type MyPaint.BrushSetting>, 8: <enum MYPAINT_BRUSH_SETTING_DABS_PER_SECOND of type MyPaint.BrushSetting>, 9: <enum MYPAINT_BRUSH_SETTING_RADIUS_BY_RANDOM of type MyPaint.BrushSetting>, 10: <enum MYPAINT_BRUSH_SETTING_SPEED1_SLOWNESS of type MyPaint.BrushSetting>, 11: <enum MYPAINT_BRUSH_SETTING_SPEED2_SLOWNESS of type MyPaint.BrushSetting>, 12: <enum MYPAINT_BRUSH_SETTING_SPEED1_GAMMA of type MyPaint.BrushSetting>, 13: <enum MYPAINT_BRUSH_SETTING_SPEED2_GAMMA of type MyPaint.BrushSetting>, 14: <enum MYPAINT_BRUSH_SETTING_OFFSET_BY_RANDOM of type MyPaint.BrushSetting>, 15: <enum MYPAINT_BRUSH_SETTING_OFFSET_BY_SPEED of type MyPaint.BrushSetting>, 16: <enum MYPAINT_BRUSH_SETTING_OFFSET_BY_SPEED_SLOWNESS of type MyPaint.BrushSetting>, 17: <enum MYPAINT_BRUSH_SETTING_SLOW_TRACKING of type MyPaint.BrushSetting>, 18: <enum MYPAINT_BRUSH_SETTING_SLOW_TRACKING_PER_DAB of type MyPaint.BrushSetting>, 19: <enum MYPAINT_BRUSH_SETTING_TRACKING_NOISE of type MyPaint.BrushSetting>, 20: <enum MYPAINT_BRUSH_SETTING_COLOR_H of type MyPaint.BrushSetting>, 21: <enum MYPAINT_BRUSH_SETTING_COLOR_S of type MyPaint.BrushSetting>, 22: <enum MYPAINT_BRUSH_SETTING_COLOR_V of type MyPaint.BrushSetting>, 23: <enum MYPAINT_BRUSH_SETTING_RESTORE_COLOR of type MyPaint.BrushSetting>, 24: <enum MYPAINT_BRUSH_SETTING_CHANGE_COLOR_H of type MyPaint.BrushSetting>, 25: <enum MYPAINT_BRUSH_SETTING_CHANGE_COLOR_L of type MyPaint.BrushSetting>, 26: <enum MYPAINT_BRUSH_SETTING_CHANGE_COLOR_HSL_S of type MyPaint.BrushSetting>, 27: <enum MYPAINT_BRUSH_SETTING_CHANGE_COLOR_V of type MyPaint.BrushSetting>, 28: <enum MYPAINT_BRUSH_SETTING_CHANGE_COLOR_HSV_S of type MyPaint.BrushSetting>, 29: <enum MYPAINT_BRUSH_SETTING_SMUDGE of type MyPaint.BrushSetting>, 30: <enum MYPAINT_BRUSH_SETTING_SMUDGE_LENGTH of type MyPaint.BrushSetting>, 31: <enum MYPAINT_BRUSH_SETTING_SMUDGE_RADIUS_LOG of type MyPaint.BrushSetting>, 32: <enum MYPAINT_BRUSH_SETTING_ERASER of type MyPaint.BrushSetting>, 33: <enum MYPAINT_BRUSH_SETTING_STROKE_THRESHOLD of type MyPaint.BrushSetting>, 34: <enum MYPAINT_BRUSH_SETTING_STROKE_DURATION_LOGARITHMIC of type MyPaint.BrushSetting>, 35: <enum MYPAINT_BRUSH_SETTING_STROKE_HOLDTIME of type MyPaint.BrushSetting>, 36: <enum MYPAINT_BRUSH_SETTING_CUSTOM_INPUT of type MyPaint.BrushSetting>, 37: <enum MYPAINT_BRUSH_SETTING_CUSTOM_INPUT_SLOWNESS of type MyPaint.BrushSetting>, 38: <enum MYPAINT_BRUSH_SETTING_ELLIPTICAL_DAB_RATIO of type MyPaint.BrushSetting>, 39: <enum MYPAINT_BRUSH_SETTING_ELLIPTICAL_DAB_ANGLE of type MyPaint.BrushSetting>, 40: <enum MYPAINT_BRUSH_SETTING_DIRECTION_FILTER of type MyPaint.BrushSetting>, 41: <enum MYPAINT_BRUSH_SETTING_LOCK_ALPHA of type MyPaint.BrushSetting>, 42: <enum MYPAINT_BRUSH_SETTING_COLORIZE of type MyPaint.BrushSetting>, 43: <enum MYPAINT_BRUSH_SETTING_SNAP_TO_PIXEL of type MyPaint.BrushSetting>, 44: <enum MYPAINT_BRUSH_SETTING_PRESSURE_GAIN_LOG of type MyPaint.BrushSetting>, 45: <enum MYPAINT_BRUSH_SETTING_GRIDMAP_SCALE of type MyPaint.BrushSetting>, 46: <enum MYPAINT_BRUSH_SETTING_GRIDMAP_SCALE_X of type MyPaint.BrushSetting>, 47: <enum MYPAINT_BRUSH_SETTING_GRIDMAP_SCALE_Y of type MyPaint.BrushSetting>, 48: <enum MYPAINT_BRUSH_SETTING_SMUDGE_LENGTH_LOG of type MyPaint.BrushSetting>, 49: <enum MYPAINT_BRUSH_SETTING_SMUDGE_BUCKET of type MyPaint.BrushSetting>, 50: <enum MYPAINT_BRUSH_SETTING_SMUDGE_TRANSPARENCY of type MyPaint.BrushSetting>, 51: <enum MYPAINT_BRUSH_SETTING_OFFSET_Y of type MyPaint.BrushSetting>, 52: <enum MYPAINT_BRUSH_SETTING_OFFSET_X of type MyPaint.BrushSetting>, 53: <enum MYPAINT_BRUSH_SETTING_OFFSET_ANGLE of type MyPaint.BrushSetting>, 54: <enum MYPAINT_BRUSH_SETTING_OFFSET_ANGLE_ASC of type MyPaint.BrushSetting>, 55: <enum MYPAINT_BRUSH_SETTING_OFFSET_ANGLE_VIEW of type MyPaint.BrushSetting>, 56: <enum MYPAINT_BRUSH_SETTING_OFFSET_ANGLE_2 of type MyPaint.BrushSetting>, 57: <enum MYPAINT_BRUSH_SETTING_OFFSET_ANGLE_2_ASC of type MyPaint.BrushSetting>, 58: <enum MYPAINT_BRUSH_SETTING_OFFSET_ANGLE_2_VIEW of type MyPaint.BrushSetting>, 59: <enum MYPAINT_BRUSH_SETTING_OFFSET_ANGLE_ADJ of type MyPaint.BrushSetting>, 60: <enum MYPAINT_BRUSH_SETTING_OFFSET_MULTIPLIER of type MyPaint.BrushSetting>, 61: <enum MYPAINT_BRUSH_SETTING_POSTERIZE of type MyPaint.BrushSetting>, 62: <enum MYPAINT_BRUSH_SETTING_POSTERIZE_NUM of type MyPaint.BrushSetting>, 63: <enum MYPAINT_BRUSH_SETTING_PAINT_MODE of type MyPaint.BrushSetting>, 64: <enum MYPAINT_BRUSH_SETTINGS_COUNT of type MyPaint.BrushSetting>}, '__info__': gi.EnumInfo(BrushSetting), 'SETTING_OPAQUE': <enum MYPAINT_BRUSH_SETTING_OPAQUE of type MyPaint.BrushSetting>, 'SETTING_OPAQUE_MULTIPLY': <enum MYPAINT_BRUSH_SETTING_OPAQUE_MULTIPLY of type MyPaint.BrushSetting>, 'SETTING_OPAQUE_LINEARIZE': <enum MYPAINT_BRUSH_SETTING_OPAQUE_LINEARIZE of type MyPaint.BrushSetting>, 'SETTING_RADIUS_LOGARITHMIC': <enum MYPAINT_BRUSH_SETTING_RADIUS_LOGARITHMIC of type MyPaint.BrushSetting>, 'SETTING_HARDNESS': <enum MYPAINT_BRUSH_SETTING_HARDNESS of type MyPaint.BrushSetting>, 'SETTING_ANTI_ALIASING': <enum MYPAINT_BRUSH_SETTING_ANTI_ALIASING of type MyPaint.BrushSetting>, 'SETTING_DABS_PER_BASIC_RADIUS': <enum MYPAINT_BRUSH_SETTING_DABS_PER_BASIC_RADIUS of type MyPaint.BrushSetting>, 'SETTING_DABS_PER_ACTUAL_RADIUS': <enum MYPAINT_BRUSH_SETTING_DABS_PER_ACTUAL_RADIUS of type MyPaint.BrushSetting>, 'SETTING_DABS_PER_SECOND': <enum MYPAINT_BRUSH_SETTING_DABS_PER_SECOND of type MyPaint.BrushSetting>, 'SETTING_RADIUS_BY_RANDOM': <enum MYPAINT_BRUSH_SETTING_RADIUS_BY_RANDOM of type MyPaint.BrushSetting>, 'SETTING_SPEED1_SLOWNESS': <enum MYPAINT_BRUSH_SETTING_SPEED1_SLOWNESS of type MyPaint.BrushSetting>, 'SETTING_SPEED2_SLOWNESS': <enum MYPAINT_BRUSH_SETTING_SPEED2_SLOWNESS of type MyPaint.BrushSetting>, 'SETTING_SPEED1_GAMMA': <enum MYPAINT_BRUSH_SETTING_SPEED1_GAMMA of type MyPaint.BrushSetting>, 'SETTING_SPEED2_GAMMA': <enum MYPAINT_BRUSH_SETTING_SPEED2_GAMMA of type MyPaint.BrushSetting>, 'SETTING_OFFSET_BY_RANDOM': <enum MYPAINT_BRUSH_SETTING_OFFSET_BY_RANDOM of type MyPaint.BrushSetting>, 'SETTING_OFFSET_BY_SPEED': <enum MYPAINT_BRUSH_SETTING_OFFSET_BY_SPEED of type MyPaint.BrushSetting>, 'SETTING_OFFSET_BY_SPEED_SLOWNESS': <enum MYPAINT_BRUSH_SETTING_OFFSET_BY_SPEED_SLOWNESS of type MyPaint.BrushSetting>, 'SETTING_SLOW_TRACKING': <enum MYPAINT_BRUSH_SETTING_SLOW_TRACKING of type MyPaint.BrushSetting>, 'SETTING_SLOW_TRACKING_PER_DAB': <enum MYPAINT_BRUSH_SETTING_SLOW_TRACKING_PER_DAB of type MyPaint.BrushSetting>, 'SETTING_TRACKING_NOISE': <enum MYPAINT_BRUSH_SETTING_TRACKING_NOISE of type MyPaint.BrushSetting>, 'SETTING_COLOR_H': <enum MYPAINT_BRUSH_SETTING_COLOR_H of type MyPaint.BrushSetting>, 'SETTING_COLOR_S': <enum MYPAINT_BRUSH_SETTING_COLOR_S of type MyPaint.BrushSetting>, 'SETTING_COLOR_V': <enum MYPAINT_BRUSH_SETTING_COLOR_V of type MyPaint.BrushSetting>, 'SETTING_RESTORE_COLOR': <enum MYPAINT_BRUSH_SETTING_RESTORE_COLOR of type MyPaint.BrushSetting>, 'SETTING_CHANGE_COLOR_H': <enum MYPAINT_BRUSH_SETTING_CHANGE_COLOR_H of type MyPaint.BrushSetting>, 'SETTING_CHANGE_COLOR_L': <enum MYPAINT_BRUSH_SETTING_CHANGE_COLOR_L of type MyPaint.BrushSetting>, 'SETTING_CHANGE_COLOR_HSL_S': <enum MYPAINT_BRUSH_SETTING_CHANGE_COLOR_HSL_S of type MyPaint.BrushSetting>, 'SETTING_CHANGE_COLOR_V': <enum MYPAINT_BRUSH_SETTING_CHANGE_COLOR_V of type MyPaint.BrushSetting>, 'SETTING_CHANGE_COLOR_HSV_S': <enum MYPAINT_BRUSH_SETTING_CHANGE_COLOR_HSV_S of type MyPaint.BrushSetting>, 'SETTING_SMUDGE': <enum MYPAINT_BRUSH_SETTING_SMUDGE of type MyPaint.BrushSetting>, 'SETTING_SMUDGE_LENGTH': <enum MYPAINT_BRUSH_SETTING_SMUDGE_LENGTH of type MyPaint.BrushSetting>, 'SETTING_SMUDGE_RADIUS_LOG': <enum MYPAINT_BRUSH_SETTING_SMUDGE_RADIUS_LOG of type MyPaint.BrushSetting>, 'SETTING_ERASER': <enum MYPAINT_BRUSH_SETTING_ERASER of type MyPaint.BrushSetting>, 'SETTING_STROKE_THRESHOLD': <enum MYPAINT_BRUSH_SETTING_STROKE_THRESHOLD of type MyPaint.BrushSetting>, 'SETTING_STROKE_DURATION_LOGARITHMIC': <enum MYPAINT_BRUSH_SETTING_STROKE_DURATION_LOGARITHMIC of type MyPaint.BrushSetting>, 'SETTING_STROKE_HOLDTIME': <enum MYPAINT_BRUSH_SETTING_STROKE_HOLDTIME of type MyPaint.BrushSetting>, 'SETTING_CUSTOM_INPUT': <enum MYPAINT_BRUSH_SETTING_CUSTOM_INPUT of type MyPaint.BrushSetting>, 'SETTING_CUSTOM_INPUT_SLOWNESS': <enum MYPAINT_BRUSH_SETTING_CUSTOM_INPUT_SLOWNESS of type MyPaint.BrushSetting>, 'SETTING_ELLIPTICAL_DAB_RATIO': <enum MYPAINT_BRUSH_SETTING_ELLIPTICAL_DAB_RATIO of type MyPaint.BrushSetting>, 'SETTING_ELLIPTICAL_DAB_ANGLE': <enum MYPAINT_BRUSH_SETTING_ELLIPTICAL_DAB_ANGLE of type MyPaint.BrushSetting>, 'SETTING_DIRECTION_FILTER': <enum MYPAINT_BRUSH_SETTING_DIRECTION_FILTER of type MyPaint.BrushSetting>, 'SETTING_LOCK_ALPHA': <enum MYPAINT_BRUSH_SETTING_LOCK_ALPHA of type MyPaint.BrushSetting>, 'SETTING_COLORIZE': <enum MYPAINT_BRUSH_SETTING_COLORIZE of type MyPaint.BrushSetting>, 'SETTING_SNAP_TO_PIXEL': <enum MYPAINT_BRUSH_SETTING_SNAP_TO_PIXEL of type MyPaint.BrushSetting>, 'SETTING_PRESSURE_GAIN_LOG': <enum MYPAINT_BRUSH_SETTING_PRESSURE_GAIN_LOG of type MyPaint.BrushSetting>, 'SETTING_GRIDMAP_SCALE': <enum MYPAINT_BRUSH_SETTING_GRIDMAP_SCALE of type MyPaint.BrushSetting>, 'SETTING_GRIDMAP_SCALE_X': <enum MYPAINT_BRUSH_SETTING_GRIDMAP_SCALE_X of type MyPaint.BrushSetting>, 'SETTING_GRIDMAP_SCALE_Y': <enum MYPAINT_BRUSH_SETTING_GRIDMAP_SCALE_Y of type MyPaint.BrushSetting>, 'SETTING_SMUDGE_LENGTH_LOG': <enum MYPAINT_BRUSH_SETTING_SMUDGE_LENGTH_LOG of type MyPaint.BrushSetting>, 'SETTING_SMUDGE_BUCKET': <enum MYPAINT_BRUSH_SETTING_SMUDGE_BUCKET of type MyPaint.BrushSetting>, 'SETTING_SMUDGE_TRANSPARENCY': <enum MYPAINT_BRUSH_SETTING_SMUDGE_TRANSPARENCY of type MyPaint.BrushSetting>, 'SETTING_OFFSET_Y': <enum MYPAINT_BRUSH_SETTING_OFFSET_Y of type MyPaint.BrushSetting>, 'SETTING_OFFSET_X': <enum MYPAINT_BRUSH_SETTING_OFFSET_X of type MyPaint.BrushSetting>, 'SETTING_OFFSET_ANGLE': <enum MYPAINT_BRUSH_SETTING_OFFSET_ANGLE of type MyPaint.BrushSetting>, 'SETTING_OFFSET_ANGLE_ASC': <enum MYPAINT_BRUSH_SETTING_OFFSET_ANGLE_ASC of type MyPaint.BrushSetting>, 'SETTING_OFFSET_ANGLE_VIEW': <enum MYPAINT_BRUSH_SETTING_OFFSET_ANGLE_VIEW of type MyPaint.BrushSetting>, 'SETTING_OFFSET_ANGLE_2': <enum MYPAINT_BRUSH_SETTING_OFFSET_ANGLE_2 of type MyPaint.BrushSetting>, 'SETTING_OFFSET_ANGLE_2_ASC': <enum MYPAINT_BRUSH_SETTING_OFFSET_ANGLE_2_ASC of type MyPaint.BrushSetting>, 'SETTING_OFFSET_ANGLE_2_VIEW': <enum MYPAINT_BRUSH_SETTING_OFFSET_ANGLE_2_VIEW of type MyPaint.BrushSetting>, 'SETTING_OFFSET_ANGLE_ADJ': <enum MYPAINT_BRUSH_SETTING_OFFSET_ANGLE_ADJ of type MyPaint.BrushSetting>, 'SETTING_OFFSET_MULTIPLIER': <enum MYPAINT_BRUSH_SETTING_OFFSET_MULTIPLIER of type MyPaint.BrushSetting>, 'SETTING_POSTERIZE': <enum MYPAINT_BRUSH_SETTING_POSTERIZE of type MyPaint.BrushSetting>, 'SETTING_POSTERIZE_NUM': <enum MYPAINT_BRUSH_SETTING_POSTERIZE_NUM of type MyPaint.BrushSetting>, 'SETTING_PAINT_MODE': <enum MYPAINT_BRUSH_SETTING_PAINT_MODE of type MyPaint.BrushSetting>, 'SETTINGS_COUNT': <enum MYPAINT_BRUSH_SETTINGS_COUNT of type MyPaint.BrushSetting>})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 11,
        12: 12,
        13: 13,
        14: 14,
        15: 15,
        16: 16,
        17: 17,
        18: 18,
        19: 19,
        20: 20,
        21: 21,
        22: 22,
        23: 23,
        24: 24,
        25: 25,
        26: 26,
        27: 27,
        28: 28,
        29: 29,
        30: 30,
        31: 31,
        32: 32,
        33: 33,
        34: 34,
        35: 35,
        36: 36,
        37: 37,
        38: 38,
        39: 39,
        40: 40,
        41: 41,
        42: 42,
        43: 43,
        44: 44,
        45: 45,
        46: 46,
        47: 47,
        48: 48,
        49: 49,
        50: 50,
        51: 51,
        52: 52,
        53: 53,
        54: 54,
        55: 55,
        56: 56,
        57: 57,
        58: 58,
        59: 59,
        60: 60,
        61: 61,
        62: 62,
        63: 63,
        64: 64,
    }
    __gtype__ = None # (!) real value is '<GType PyMyPaintBrushSetting (3895786432)>'
    __info__ = gi.EnumInfo(BrushSetting)


class BrushSettingInfo(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        BrushSettingInfo()
    """
    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_tooltip(self): # real signature unknown; restored from __doc__
        """ get_tooltip(self) -> str """
        return ""

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

    cname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    constant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    def_ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    min = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tooltip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(BrushSettingInfo), '__module__': 'gi.repository.MyPaint', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'BrushSettingInfo' objects>, '__weakref__': <attribute '__weakref__' of 'BrushSettingInfo' objects>, '__doc__': None, 'cname': <property object at 0x00000230e8bc8b30>, 'name': <property object at 0x00000230e8bc8c20>, 'constant': <property object at 0x00000230e8bc8d10>, 'min': <property object at 0x00000230e8bc8e00>, 'def_': <property object at 0x00000230e8bc8ef0>, 'max': <property object at 0x00000230e8bc8fe0>, 'tooltip': <property object at 0x00000230e8bc90d0>, 'get_name': gi.FunctionInfo(get_name, bound=None), 'get_tooltip': gi.FunctionInfo(get_tooltip, bound=None)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(BrushSettingInfo)


class BrushState(__gobject.GEnum):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_count(self): # real signature unknown; restored from __doc__
        """
        Number of ones in the binary representation of the absolute value of self.
        
        Also known as the population count.
        
        >>> bin(13)
        '0b1101'
        >>> (13).bit_count()
        3
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.  Default is to use 'big'.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.  Default
            is length 1.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.  Default is to use 'big'.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    STATES_COUNT = 44
    STATE_ACTUAL_ELLIPTICAL_DAB_ANGLE = 25
    STATE_ACTUAL_ELLIPTICAL_DAB_RATIO = 24
    STATE_ACTUAL_RADIUS = 4
    STATE_ACTUAL_X = 14
    STATE_ACTUAL_Y = 15
    STATE_ASCENSION = 29
    STATE_ATTACK_ANGLE = 34
    STATE_BARREL_ROTATION = 43
    STATE_CUSTOM_INPUT = 22
    STATE_DABS_PER_ACTUAL_RADIUS = 41
    STATE_DABS_PER_BASIC_RADIUS = 40
    STATE_DABS_PER_SECOND = 42
    STATE_DECLINATION = 28
    STATE_DECLINATIONX = 38
    STATE_DECLINATIONY = 39
    STATE_DIRECTION_ANGLE_DX = 32
    STATE_DIRECTION_ANGLE_DY = 33
    STATE_DIRECTION_DX = 26
    STATE_DIRECTION_DY = 27
    STATE_FLIP = 35
    STATE_GRIDMAP_X = 36
    STATE_GRIDMAP_Y = 37
    STATE_LAST_GETCOLOR_A = 12
    STATE_LAST_GETCOLOR_B = 11
    STATE_LAST_GETCOLOR_G = 10
    STATE_LAST_GETCOLOR_R = 9
    STATE_LAST_GETCOLOR_RECENTNESS = 13
    STATE_NORM_DX_SLOW = 16
    STATE_NORM_DY_SLOW = 17
    STATE_NORM_SPEED1_SLOW = 18
    STATE_NORM_SPEED2_SLOW = 19
    STATE_PARTIAL_DABS = 3
    STATE_PRESSURE = 2
    STATE_RNG_SEED = 23
    STATE_SMUDGE_A = 8
    STATE_SMUDGE_BA = 7
    STATE_SMUDGE_GA = 6
    STATE_SMUDGE_RA = 5
    STATE_STROKE = 20
    STATE_STROKE_STARTED = 21
    STATE_VIEWROTATION = 31
    STATE_VIEWZOOM = 30
    STATE_X = 0
    STATE_Y = 1
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.MyPaint', '__dict__': <attribute '__dict__' of 'BrushState' objects>, '__doc__': None, '__gtype__': <GType PyMyPaintBrushState (3895786656)>, '__enum_values__': {0: <enum MYPAINT_BRUSH_STATE_X of type MyPaint.BrushState>, 1: <enum MYPAINT_BRUSH_STATE_Y of type MyPaint.BrushState>, 2: <enum MYPAINT_BRUSH_STATE_PRESSURE of type MyPaint.BrushState>, 3: <enum MYPAINT_BRUSH_STATE_PARTIAL_DABS of type MyPaint.BrushState>, 4: <enum MYPAINT_BRUSH_STATE_ACTUAL_RADIUS of type MyPaint.BrushState>, 5: <enum MYPAINT_BRUSH_STATE_SMUDGE_RA of type MyPaint.BrushState>, 6: <enum MYPAINT_BRUSH_STATE_SMUDGE_GA of type MyPaint.BrushState>, 7: <enum MYPAINT_BRUSH_STATE_SMUDGE_BA of type MyPaint.BrushState>, 8: <enum MYPAINT_BRUSH_STATE_SMUDGE_A of type MyPaint.BrushState>, 9: <enum MYPAINT_BRUSH_STATE_LAST_GETCOLOR_R of type MyPaint.BrushState>, 10: <enum MYPAINT_BRUSH_STATE_LAST_GETCOLOR_G of type MyPaint.BrushState>, 11: <enum MYPAINT_BRUSH_STATE_LAST_GETCOLOR_B of type MyPaint.BrushState>, 12: <enum MYPAINT_BRUSH_STATE_LAST_GETCOLOR_A of type MyPaint.BrushState>, 13: <enum MYPAINT_BRUSH_STATE_LAST_GETCOLOR_RECENTNESS of type MyPaint.BrushState>, 14: <enum MYPAINT_BRUSH_STATE_ACTUAL_X of type MyPaint.BrushState>, 15: <enum MYPAINT_BRUSH_STATE_ACTUAL_Y of type MyPaint.BrushState>, 16: <enum MYPAINT_BRUSH_STATE_NORM_DX_SLOW of type MyPaint.BrushState>, 17: <enum MYPAINT_BRUSH_STATE_NORM_DY_SLOW of type MyPaint.BrushState>, 18: <enum MYPAINT_BRUSH_STATE_NORM_SPEED1_SLOW of type MyPaint.BrushState>, 19: <enum MYPAINT_BRUSH_STATE_NORM_SPEED2_SLOW of type MyPaint.BrushState>, 20: <enum MYPAINT_BRUSH_STATE_STROKE of type MyPaint.BrushState>, 21: <enum MYPAINT_BRUSH_STATE_STROKE_STARTED of type MyPaint.BrushState>, 22: <enum MYPAINT_BRUSH_STATE_CUSTOM_INPUT of type MyPaint.BrushState>, 23: <enum MYPAINT_BRUSH_STATE_RNG_SEED of type MyPaint.BrushState>, 24: <enum MYPAINT_BRUSH_STATE_ACTUAL_ELLIPTICAL_DAB_RATIO of type MyPaint.BrushState>, 25: <enum MYPAINT_BRUSH_STATE_ACTUAL_ELLIPTICAL_DAB_ANGLE of type MyPaint.BrushState>, 26: <enum MYPAINT_BRUSH_STATE_DIRECTION_DX of type MyPaint.BrushState>, 27: <enum MYPAINT_BRUSH_STATE_DIRECTION_DY of type MyPaint.BrushState>, 28: <enum MYPAINT_BRUSH_STATE_DECLINATION of type MyPaint.BrushState>, 29: <enum MYPAINT_BRUSH_STATE_ASCENSION of type MyPaint.BrushState>, 30: <enum MYPAINT_BRUSH_STATE_VIEWZOOM of type MyPaint.BrushState>, 31: <enum MYPAINT_BRUSH_STATE_VIEWROTATION of type MyPaint.BrushState>, 32: <enum MYPAINT_BRUSH_STATE_DIRECTION_ANGLE_DX of type MyPaint.BrushState>, 33: <enum MYPAINT_BRUSH_STATE_DIRECTION_ANGLE_DY of type MyPaint.BrushState>, 34: <enum MYPAINT_BRUSH_STATE_ATTACK_ANGLE of type MyPaint.BrushState>, 35: <enum MYPAINT_BRUSH_STATE_FLIP of type MyPaint.BrushState>, 36: <enum MYPAINT_BRUSH_STATE_GRIDMAP_X of type MyPaint.BrushState>, 37: <enum MYPAINT_BRUSH_STATE_GRIDMAP_Y of type MyPaint.BrushState>, 38: <enum MYPAINT_BRUSH_STATE_DECLINATIONX of type MyPaint.BrushState>, 39: <enum MYPAINT_BRUSH_STATE_DECLINATIONY of type MyPaint.BrushState>, 40: <enum MYPAINT_BRUSH_STATE_DABS_PER_BASIC_RADIUS of type MyPaint.BrushState>, 41: <enum MYPAINT_BRUSH_STATE_DABS_PER_ACTUAL_RADIUS of type MyPaint.BrushState>, 42: <enum MYPAINT_BRUSH_STATE_DABS_PER_SECOND of type MyPaint.BrushState>, 43: <enum MYPAINT_BRUSH_STATE_BARREL_ROTATION of type MyPaint.BrushState>, 44: <enum MYPAINT_BRUSH_STATES_COUNT of type MyPaint.BrushState>}, '__info__': gi.EnumInfo(BrushState), 'STATE_X': <enum MYPAINT_BRUSH_STATE_X of type MyPaint.BrushState>, 'STATE_Y': <enum MYPAINT_BRUSH_STATE_Y of type MyPaint.BrushState>, 'STATE_PRESSURE': <enum MYPAINT_BRUSH_STATE_PRESSURE of type MyPaint.BrushState>, 'STATE_PARTIAL_DABS': <enum MYPAINT_BRUSH_STATE_PARTIAL_DABS of type MyPaint.BrushState>, 'STATE_ACTUAL_RADIUS': <enum MYPAINT_BRUSH_STATE_ACTUAL_RADIUS of type MyPaint.BrushState>, 'STATE_SMUDGE_RA': <enum MYPAINT_BRUSH_STATE_SMUDGE_RA of type MyPaint.BrushState>, 'STATE_SMUDGE_GA': <enum MYPAINT_BRUSH_STATE_SMUDGE_GA of type MyPaint.BrushState>, 'STATE_SMUDGE_BA': <enum MYPAINT_BRUSH_STATE_SMUDGE_BA of type MyPaint.BrushState>, 'STATE_SMUDGE_A': <enum MYPAINT_BRUSH_STATE_SMUDGE_A of type MyPaint.BrushState>, 'STATE_LAST_GETCOLOR_R': <enum MYPAINT_BRUSH_STATE_LAST_GETCOLOR_R of type MyPaint.BrushState>, 'STATE_LAST_GETCOLOR_G': <enum MYPAINT_BRUSH_STATE_LAST_GETCOLOR_G of type MyPaint.BrushState>, 'STATE_LAST_GETCOLOR_B': <enum MYPAINT_BRUSH_STATE_LAST_GETCOLOR_B of type MyPaint.BrushState>, 'STATE_LAST_GETCOLOR_A': <enum MYPAINT_BRUSH_STATE_LAST_GETCOLOR_A of type MyPaint.BrushState>, 'STATE_LAST_GETCOLOR_RECENTNESS': <enum MYPAINT_BRUSH_STATE_LAST_GETCOLOR_RECENTNESS of type MyPaint.BrushState>, 'STATE_ACTUAL_X': <enum MYPAINT_BRUSH_STATE_ACTUAL_X of type MyPaint.BrushState>, 'STATE_ACTUAL_Y': <enum MYPAINT_BRUSH_STATE_ACTUAL_Y of type MyPaint.BrushState>, 'STATE_NORM_DX_SLOW': <enum MYPAINT_BRUSH_STATE_NORM_DX_SLOW of type MyPaint.BrushState>, 'STATE_NORM_DY_SLOW': <enum MYPAINT_BRUSH_STATE_NORM_DY_SLOW of type MyPaint.BrushState>, 'STATE_NORM_SPEED1_SLOW': <enum MYPAINT_BRUSH_STATE_NORM_SPEED1_SLOW of type MyPaint.BrushState>, 'STATE_NORM_SPEED2_SLOW': <enum MYPAINT_BRUSH_STATE_NORM_SPEED2_SLOW of type MyPaint.BrushState>, 'STATE_STROKE': <enum MYPAINT_BRUSH_STATE_STROKE of type MyPaint.BrushState>, 'STATE_STROKE_STARTED': <enum MYPAINT_BRUSH_STATE_STROKE_STARTED of type MyPaint.BrushState>, 'STATE_CUSTOM_INPUT': <enum MYPAINT_BRUSH_STATE_CUSTOM_INPUT of type MyPaint.BrushState>, 'STATE_RNG_SEED': <enum MYPAINT_BRUSH_STATE_RNG_SEED of type MyPaint.BrushState>, 'STATE_ACTUAL_ELLIPTICAL_DAB_RATIO': <enum MYPAINT_BRUSH_STATE_ACTUAL_ELLIPTICAL_DAB_RATIO of type MyPaint.BrushState>, 'STATE_ACTUAL_ELLIPTICAL_DAB_ANGLE': <enum MYPAINT_BRUSH_STATE_ACTUAL_ELLIPTICAL_DAB_ANGLE of type MyPaint.BrushState>, 'STATE_DIRECTION_DX': <enum MYPAINT_BRUSH_STATE_DIRECTION_DX of type MyPaint.BrushState>, 'STATE_DIRECTION_DY': <enum MYPAINT_BRUSH_STATE_DIRECTION_DY of type MyPaint.BrushState>, 'STATE_DECLINATION': <enum MYPAINT_BRUSH_STATE_DECLINATION of type MyPaint.BrushState>, 'STATE_ASCENSION': <enum MYPAINT_BRUSH_STATE_ASCENSION of type MyPaint.BrushState>, 'STATE_VIEWZOOM': <enum MYPAINT_BRUSH_STATE_VIEWZOOM of type MyPaint.BrushState>, 'STATE_VIEWROTATION': <enum MYPAINT_BRUSH_STATE_VIEWROTATION of type MyPaint.BrushState>, 'STATE_DIRECTION_ANGLE_DX': <enum MYPAINT_BRUSH_STATE_DIRECTION_ANGLE_DX of type MyPaint.BrushState>, 'STATE_DIRECTION_ANGLE_DY': <enum MYPAINT_BRUSH_STATE_DIRECTION_ANGLE_DY of type MyPaint.BrushState>, 'STATE_ATTACK_ANGLE': <enum MYPAINT_BRUSH_STATE_ATTACK_ANGLE of type MyPaint.BrushState>, 'STATE_FLIP': <enum MYPAINT_BRUSH_STATE_FLIP of type MyPaint.BrushState>, 'STATE_GRIDMAP_X': <enum MYPAINT_BRUSH_STATE_GRIDMAP_X of type MyPaint.BrushState>, 'STATE_GRIDMAP_Y': <enum MYPAINT_BRUSH_STATE_GRIDMAP_Y of type MyPaint.BrushState>, 'STATE_DECLINATIONX': <enum MYPAINT_BRUSH_STATE_DECLINATIONX of type MyPaint.BrushState>, 'STATE_DECLINATIONY': <enum MYPAINT_BRUSH_STATE_DECLINATIONY of type MyPaint.BrushState>, 'STATE_DABS_PER_BASIC_RADIUS': <enum MYPAINT_BRUSH_STATE_DABS_PER_BASIC_RADIUS of type MyPaint.BrushState>, 'STATE_DABS_PER_ACTUAL_RADIUS': <enum MYPAINT_BRUSH_STATE_DABS_PER_ACTUAL_RADIUS of type MyPaint.BrushState>, 'STATE_DABS_PER_SECOND': <enum MYPAINT_BRUSH_STATE_DABS_PER_SECOND of type MyPaint.BrushState>, 'STATE_BARREL_ROTATION': <enum MYPAINT_BRUSH_STATE_BARREL_ROTATION of type MyPaint.BrushState>, 'STATES_COUNT': <enum MYPAINT_BRUSH_STATES_COUNT of type MyPaint.BrushState>})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 11,
        12: 12,
        13: 13,
        14: 14,
        15: 15,
        16: 16,
        17: 17,
        18: 18,
        19: 19,
        20: 20,
        21: 21,
        22: 22,
        23: 23,
        24: 24,
        25: 25,
        26: 26,
        27: 27,
        28: 28,
        29: 29,
        30: 30,
        31: 31,
        32: 32,
        33: 33,
        34: 34,
        35: 35,
        36: 36,
        37: 37,
        38: 38,
        39: 39,
        40: 40,
        41: 41,
        42: 42,
        43: 43,
        44: 44,
    }
    __gtype__ = None # (!) real value is '<GType PyMyPaintBrushState (3895786656)>'
    __info__ = gi.EnumInfo(BrushState)


class FixedTiledSurface(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(width:int, height:int) -> MyPaint.FixedTiledSurface
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def get_height(self): # real signature unknown; restored from __doc__
        """ get_height(self) -> int """
        return 0

    def get_width(self): # real signature unknown; restored from __doc__
        """ get_width(self) -> int """
        return 0

    def interface(self): # real signature unknown; restored from __doc__
        """ interface(self) -> MyPaint.Surface """
        pass

    def new(self, width, height): # real signature unknown; restored from __doc__
        """ new(width:int, height:int) -> MyPaint.FixedTiledSurface """
        pass

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
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

    def __init__(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ new(width:int, height:int) -> MyPaint.FixedTiledSurface """
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(FixedTiledSurface), '__module__': 'gi.repository.MyPaint', '__gtype__': <GType MyPaintFixedTiledSurface (3895791248)>, '__dict__': <attribute '__dict__' of 'FixedTiledSurface' objects>, '__weakref__': <attribute '__weakref__' of 'FixedTiledSurface' objects>, '__doc__': None, 'new': gi.FunctionInfo(new, bound=None), 'get_height': gi.FunctionInfo(get_height, bound=None), 'get_width': gi.FunctionInfo(get_width, bound=None), 'interface': gi.FunctionInfo(interface, bound=None), '__new__': <staticmethod(gi.FunctionInfo(new, bound=None))>, '__init__': <function nothing at 0x00000230e89d8680>})"
    __gtype__ = None # (!) real value is '<GType MyPaintFixedTiledSurface (3895791248)>'
    __info__ = StructInfo(FixedTiledSurface)


class Rectangle(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Rectangle()
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> MyPaint.Rectangle """
        pass

    def expand_to_include_point(self, x, y): # real signature unknown; restored from __doc__
        """ expand_to_include_point(self, x:int, y:int) """
        pass

    def expand_to_include_rect(self, other): # real signature unknown; restored from __doc__
        """ expand_to_include_rect(self, other:MyPaint.Rectangle) """
        pass

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
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

    height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Rectangle), '__module__': 'gi.repository.MyPaint', '__gtype__': <GType MyPaintRectangle (3895791360)>, '__dict__': <attribute '__dict__' of 'Rectangle' objects>, '__weakref__': <attribute '__weakref__' of 'Rectangle' objects>, '__doc__': None, 'x': <property object at 0x00000230e8bca9d0>, 'y': <property object at 0x00000230e8bcaac0>, 'width': <property object at 0x00000230e8bcabb0>, 'height': <property object at 0x00000230e8bcaca0>, 'copy': gi.FunctionInfo(copy, bound=None), 'expand_to_include_point': gi.FunctionInfo(expand_to_include_point, bound=None), 'expand_to_include_rect': gi.FunctionInfo(expand_to_include_rect, bound=None)})"
    __gtype__ = None # (!) real value is '<GType MyPaintRectangle (3895791360)>'
    __info__ = StructInfo(Rectangle)


class Rectangles(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        Rectangles()
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

    num_rectangles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rectangles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Rectangles), '__module__': 'gi.repository.MyPaint', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'Rectangles' objects>, '__weakref__': <attribute '__weakref__' of 'Rectangles' objects>, '__doc__': None, 'num_rectangles': <property object at 0x00000230e8bcaed0>, 'rectangles': <property object at 0x00000230e8bcafc0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(Rectangles)


class Surface(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Surface()
    """
    def begin_atomic(self): # real signature unknown; restored from __doc__
        """ begin_atomic(self) """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def draw_dab(self, x, y, radius, color_r, color_g, color_b, opaque, hardness, alpha_eraser, aspect_ratio, angle, lock_alpha, colorize): # real signature unknown; restored from __doc__
        """ draw_dab(self, x:float, y:float, radius:float, color_r:float, color_g:float, color_b:float, opaque:float, hardness:float, alpha_eraser:float, aspect_ratio:float, angle:float, lock_alpha:float, colorize:float) -> int """
        return 0

    def end_atomic(self): # real signature unknown; restored from __doc__
        """ end_atomic(self) -> roi:MyPaint.Rectangle """
        pass

    def get_alpha(self, x, y, radius): # real signature unknown; restored from __doc__
        """ get_alpha(self, x:float, y:float, radius:float) -> float """
        return 0.0

    def get_color(self, x, y, radius, color_r, color_g, color_b, color_a): # real signature unknown; restored from __doc__
        """ get_color(self, x:float, y:float, radius:float, color_r:float, color_g:float, color_b:float, color_a:float) """
        pass

    def save_png(self, path, x, y, width, height): # real signature unknown; restored from __doc__
        """ save_png(self, path:str, x:int, y:int, width:int, height:int) """
        pass

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
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

    destroy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    refcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Surface), '__module__': 'gi.repository.MyPaint', '__gtype__': <GType MyPaintSurface (3895790688)>, '__dict__': <attribute '__dict__' of 'Surface' objects>, '__weakref__': <attribute '__weakref__' of 'Surface' objects>, '__doc__': None, 'draw_dab': gi.FunctionInfo(draw_dab, bound=None), 'get_color': gi.FunctionInfo(get_color, bound=None), 'begin_atomic': gi.FunctionInfo(begin_atomic, bound=None), 'end_atomic': gi.FunctionInfo(end_atomic, bound=None), 'destroy': <property object at 0x00000230e8bcb510>, 'save_png': gi.FunctionInfo(save_png, bound=None), 'refcount': <property object at 0x00000230e8bcb6f0>, 'get_alpha': gi.FunctionInfo(get_alpha, bound=None)})"
    __gtype__ = None # (!) real value is '<GType MyPaintSurface (3895790688)>'
    __info__ = StructInfo(Surface)


class TiledSurface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        TiledSurface()
    """
    def get_alpha(self, x, y, radius): # real signature unknown; restored from __doc__
        """ get_alpha(self, x:float, y:float, radius:float) -> float """
        return 0.0

    def set_symmetry_state(self, active, center_x): # real signature unknown; restored from __doc__
        """ set_symmetry_state(self, active:bool, center_x:float) """
        pass

    def tile_request_end(self, request): # real signature unknown; restored from __doc__
        """ tile_request_end(self, request:MyPaint.TileRequest) """
        pass

    def tile_request_start(self, request): # real signature unknown; restored from __doc__
        """ tile_request_start(self, request:MyPaint.TileRequest) """
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

    dirty_bbox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    operation_queue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    surface_center_x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    surface_do_symmetry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    threadsafe_tile_requests = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tile_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TiledSurface), '__module__': 'gi.repository.MyPaint', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'TiledSurface' objects>, '__weakref__': <attribute '__weakref__' of 'TiledSurface' objects>, '__doc__': None, 'parent': <property object at 0x00000230e8bcbb00>, 'tile_request_start': gi.FunctionInfo(tile_request_start, bound=None), 'tile_request_end': gi.FunctionInfo(tile_request_end, bound=None), 'surface_do_symmetry': <property object at 0x00000230e8bcbec0>, 'surface_center_x': <property object at 0x00000230e8bcc040>, 'operation_queue': <property object at 0x00000230e8bcc130>, 'dirty_bbox': <property object at 0x00000230e8bcc220>, 'threadsafe_tile_requests': <property object at 0x00000230e8bcc360>, 'tile_size': <property object at 0x00000230e8bcc450>, 'get_alpha': gi.FunctionInfo(get_alpha, bound=None), 'set_symmetry_state': gi.FunctionInfo(set_symmetry_state, bound=None)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(TiledSurface)


class TileRequest(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        TileRequest()
    """
    def init(self, level, tx, ty, readonly): # real signature unknown; restored from __doc__
        """ init(self, level:int, tx:int, ty:int, readonly:bool) """
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

    buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mipmap_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    readonly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thread_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TileRequest), '__module__': 'gi.repository.MyPaint', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'TileRequest' objects>, '__weakref__': <attribute '__weakref__' of 'TileRequest' objects>, '__doc__': None, 'tx': <property object at 0x00000230e8bcb1f0>, 'ty': <property object at 0x00000230e8bcb3d0>, 'readonly': <property object at 0x00000230e8bcb100>, 'buffer': <property object at 0x00000230e8bcb2e0>, 'context': <property object at 0x00000230e8bcb790>, 'thread_id': <property object at 0x00000230e8bcb880>, 'mipmap_level': <property object at 0x00000230e8bcb970>, 'init': gi.FunctionInfo(init, bound=None)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(TileRequest)


class __class__(object):
    """
    An object which wraps an introspection typelib.
    
        This wrapping creates a python module like representation of the typelib
        using gi repository as a foundation. Accessing attributes of the module
        will dynamically pull them in and create wrappers for the members.
        These members are then cached on this introspection module.
    """
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self): # reliably restored by inspect
        # no doc
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

    def __getattr__(self, name): # reliably restored by inspect
        # no doc
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

    def __init__(self, namespace, version=None): # reliably restored by inspect
        """ Might raise gi._gi.RepositoryError """
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

    def __repr__(self): # reliably restored by inspect
        # no doc
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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.module', '__doc__': 'An object which wraps an introspection typelib.\\n\\n    This wrapping creates a python module like representation of the typelib\\n    using gi repository as a foundation. Accessing attributes of the module\\n    will dynamically pull them in and create wrappers for the members.\\n    These members are then cached on this introspection module.\\n    ', '__init__': <function IntrospectionModule.__init__ at 0x00000230e89d8720>, '__getattr__': <function IntrospectionModule.__getattr__ at 0x00000230e89d8900>, '__repr__': <function IntrospectionModule.__repr__ at 0x00000230e89d89a0>, '__dir__': <function IntrospectionModule.__dir__ at 0x00000230e89d8a40>, '__dict__': <attribute '__dict__' of 'IntrospectionModule' objects>, '__weakref__': <attribute '__weakref__' of 'IntrospectionModule' objects>})"


# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x00000230e8102090>'

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.MyPaint', loader=<gi.importer.DynamicImporter object at 0x00000230e8102090>)"

