"""
测试期权基类模块

验证 Option 和 ExoticOption 基类的功能
"""

import pytest
import numpy as np
from typing import Literal

from src.pricing_tool.options.base import Option
from src.pricing_tool.options.exotic import ExoticOption


class TestOption(Option):
    """
    测试用的 Option 实现类
    """
    
    def payoff(self, S_T: np.ndarray) -> np.ndarray:
        """
        简单的看涨/看跌期权收益函数
        """
        if self.is_call:
            return np.maximum(S_T - self.K, 0)
        else:
            return np.maximum(self.K - S_T, 0)


class TestExoticOption(ExoticOption):
    """
    测试用的 ExoticOption 实现类
    """
    
    def payoff(self, S_T: np.ndarray) -> np.ndarray:
        """
        简单的看涨/看跌期权收益函数
        """
        if self.is_call:
            return np.maximum(S_T - self.K, 0)
        else:
            return np.maximum(self.K - S_T, 0)
    
    def boundary_condition(self, S: np.ndarray, t: float) -> np.ndarray:
        """
        简单的边界条件
        """
        return np.zeros_like(S)


class TestOptionBase:
    """测试 Option 基类"""
    
    def test_option_initialization(self):
        """测试期权对象初始化"""
        option = TestOption(
            S=100.0,
            K=100.0,
            T=1.0,
            r=0.05,
            sigma=0.2,
            option_type="call",
        )
        
        assert option.S == 100.0
        assert option.K == 100.0
        assert option.T == 1.0
        assert option.r == 0.05
        assert option.sigma == 0.2
        assert option.option_type == "call"
        assert option.is_call is True
        assert option.is_put is False
    
    def test_option_put_type(self):
        """测试看跌期权类型"""
        option = TestOption(
            S=100.0,
            K=100.0,
            T=1.0,
            r=0.05,
            sigma=0.2,
            option_type="put",
        )
        
        assert option.is_put is True
        assert option.is_call is False
    
    def test_option_validation_negative_S(self):
        """测试标的资产价格为负时的验证"""
        with pytest.raises(ValueError, match="标的资产价格 S 必须大于 0"):
            TestOption(S=-10.0, K=100.0, T=1.0, r=0.05, sigma=0.2, option_type="call")
    
    def test_option_validation_negative_K(self):
        """测试执行价格为负时的验证"""
        with pytest.raises(ValueError, match="执行价格 K 必须大于 0"):
            TestOption(S=100.0, K=-10.0, T=1.0, r=0.05, sigma=0.2, option_type="call")
    
    def test_option_validation_negative_T(self):
        """测试到期时间为负时的验证"""
        with pytest.raises(ValueError, match="到期时间 T 必须大于 0"):
            TestOption(S=100.0, K=100.0, T=-1.0, r=0.05, sigma=0.2, option_type="call")
    
    def test_option_validation_negative_sigma(self):
        """测试波动率为负时的验证"""
        with pytest.raises(ValueError, match="波动率 sigma 必须大于 0"):
            TestOption(S=100.0, K=100.0, T=1.0, r=0.05, sigma=-0.2, option_type="call")
    
    def test_option_validation_invalid_type(self):
        """测试无效期权类型时的验证"""
        with pytest.raises(ValueError, match="期权类型必须是 'call' 或 'put'"):
            TestOption(S=100.0, K=100.0, T=1.0, r=0.05, sigma=0.2, option_type="invalid")
    
    def test_option_payoff_call(self):
        """测试看涨期权收益函数"""
        option = TestOption(
            S=100.0,
            K=100.0,
            T=1.0,
            r=0.05,
            sigma=0.2,
            option_type="call",
        )
        
        S_T = np.array([80.0, 100.0, 120.0])
        payoff = option.payoff(S_T)
        
        expected = np.array([0.0, 0.0, 20.0])
        np.testing.assert_array_almost_equal(payoff, expected)
    
    def test_option_payoff_put(self):
        """测试看跌期权收益函数"""
        option = TestOption(
            S=100.0,
            K=100.0,
            T=1.0,
            r=0.05,
            sigma=0.2,
            option_type="put",
        )
        
        S_T = np.array([80.0, 100.0, 120.0])
        payoff = option.payoff(S_T)
        
        expected = np.array([20.0, 0.0, 0.0])
        np.testing.assert_array_almost_equal(payoff, expected)
    
    def test_option_repr(self):
        """测试期权对象的字符串表示"""
        option = TestOption(
            S=100.0,
            K=100.0,
            T=1.0,
            r=0.05,
            sigma=0.2,
            option_type="call",
        )
        
        repr_str = repr(option)
        assert "TestOption" in repr_str
        assert "S=100.00" in repr_str
        assert "K=100.00" in repr_str
        assert "type=call" in repr_str


class TestExoticOptionBase:
    """测试 ExoticOption 基类"""
    
    def test_exotic_option_initialization(self):
        """测试奇异期权对象初始化"""
        exotic_option = TestExoticOption(
            S=100.0,
            K=100.0,
            T=1.0,
            r=0.05,
            sigma=0.2,
            option_type="call",
        )
        
        assert exotic_option.S == 100.0
        assert exotic_option.K == 100.0
        assert exotic_option.T == 1.0
        assert exotic_option.r == 0.05
        assert exotic_option.sigma == 0.2
        assert exotic_option.option_type == "call"
    
    def test_exotic_option_boundary_condition(self):
        """测试边界条件方法"""
        exotic_option = TestExoticOption(
            S=100.0,
            K=100.0,
            T=1.0,
            r=0.05,
            sigma=0.2,
            option_type="call",
        )
        
        S = np.array([50.0, 100.0, 150.0])
        t = 0.5
        boundary = exotic_option.boundary_condition(S, t)
        
        expected = np.array([0.0, 0.0, 0.0])
        np.testing.assert_array_almost_equal(boundary, expected)
    
    def test_exotic_option_inheritance(self):
        """测试 ExoticOption 继承自 Option"""
        exotic_option = TestExoticOption(
            S=100.0,
            K=100.0,
            T=1.0,
            r=0.05,
            sigma=0.2,
            option_type="call",
        )
        
        # 验证继承的属性
        assert exotic_option.is_call is True
        assert exotic_option.is_put is False
        
        # 验证继承的方法
        S_T = np.array([80.0, 100.0, 120.0])
        payoff = exotic_option.payoff(S_T)
        expected = np.array([0.0, 0.0, 20.0])
        np.testing.assert_array_almost_equal(payoff, expected)
