"""
定价方法基类模块

定义所有定价方法的抽象接口
"""

from abc import ABC, abstractmethod
from typing import Dict, Optional
from dataclasses import dataclass

from ..options.base import Option
from ..utils.market_data import MarketData


@dataclass
class PricingResult:
    """
    定价结果数据类
    
    包含期权价格、Greeks 和其他相关信息
    """
    price: float
    """期权价格"""
    
    delta: Optional[float] = None
    """Delta：价格对标的价格的敏感性"""
    
    gamma: Optional[float] = None
    """Gamma：Delta 对标的价格的敏感性"""
    
    theta: Optional[float] = None
    """Theta：价格对时间的敏感性"""
    
    vega: Optional[float] = None
    """Vega：价格对波动率的敏感性"""
    
    rho: Optional[float] = None
    """Rho：价格对利率的敏感性"""
    
    def to_dict(self) -> Dict[str, Optional[float]]:
        """
        将定价结果转换为字典
        
        返回:
            包含所有字段的字典
        """
        return {
            "price": self.price,
            "delta": self.delta,
            "gamma": self.gamma,
            "theta": self.theta,
            "vega": self.vega,
            "rho": self.rho,
        }
    
    def __repr__(self) -> str:
        """
        返回定价结果的字符串表示
        
        返回:
            格式化的字符串
        """
        parts = [f"price={self.price:.6f}"]
        if self.delta is not None:
            parts.append(f"delta={self.delta:.6f}")
        if self.gamma is not None:
            parts.append(f"gamma={self.gamma:.6f}")
        if self.theta is not None:
            parts.append(f"theta={self.theta:.6f}")
        if self.vega is not None:
            parts.append(f"vega={self.vega:.6f}")
        if self.rho is not None:
            parts.append(f"rho={self.rho:.6f}")
        return f"PricingResult({', '.join(parts)})"


class PricingMethod(ABC):
    """
    定价方法抽象接口
    
    定义所有定价方法的通用接口，包括 PDE 和 MC 方法
    """
    
    @abstractmethod
    def price(
        self,
        option: Option,
        market_data: MarketData,
    ) -> PricingResult:
        """
        计算期权价格和 Greeks（抽象方法）
        
        参数:
            option: 期权对象实例
            market_data: 市场数据对象
            
        返回:
            PricingResult 对象，包含价格和 Greeks
            
        注意:
            子类必须实现此方法，定义具体的定价计算逻辑
        """
        pass
    
    def __repr__(self) -> str:
        """
        返回定价方法的字符串表示
        
        返回:
            定价方法的描述字符串
        """
        return f"{self.__class__.__name__}()"
