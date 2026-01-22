"""
期权参数模块

提供期权参数类，用于存储和管理不同期权类型的特定参数。
"""

from abc import ABC


class OptionParams(ABC):
    """
    期权参数基类
    
    定义所有期权类型的通用参数，包括执行价格、到期时间和期权类型。
    
    属性:
        strike_price (float): 执行价格，必须为正数
        time_to_maturity (float): 到期时间（年），必须为正数
        option_type (str): 期权类型，'call'（看涨）或 'put'（看跌）
    
    示例:
        >>> params = VanillaParams(
        ...     strike_price=100.0,
        ...     time_to_maturity=0.25,
        ...     option_type='call'
        ... )
        >>> print(params.strike_price)
        100.0
    """
    
    def __init__(self, strike_price, time_to_maturity, option_type):
        """
        初始化期权参数对象
        
        参数:
            strike_price (float): 执行价格
            time_to_maturity (float): 到期时间（年）
            option_type (str): 期权类型，'call' 或 'put'
        
        异常:
            ValueError: 如果参数验证失败
        """
        # 验证并设置执行价格
        self._validate_positive(strike_price, "strike_price")
        self.strike_price = float(strike_price)
        
        # 验证并设置到期时间
        self._validate_positive(time_to_maturity, "time_to_maturity")
        self.time_to_maturity = float(time_to_maturity)
        
        # 验证并设置期权类型
        self._validate_option_type(option_type)
        self.option_type = option_type.lower()
    
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
    
    def _validate_option_type(self, option_type):
        """
        验证期权类型必须是 'call' 或 'put'
        
        参数:
            option_type: 待验证的期权类型
        
        异常:
            ValueError: 如果期权类型不是 'call' 或 'put'
        """
        if not isinstance(option_type, str):
            raise ValueError("option_type 必须是字符串类型")
        if option_type.lower() not in ['call', 'put']:
            raise ValueError(
                f"option_type 必须是 'call' 或 'put'，当前值: {option_type}"
            )
    
    def __repr__(self):
        """
        返回对象的字符串表示
        
        返回:
            str: 对象的字符串表示
        """
        return (
            f"{self.__class__.__name__}(strike_price={self.strike_price}, "
            f"time_to_maturity={self.time_to_maturity}, "
            f"option_type='{self.option_type}')"
        )
    
    def __eq__(self, other):
        """
        判断两个 OptionParams 对象是否相等
        
        参数:
            other: 另一个 OptionParams 对象
        
        返回:
            bool: 如果所有属性都相等则返回 True，否则返回 False
        """
        if not isinstance(other, self.__class__):
            return False
        return (
            abs(self.strike_price - other.strike_price) < 1e-10 and
            abs(self.time_to_maturity - other.time_to_maturity) < 1e-10 and
            self.option_type == other.option_type
        )


class VanillaParams(OptionParams):
    """
    Vanilla 期权参数类
    
    标准期权的参数，继承自 OptionParams，没有额外参数。
    
    属性:
        strike_price (float): 执行价格
        time_to_maturity (float): 到期时间（年）
        option_type (str): 期权类型，'call' 或 'put'
    
    示例:
        >>> params = VanillaParams(
        ...     strike_price=100.0,
        ...     time_to_maturity=0.25,
        ...     option_type='call'
        ... )
    """
    
    def __init__(self, strike_price, time_to_maturity, option_type):
        """
        初始化 Vanilla 期权参数对象
        
        参数:
            strike_price (float): 执行价格
            time_to_maturity (float): 到期时间（年）
            option_type (str): 期权类型，'call' 或 'put'
        """
        super().__init__(strike_price, time_to_maturity, option_type)


class DigitalParams(OptionParams):
    """
    Digital 期权参数类
    
    二元期权的参数，继承自 OptionParams，没有额外参数。
    
    属性:
        strike_price (float): 执行价格（触发价格）
        time_to_maturity (float): 到期时间（年）
        option_type (str): 期权类型，'call' 或 'put'
    
    示例:
        >>> params = DigitalParams(
        ...     strike_price=100.0,
        ...     time_to_maturity=0.25,
        ...     option_type='call'
        ... )
    """
    
    def __init__(self, strike_price, time_to_maturity, option_type):
        """
        初始化 Digital 期权参数对象
        
        参数:
            strike_price (float): 执行价格（触发价格）
            time_to_maturity (float): 到期时间（年）
            option_type (str): 期权类型，'call' 或 'put'
        """
        super().__init__(strike_price, time_to_maturity, option_type)


class BarrierParams(OptionParams):
    """
    Barrier 期权参数类
    
    障碍期权的参数，继承自 OptionParams，添加障碍水平、障碍方向、敲出/敲入类型和监控频率。
    
    属性:
        strike_price (float): 执行价格
        time_to_maturity (float): 到期时间（年）
        option_type (str): 期权类型，'call' 或 'put'
        barrier_level (float): 障碍水平（障碍价格），必须为正数
        barrier_direction (str): 障碍方向，'up'（向上）或 'down'（向下）
        knock_type (str): 敲出/敲入类型，'knock-out'（敲出）或 'knock-in'（敲入）
        monitoring_frequency (str 或 int): 监控频率，'continuous'（连续监控）或正整数（离散监控点数）
    
    示例:
        >>> params = BarrierParams(
        ...     strike_price=100.0,
        ...     time_to_maturity=0.25,
        ...     option_type='call',
        ...     barrier_level=110.0,
        ...     barrier_direction='up',
        ...     knock_type='knock-out',
        ...     monitoring_frequency='continuous'
        ... )
    """
    
    def __init__(
        self, 
        strike_price, 
        time_to_maturity, 
        option_type,
        barrier_level,
        barrier_direction,
        knock_type,
        monitoring_frequency='continuous'
    ):
        """
        初始化 Barrier 期权参数对象
        
        参数:
            strike_price (float): 执行价格
            time_to_maturity (float): 到期时间（年）
            option_type (str): 期权类型，'call' 或 'put'
            barrier_level (float): 障碍水平（障碍价格）
            barrier_direction (str): 障碍方向，'up' 或 'down'
            knock_type (str): 敲出/敲入类型，'knock-out' 或 'knock-in'
            monitoring_frequency (str 或 int, optional): 监控频率，默认为 'continuous'
                - 'continuous': 连续监控
                - 正整数: 离散监控点数（如 12 表示每月监控一次，共 12 次）
        
        异常:
            ValueError: 如果参数验证失败
        """
        super().__init__(strike_price, time_to_maturity, option_type)
        
        # 验证并设置障碍水平
        self._validate_positive(barrier_level, "barrier_level")
        self.barrier_level = float(barrier_level)
        # 保持向后兼容，barrier_price 作为 barrier_level 的别名
        self.barrier_price = self.barrier_level
        
        # 验证并设置障碍方向
        self._validate_barrier_direction(barrier_direction)
        self.barrier_direction = barrier_direction.lower()
        # 保持向后兼容，barrier_type 作为 barrier_direction 的别名
        self.barrier_type = self.barrier_direction
        
        # 验证并设置敲出/敲入类型
        self._validate_knock_type(knock_type)
        self.knock_type = knock_type.lower()
        
        # 验证并设置监控频率
        self._validate_monitoring_frequency(monitoring_frequency)
        if isinstance(monitoring_frequency, str):
            self.monitoring_frequency = monitoring_frequency.lower()
        else:
            self.monitoring_frequency = int(monitoring_frequency)
    
    def _validate_barrier_direction(self, barrier_direction):
        """
        验证障碍方向必须是 'up' 或 'down'
        
        参数:
            barrier_direction: 待验证的障碍方向
        
        异常:
            ValueError: 如果障碍方向不是 'up' 或 'down'
        """
        if not isinstance(barrier_direction, str):
            raise ValueError("barrier_direction 必须是字符串类型")
        if barrier_direction.lower() not in ['up', 'down']:
            raise ValueError(
                f"barrier_direction 必须是 'up' 或 'down'，当前值: {barrier_direction}"
            )
    
    def _validate_knock_type(self, knock_type):
        """
        验证敲出/敲入类型必须是 'knock-out' 或 'knock-in'
        
        参数:
            knock_type: 待验证的敲出/敲入类型
        
        异常:
            ValueError: 如果敲出/敲入类型不是 'knock-out' 或 'knock-in'
        """
        if not isinstance(knock_type, str):
            raise ValueError("knock_type 必须是字符串类型")
        if knock_type.lower() not in ['knock-out', 'knock-in']:
            raise ValueError(
                f"knock_type 必须是 'knock-out' 或 'knock-in'，当前值: {knock_type}"
            )
    
    def _validate_monitoring_frequency(self, monitoring_frequency):
        """
        验证监控频率
        
        参数:
            monitoring_frequency: 待验证的监控频率
        
        异常:
            ValueError: 如果监控频率无效
        """
        if isinstance(monitoring_frequency, str):
            if monitoring_frequency.lower() != 'continuous':
                raise ValueError(
                    f"monitoring_frequency 字符串值必须是 'continuous'，"
                    f"当前值: {monitoring_frequency}"
                )
        elif isinstance(monitoring_frequency, (int, float)):
            if isinstance(monitoring_frequency, float) and not monitoring_frequency.is_integer():
                raise ValueError(
                    f"monitoring_frequency 数值必须是正整数，当前值: {monitoring_frequency}"
                )
            if int(monitoring_frequency) <= 0:
                raise ValueError(
                    f"monitoring_frequency 必须为正整数，当前值: {monitoring_frequency}"
                )
        else:
            raise ValueError(
                f"monitoring_frequency 必须是字符串 'continuous' 或正整数，"
                f"当前类型: {type(monitoring_frequency)}"
            )
    
    def __repr__(self):
        """
        返回对象的字符串表示
        
        返回:
            str: 对象的字符串表示
        """
        return (
            f"BarrierParams(strike_price={self.strike_price}, "
            f"time_to_maturity={self.time_to_maturity}, "
            f"option_type='{self.option_type}', "
            f"barrier_level={self.barrier_level}, "
            f"barrier_direction='{self.barrier_direction}', "
            f"knock_type='{self.knock_type}', "
            f"monitoring_frequency={repr(self.monitoring_frequency)})"
        )
    
    def __eq__(self, other):
        """
        判断两个 BarrierParams 对象是否相等
        
        参数:
            other: 另一个 BarrierParams 对象
        
        返回:
            bool: 如果所有属性都相等则返回 True，否则返回 False
        """
        if not isinstance(other, BarrierParams):
            return False
        return (
            super().__eq__(other) and
            abs(self.barrier_level - other.barrier_level) < 1e-10 and
            self.barrier_direction == other.barrier_direction and
            self.knock_type == other.knock_type and
            self.monitoring_frequency == other.monitoring_frequency
        )


class AsianParams(OptionParams):
    """
    Asian 期权参数类
    
    亚式期权的参数，继承自 OptionParams，添加平均类型和监控点数。
    
    属性:
        strike_price (float): 执行价格
        time_to_maturity (float): 到期时间（年）
        option_type (str): 期权类型，'call' 或 'put'
        averaging_type (str): 平均类型，'arithmetic'（算术平均）或 'geometric'（几何平均）
        monitoring_points (int): 监控点数，必须为正整数
    
    示例:
        >>> params = AsianParams(
        ...     strike_price=100.0,
        ...     time_to_maturity=0.25,
        ...     option_type='call',
        ...     averaging_type='arithmetic',
        ...     monitoring_points=12
        ... )
    """
    
    def __init__(
        self,
        strike_price,
        time_to_maturity,
        option_type,
        averaging_type='arithmetic',
        monitoring_points=12
    ):
        """
        初始化 Asian 期权参数对象
        
        参数:
            strike_price (float): 执行价格
            time_to_maturity (float): 到期时间（年）
            option_type (str): 期权类型，'call' 或 'put'
            averaging_type (str, optional): 平均类型，'arithmetic' 或 'geometric'，默认为 'arithmetic'
            monitoring_points (int, optional): 监控点数，默认为 12
        
        异常:
            ValueError: 如果参数验证失败
        """
        super().__init__(strike_price, time_to_maturity, option_type)
        
        # 验证并设置平均类型
        self._validate_averaging_type(averaging_type)
        self.averaging_type = averaging_type.lower()
        
        # 验证并设置监控点数
        self._validate_positive_integer(monitoring_points, "monitoring_points")
        self.monitoring_points = int(monitoring_points)
    
    def _validate_averaging_type(self, averaging_type):
        """
        验证平均类型必须是 'arithmetic' 或 'geometric'
        
        参数:
            averaging_type: 待验证的平均类型
        
        异常:
            ValueError: 如果平均类型不是 'arithmetic' 或 'geometric'
        """
        if not isinstance(averaging_type, str):
            raise ValueError("averaging_type 必须是字符串类型")
        if averaging_type.lower() not in ['arithmetic', 'geometric']:
            raise ValueError(
                f"averaging_type 必须是 'arithmetic' 或 'geometric'，"
                f"当前值: {averaging_type}"
            )
    
    def _validate_positive_integer(self, value, param_name):
        """
        验证参数必须为正整数
        
        参数:
            value: 待验证的值
            param_name (str): 参数名称，用于错误消息
        
        异常:
            ValueError: 如果值不是正整数
        """
        if not isinstance(value, (int, float)):
            raise ValueError(f"{param_name} 必须是数值类型")
        if isinstance(value, float) and not value.is_integer():
            raise ValueError(f"{param_name} 必须是整数，当前值: {value}")
        if int(value) <= 0:
            raise ValueError(f"{param_name} 必须为正整数，当前值: {value}")
    
    def __repr__(self):
        """
        返回对象的字符串表示
        
        返回:
            str: 对象的字符串表示
        """
        return (
            f"AsianParams(strike_price={self.strike_price}, "
            f"time_to_maturity={self.time_to_maturity}, "
            f"option_type='{self.option_type}', "
            f"averaging_type='{self.averaging_type}', "
            f"monitoring_points={self.monitoring_points})"
        )
    
    def __eq__(self, other):
        """
        判断两个 AsianParams 对象是否相等
        
        参数:
            other: 另一个 AsianParams 对象
        
        返回:
            bool: 如果所有属性都相等则返回 True，否则返回 False
        """
        if not isinstance(other, AsianParams):
            return False
        return (
            super().__eq__(other) and
            self.averaging_type == other.averaging_type and
            self.monitoring_points == other.monitoring_points
        )
