"""
奇异期权基类模块

定义所有奇异期权类型的抽象基类
"""

from abc import ABC, abstractmethod
from typing import Optional
import numpy as np

from .base import Option


class ExoticOption(Option, ABC):
    """
    奇异期权抽象基类
    
    继承自 Option，定义所有奇异期权的通用接口和抽象方法
    奇异期权通常具有路径依赖性，需要特殊的定价方法
    """
    
    def __init__(
        self,
        S: float,
        K: float,
        T: float,
        r: float,
        sigma: float,
        option_type: str,
    ):
        """
        初始化奇异期权对象
        
        参数:
            S: 标的资产当前价格
            K: 执行价格
            T: 到期时间（年）
            r: 无风险利率（年化）
            sigma: 波动率（年化）
            option_type: 期权类型，"call" 或 "put"
        """
        super().__init__(S, K, T, r, sigma, option_type)
    
    @abstractmethod
    def payoff(self, S_T: np.ndarray) -> np.ndarray:
        """
        计算奇异期权收益函数（抽象方法）
        
        参数:
            S_T: 到期时的标的资产价格或价格路径（可以是标量或数组）
            
        返回:
            期权收益（与 S_T 同形状的数组）
            
        注意:
            子类必须实现此方法，定义具体的收益计算逻辑
            对于路径依赖型期权，S_T 可能是价格路径数组
        """
        pass
    
    @abstractmethod
    def boundary_condition(
        self,
        S: np.ndarray,
        t: float,
    ) -> np.ndarray:
        """
        计算边界条件（抽象方法）
        
        用于 PDE 方法求解时的边界条件设置
        
        参数:
            S: 标的资产价格数组（网格点）
            t: 当前时间
            
        返回:
            边界条件值数组
            
        注意:
            子类必须实现此方法，定义边界条件的计算逻辑
        """
        pass
    
    def __repr__(self) -> str:
        """
        返回奇异期权的字符串表示
        
        返回:
            奇异期权的描述字符串
        """
        return f"{self.__class__.__name__}({super().__repr__()})"
