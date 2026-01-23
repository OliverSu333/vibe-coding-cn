"""
市场数据模块

定义市场数据的数据类和验证方法
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class MarketData:
    """
    市场数据数据类
    
    包含期权定价所需的所有市场数据参数
    """
    S: float
    """标的资产当前价格"""
    
    K: float
    """执行价格"""
    
    T: float
    """到期时间（年）"""
    
    r: float
    """无风险利率（年化）"""
    
    sigma: float
    """波动率（年化）"""
    
    def __post_init__(self) -> None:
        """
        初始化后验证参数有效性
        
        抛出:
            ValueError: 如果参数无效
        """
        self.validate()
    
    def validate(self) -> None:
        """
        验证市场数据参数的有效性
        
        抛出:
            ValueError: 如果参数无效
        """
        if self.S <= 0:
            raise ValueError(f"标的资产价格 S 必须大于 0，当前值: {self.S}")
        if self.K <= 0:
            raise ValueError(f"执行价格 K 必须大于 0，当前值: {self.K}")
        if self.T <= 0:
            raise ValueError(f"到期时间 T 必须大于 0，当前值: {self.T}")
        if self.sigma <= 0:
            raise ValueError(f"波动率 sigma 必须大于 0，当前值: {self.sigma}")
        if self.r < 0:
            # 允许负利率（在某些市场环境下可能出现）
            pass
    
    def to_dict(self) -> dict:
        """
        将市场数据转换为字典
        
        返回:
            包含所有字段的字典
        """
        return {
            "S": self.S,
            "K": self.K,
            "T": self.T,
            "r": self.r,
            "sigma": self.sigma,
        }
    
    def __repr__(self) -> str:
        """
        返回市场数据的字符串表示
        
        返回:
            格式化的字符串
        """
        return (
            f"MarketData(S={self.S:.2f}, K={self.K:.2f}, "
            f"T={self.T:.4f}, r={self.r:.4f}, sigma={self.sigma:.4f})"
        )
