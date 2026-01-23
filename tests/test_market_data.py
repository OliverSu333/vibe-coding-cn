"""
测试市场数据模块

验证 MarketData 数据类的功能
"""

import pytest

from src.pricing_tool.utils.market_data import MarketData


class TestMarketData:
    """测试 MarketData 数据类"""
    
    def test_market_data_creation(self):
        """测试创建市场数据对象"""
        market_data = MarketData(
            S=100.0,
            K=100.0,
            T=1.0,
            r=0.05,
            sigma=0.2,
        )
        
        assert market_data.S == 100.0
        assert market_data.K == 100.0
        assert market_data.T == 1.0
        assert market_data.r == 0.05
        assert market_data.sigma == 0.2
    
    def test_market_data_validation_negative_S(self):
        """测试标的资产价格为负时的验证"""
        with pytest.raises(ValueError, match="标的资产价格 S 必须大于 0"):
            MarketData(S=-10.0, K=100.0, T=1.0, r=0.05, sigma=0.2)
    
    def test_market_data_validation_zero_S(self):
        """测试标的资产价格为 0 时的验证"""
        with pytest.raises(ValueError, match="标的资产价格 S 必须大于 0"):
            MarketData(S=0.0, K=100.0, T=1.0, r=0.05, sigma=0.2)
    
    def test_market_data_validation_negative_K(self):
        """测试执行价格为负时的验证"""
        with pytest.raises(ValueError, match="执行价格 K 必须大于 0"):
            MarketData(S=100.0, K=-10.0, T=1.0, r=0.05, sigma=0.2)
    
    def test_market_data_validation_negative_T(self):
        """测试到期时间为负时的验证"""
        with pytest.raises(ValueError, match="到期时间 T 必须大于 0"):
            MarketData(S=100.0, K=100.0, T=-1.0, r=0.05, sigma=0.2)
    
    def test_market_data_validation_negative_sigma(self):
        """测试波动率为负时的验证"""
        with pytest.raises(ValueError, match="波动率 sigma 必须大于 0"):
            MarketData(S=100.0, K=100.0, T=1.0, r=0.05, sigma=-0.2)
    
    def test_market_data_validation_zero_sigma(self):
        """测试波动率为 0 时的验证"""
        with pytest.raises(ValueError, match="波动率 sigma 必须大于 0"):
            MarketData(S=100.0, K=100.0, T=1.0, r=0.05, sigma=0.0)
    
    def test_market_data_negative_rate_allowed(self):
        """测试负利率是允许的（某些市场环境下可能出现）"""
        market_data = MarketData(
            S=100.0,
            K=100.0,
            T=1.0,
            r=-0.01,  # 负利率
            sigma=0.2,
        )
        
        assert market_data.r == -0.01
    
    def test_market_data_to_dict(self):
        """测试转换为字典"""
        market_data = MarketData(
            S=100.0,
            K=100.0,
            T=1.0,
            r=0.05,
            sigma=0.2,
        )
        
        data_dict = market_data.to_dict()
        
        assert data_dict["S"] == 100.0
        assert data_dict["K"] == 100.0
        assert data_dict["T"] == 1.0
        assert data_dict["r"] == 0.05
        assert data_dict["sigma"] == 0.2
    
    def test_market_data_repr(self):
        """测试字符串表示"""
        market_data = MarketData(
            S=100.0,
            K=100.0,
            T=1.0,
            r=0.05,
            sigma=0.2,
        )
        
        repr_str = repr(market_data)
        assert "MarketData" in repr_str
        assert "S=100.00" in repr_str
        assert "K=100.00" in repr_str
        assert "T=1.0000" in repr_str
        assert "r=0.0500" in repr_str
        assert "sigma=0.2000" in repr_str
