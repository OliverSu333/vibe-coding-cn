"""
测试定价方法基类模块

验证 PricingMethod 接口和 PricingResult 数据类
"""

import pytest
import numpy as np

from src.pricing_tool.pricing.base import PricingMethod, PricingResult
from src.pricing_tool.options.base import Option
from src.pricing_tool.utils.market_data import MarketData


class TestOption(Option):
    """测试用的 Option 实现类"""
    
    def payoff(self, S_T: np.ndarray) -> np.ndarray:
        """简单的看涨期权收益函数"""
        return np.maximum(S_T - self.K, 0)


class TestPricingMethod(PricingMethod):
    """测试用的 PricingMethod 实现类"""
    
    def price(self, option: Option, market_data: MarketData) -> PricingResult:
        """返回测试定价结果"""
        return PricingResult(
            price=10.0,
            delta=0.5,
            gamma=0.01,
            theta=-0.1,
            vega=20.0,
            rho=15.0,
        )


class TestPricingResult:
    """测试 PricingResult 数据类"""
    
    def test_pricing_result_creation(self):
        """测试创建定价结果对象"""
        result = PricingResult(
            price=10.0,
            delta=0.5,
            gamma=0.01,
            theta=-0.1,
            vega=20.0,
            rho=15.0,
        )
        
        assert result.price == 10.0
        assert result.delta == 0.5
        assert result.gamma == 0.01
        assert result.theta == -0.1
        assert result.vega == 20.0
        assert result.rho == 15.0
    
    def test_pricing_result_minimal(self):
        """测试最小定价结果（仅价格）"""
        result = PricingResult(price=10.0)
        
        assert result.price == 10.0
        assert result.delta is None
        assert result.gamma is None
        assert result.theta is None
        assert result.vega is None
        assert result.rho is None
    
    def test_pricing_result_to_dict(self):
        """测试转换为字典"""
        result = PricingResult(
            price=10.0,
            delta=0.5,
            gamma=0.01,
            theta=-0.1,
            vega=20.0,
            rho=15.0,
        )
        
        result_dict = result.to_dict()
        
        assert result_dict["price"] == 10.0
        assert result_dict["delta"] == 0.5
        assert result_dict["gamma"] == 0.01
        assert result_dict["theta"] == -0.1
        assert result_dict["vega"] == 20.0
        assert result_dict["rho"] == 15.0
    
    def test_pricing_result_to_dict_with_none(self):
        """测试包含 None 值的字典转换"""
        result = PricingResult(price=10.0)
        
        result_dict = result.to_dict()
        
        assert result_dict["price"] == 10.0
        assert result_dict["delta"] is None
        assert result_dict["gamma"] is None
    
    def test_pricing_result_repr(self):
        """测试字符串表示"""
        result = PricingResult(
            price=10.0,
            delta=0.5,
            gamma=0.01,
        )
        
        repr_str = repr(result)
        assert "PricingResult" in repr_str
        assert "price=10.000000" in repr_str
        assert "delta=0.500000" in repr_str
        assert "gamma=0.010000" in repr_str


class TestPricingMethod:
    """测试 PricingMethod 接口"""
    
    def test_pricing_method_abstract(self):
        """测试 PricingMethod 是抽象类，不能直接实例化"""
        with pytest.raises(TypeError):
            PricingMethod()
    
    def test_pricing_method_implementation(self):
        """测试 PricingMethod 的具体实现"""
        pricing_method = TestPricingMethod()
        
        option = TestOption(
            S=100.0,
            K=100.0,
            T=1.0,
            r=0.05,
            sigma=0.2,
            option_type="call",
        )
        
        market_data = MarketData(
            S=100.0,
            K=100.0,
            T=1.0,
            r=0.05,
            sigma=0.2,
        )
        
        result = pricing_method.price(option, market_data)
        
        assert isinstance(result, PricingResult)
        assert result.price == 10.0
        assert result.delta == 0.5
        assert result.gamma == 0.01
        assert result.theta == -0.1
        assert result.vega == 20.0
        assert result.rho == 15.0
    
    def test_pricing_method_repr(self):
        """测试定价方法的字符串表示"""
        pricing_method = TestPricingMethod()
        repr_str = repr(pricing_method)
        assert "TestPricingMethod" in repr_str
