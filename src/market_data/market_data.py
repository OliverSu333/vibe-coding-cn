"""
市场数据模块

提供市场数据类，用于存储和管理期权定价所需的市场参数。
"""


class MarketData:
    """
    市场数据类
    
    用于存储和管理期权定价所需的市场参数，包括标的价格、波动率、
    无风险利率和股息率等。
    
    属性:
        spot_price (float): 标的资产当前价格，必须为正数
        volatility (float): 标的资产波动率，必须在 [0, 1] 范围内
        risk_free_rate (float): 无风险利率，必须为正数
        dividend_yield (float): 股息率，默认为 0，必须为非负数
    
    示例:
        >>> market_data = MarketData(
        ...     spot_price=100.0,
        ...     volatility=0.2,
        ...     risk_free_rate=0.05
        ... )
        >>> print(market_data.spot_price)
        100.0
    """
    
    def __init__(self, spot_price, volatility, risk_free_rate, dividend_yield=0.0):
        """
        初始化市场数据对象
        
        参数:
            spot_price (float): 标的资产当前价格
            volatility (float): 标的资产波动率
            risk_free_rate (float): 无风险利率
            dividend_yield (float, optional): 股息率，默认为 0.0
        
        异常:
            ValueError: 如果参数验证失败
        """
        # 验证并设置标的价格
        self._validate_positive(spot_price, "spot_price")
        self.spot_price = float(spot_price)
        
        # 验证并设置波动率
        self._validate_volatility(volatility)
        self.volatility = float(volatility)
        
        # 验证并设置无风险利率
        self._validate_positive(risk_free_rate, "risk_free_rate")
        self.risk_free_rate = float(risk_free_rate)
        
        # 验证并设置股息率
        self._validate_non_negative(dividend_yield, "dividend_yield")
        self.dividend_yield = float(dividend_yield)
    
    def _validate_positive(self, value, param_name):
        """
        验证参数必须为正数
        
        参数:
            value: 待验证的值
            param_name (str): 参数名称，用于错误消息
        
        异常:
            ValueError: 如果值不是正数
        """
        if not isinstance(value, (int, float)):
            raise ValueError(f"{param_name} 必须是数值类型")
        if value <= 0:
            raise ValueError(f"{param_name} 必须为正数，当前值: {value}")
    
    def _validate_non_negative(self, value, param_name):
        """
        验证参数必须为非负数
        
        参数:
            value: 待验证的值
            param_name (str): 参数名称，用于错误消息
        
        异常:
            ValueError: 如果值是负数
        """
        if not isinstance(value, (int, float)):
            raise ValueError(f"{param_name} 必须是数值类型")
        if value < 0:
            raise ValueError(f"{param_name} 必须为非负数，当前值: {value}")
    
    def _validate_volatility(self, volatility):
        """
        验证波动率在合理范围内 [0, 1]
        
        参数:
            volatility: 待验证的波动率值
        
        异常:
            ValueError: 如果波动率不在 [0, 1] 范围内
        """
        if not isinstance(volatility, (int, float)):
            raise ValueError("volatility 必须是数值类型")
        if volatility < 0 or volatility > 1:
            raise ValueError(
                f"volatility 必须在 [0, 1] 范围内，当前值: {volatility}"
            )
    
    def __repr__(self):
        """
        返回对象的字符串表示
        
        返回:
            str: 对象的字符串表示
        """
        return (
            f"MarketData(spot_price={self.spot_price}, "
            f"volatility={self.volatility}, "
            f"risk_free_rate={self.risk_free_rate}, "
            f"dividend_yield={self.dividend_yield})"
        )
    
    def __eq__(self, other):
        """
        判断两个 MarketData 对象是否相等
        
        参数:
            other: 另一个 MarketData 对象
        
        返回:
            bool: 如果所有属性都相等则返回 True，否则返回 False
        """
        if not isinstance(other, MarketData):
            return False
        return (
            abs(self.spot_price - other.spot_price) < 1e-10 and
            abs(self.volatility - other.volatility) < 1e-10 and
            abs(self.risk_free_rate - other.risk_free_rate) < 1e-10 and
            abs(self.dividend_yield - other.dividend_yield) < 1e-10
        )
