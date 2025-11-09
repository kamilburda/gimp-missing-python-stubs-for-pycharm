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


# Variables with simple values

MAJOR_VERSION = 0

MICRO_VERSION = 24

MINOR_VERSION = 3

_namespace = 'Xmlb'

_version = '2.0'

# functions

def opcode_kind_from_string(p_str): # real signature unknown; restored from __doc__
    """ opcode_kind_from_string(str:str) -> Xmlb.OpcodeKind """
    pass

def opcode_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ opcode_kind_to_string(kind:Xmlb.OpcodeKind) -> str """
    return ""

def string_escape(p_str): # real signature unknown; restored from __doc__
    """ string_escape(str:str) -> str """
    return ""

def version_string(): # real signature unknown; restored from __doc__
    """ version_string() -> str """
    return ""

# classes

from .Builder import Builder
from .BuilderClass import BuilderClass
from .BuilderCompileFlags import BuilderCompileFlags
from .BuilderFixup import BuilderFixup
from .BuilderFixupClass import BuilderFixupClass
from .BuilderNode import BuilderNode
from .BuilderNodeClass import BuilderNodeClass
from .BuilderNodeFlags import BuilderNodeFlags
from .BuilderSource import BuilderSource
from .BuilderSourceClass import BuilderSourceClass
from .BuilderSourceCtx import BuilderSourceCtx
from .BuilderSourceCtxClass import BuilderSourceCtxClass
from .BuilderSourceFlags import BuilderSourceFlags
from .Machine import Machine
from .MachineClass import MachineClass
from .MachineDebugFlags import MachineDebugFlags
from .MachineParseFlags import MachineParseFlags
from .Node import Node
from .NodeAttrIter import NodeAttrIter
from .NodeChildIter import NodeChildIter
from .NodeClass import NodeClass
from .NodeExportFlags import NodeExportFlags
from .Opcode import Opcode
from .OpcodeFlags import OpcodeFlags
from .OpcodeKind import OpcodeKind
from .Query import Query
from .QueryClass import QueryClass
from .QueryContext import QueryContext
from .QueryFlags import QueryFlags
from .Silo import Silo
from .SiloClass import SiloClass
from .SiloLoadFlags import SiloLoadFlags
from .SiloProfileFlags import SiloProfileFlags
from .Stack import Stack
from .ValueBindings import ValueBindings
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x000001543230f7d0>'

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Xmlb', loader=<gi.importer.DynamicImporter object at 0x000001543230f7d0>)"

