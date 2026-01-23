"""
期权类型模块

包含所有期权类型的基类和具体实现
"""

from .base import Option
from .exotic import ExoticOption

__all__ = ["Option", "ExoticOption"]
