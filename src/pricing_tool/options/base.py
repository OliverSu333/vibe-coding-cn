"""
期权基类模块

定义所有期权类型的抽象基类
"""

from abc import ABC, abstractmethod
from typing import Literal, Optional
import numpy as np


class Option(ABC):
    """
    期权抽象基类
    
    定义所有期权类型的通用属性和接口
    """
    
    def __init__(
        self,
        S: float,
        K: float,
        T: float,
        r: float,
        sigma: float,
        option_type: Literal["call", "put"],
    ):
        """
        初始化期权对象
        
        参数:
            S: 标的资产当前价格
            K: 执行价格
            T: 到期时间（年）
            r: 无风险利率（年化）
            sigma: 波动率（年化）
            option_type: 期权类型，"call" 表示看涨期权，"put" 表示看跌期权
        """
        self._validate_params(S, K, T, r, sigma, option_type)
        
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.option_type = option_type
    
    @staticmethod
    def _validate_params(
        S: float,
        K: float,
        T: float,
        r: float,
        sigma: float,
        option_type: str,
    ) -> None:
        """
        验证参数有效性
        
        参数:
            S: 标的资产价格
            K: 执行价格
            T: 到期时间
            r: 无风险利率
            sigma: 波动率
            option_type: 期权类型
            
        抛出:
            ValueError: 如果参数无效
        """
        if S <= 0:
            raise ValueError(f"标的资产价格 S 必须大于 0，当前值: {S}")
        if K <= 0:
            raise ValueError(f"执行价格 K 必须大于 0，当前值: {K}")
        if T <= 0:
            raise ValueError(f"到期时间 T 必须大于 0，当前值: {T}")
        if sigma <= 0:
            raise ValueError(f"波动率 sigma 必须大于 0，当前值: {sigma}")
        if option_type not in ["call", "put"]:
            raise ValueError(f"期权类型必须是 'call' 或 'put'，当前值: {option_type}")
    
    @property
    def is_call(self) -> bool:
        """
        判断是否为看涨期权
        
        返回:
            True 如果是看涨期权，False 如果是看跌期权
        """
        return self.option_type == "call"
    
    @property
    def is_put(self) -> bool:
        """
        判断是否为看跌期权
        
        返回:
            True 如果是看跌期权，False 如果是看涨期权
        """
        return self.option_type == "put"
    
    @abstractmethod
    def payoff(self, S_T: np.ndarray) -> np.ndarray:
        """
        计算期权收益函数（抽象方法）
        
        参数:
            S_T: 到期时的标的资产价格（可以是标量或数组）
            
        返回:
            期权收益（与 S_T 同形状的数组）
            
        注意:
            子类必须实现此方法，定义具体的收益计算逻辑
        """
        pass
    
    def __repr__(self) -> str:
        """
        返回期权的字符串表示
        
        返回:
            期权的描述字符串
        """
        return (
            f"{self.__class__.__name__}("
            f"S={self.S:.2f}, K={self.K:.2f}, T={self.T:.4f}, "
            f"r={self.r:.4f}, sigma={self.sigma:.4f}, "
            f"type={self.option_type})"
        )
