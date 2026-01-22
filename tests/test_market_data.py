"""
市场数据模块的单元测试

测试 MarketData 类的参数验证和默认值处理功能。
"""

import pytest
from src.market_data import MarketData


class TestMarketData:
    """MarketData 类的测试套件"""
    
    def test_valid_creation_with_default_dividend(self):
        """测试使用默认股息率创建有效的 MarketData 对象"""
        market_data = MarketData(
            spot_price=100.0,
            volatility=0.2,
            risk_free_rate=0.05
        )
        
        assert market_data.spot_price == 100.0
        assert market_data.volatility == 0.2
        assert market_data.risk_free_rate == 0.05
        assert market_data.dividend_yield == 0.0  # 默认值
    
    def test_valid_creation_with_all_parameters(self):
        """测试使用所有参数创建有效的 MarketData 对象"""
        market_data = MarketData(
            spot_price=150.0,
            volatility=0.3,
            risk_free_rate=0.04,
            dividend_yield=0.02
        )
        
        assert market_data.spot_price == 150.0
        assert market_data.volatility == 0.3
        assert market_data.risk_free_rate == 0.04
        assert market_data.dividend_yield == 0.02
    
    def test_spot_price_validation_positive(self):
        """测试标的价格必须为正数的验证"""
        # 测试零值
        with pytest.raises(ValueError, match="spot_price 必须为正数"):
            MarketData(spot_price=0, volatility=0.2, risk_free_rate=0.05)
        
        # 测试负值
        with pytest.raises(ValueError, match="spot_price 必须为正数"):
            MarketData(spot_price=-10, volatility=0.2, risk_free_rate=0.05)
    
    def test_volatility_validation_range(self):
        """测试波动率必须在 [0, 1] 范围内的验证"""
        # 测试负值
        with pytest.raises(ValueError, match="volatility 必须在 \\[0, 1\\] 范围内"):
            MarketData(spot_price=100, volatility=-0.1, risk_free_rate=0.05)
        
        # 测试大于1的值
        with pytest.raises(ValueError, match="volatility 必须在 \\[0, 1\\] 范围内"):
            MarketData(spot_price=100, volatility=1.5, risk_free_rate=0.05)
        
        # 测试边界值：0 和 1 应该有效
        market_data_0 = MarketData(spot_price=100, volatility=0, risk_free_rate=0.05)
        assert market_data_0.volatility == 0
        
        market_data_1 = MarketData(spot_price=100, volatility=1, risk_free_rate=0.05)
        assert market_data_1.volatility == 1
    
    def test_risk_free_rate_validation_positive(self):
        """测试无风险利率必须为正数的验证"""
        # 测试零值
        with pytest.raises(ValueError, match="risk_free_rate 必须为正数"):
            MarketData(spot_price=100, volatility=0.2, risk_free_rate=0)
        
        # 测试负值
        with pytest.raises(ValueError, match="risk_free_rate 必须为正数"):
            MarketData(spot_price=100, volatility=0.2, risk_free_rate=-0.01)
    
    def test_dividend_yield_validation_non_negative(self):
        """测试股息率必须为非负数的验证"""
        # 测试负值
        with pytest.raises(ValueError, match="dividend_yield 必须为非负数"):
            MarketData(
                spot_price=100,
                volatility=0.2,
                risk_free_rate=0.05,
                dividend_yield=-0.01
            )
        
        # 测试零值应该有效
        market_data = MarketData(
            spot_price=100,
            volatility=0.2,
            risk_free_rate=0.05,
            dividend_yield=0
        )
        assert market_data.dividend_yield == 0
    
    def test_type_validation(self):
        """测试类型验证"""
        # 测试非数值类型
        with pytest.raises(ValueError, match="必须是数值类型"):
            MarketData(spot_price="100", volatility=0.2, risk_free_rate=0.05)
        
        with pytest.raises(ValueError, match="必须是数值类型"):
            MarketData(spot_price=100, volatility="0.2", risk_free_rate=0.05)
        
        with pytest.raises(ValueError, match="必须是数值类型"):
            MarketData(spot_price=100, volatility=0.2, risk_free_rate="0.05")
        
        with pytest.raises(ValueError, match="必须是数值类型"):
            MarketData(
                spot_price=100,
                volatility=0.2,
                risk_free_rate=0.05,
                dividend_yield="0.01"
            )
    
    def test_numeric_conversion(self):
        """测试数值类型转换（int 转换为 float）"""
        market_data = MarketData(
            spot_price=100,  # int
            volatility=0.2,
            risk_free_rate=5,  # int
            dividend_yield=1  # int
        )
        
        # 验证所有值都是 float 类型
        assert isinstance(market_data.spot_price, float)
        assert isinstance(market_data.volatility, float)
        assert isinstance(market_data.risk_free_rate, float)
        assert isinstance(market_data.dividend_yield, float)
    
    def test_repr(self):
        """测试对象的字符串表示"""
        market_data = MarketData(
            spot_price=100.0,
            volatility=0.2,
            risk_free_rate=0.05,
            dividend_yield=0.01
        )
        
        repr_str = repr(market_data)
        assert "MarketData" in repr_str
        assert "spot_price=100.0" in repr_str
        assert "volatility=0.2" in repr_str
        assert "risk_free_rate=0.05" in repr_str
        assert "dividend_yield=0.01" in repr_str
    
    def test_equality(self):
        """测试对象相等性比较"""
        market_data1 = MarketData(
            spot_price=100.0,
            volatility=0.2,
            risk_free_rate=0.05,
            dividend_yield=0.01
        )
        
        market_data2 = MarketData(
            spot_price=100.0,
            volatility=0.2,
            risk_free_rate=0.05,
            dividend_yield=0.01
        )
        
        assert market_data1 == market_data2
    
    def test_inequality(self):
        """测试对象不相等的情况"""
        market_data1 = MarketData(
            spot_price=100.0,
            volatility=0.2,
            risk_free_rate=0.05
        )
        
        market_data2 = MarketData(
            spot_price=101.0,  # 不同的价格
            volatility=0.2,
            risk_free_rate=0.05
        )
        
        assert market_data1 != market_data2
    
    def test_equality_with_different_type(self):
        """测试与不同类型对象的相等性比较"""
        market_data = MarketData(
            spot_price=100.0,
            volatility=0.2,
            risk_free_rate=0.05
        )
        
        assert market_data != "not a MarketData"
        assert market_data != 100
        assert market_data != None
