"""
期权参数模块的单元测试
"""

import pytest
from src.options.option_params import (
    OptionParams,
    VanillaParams,
    DigitalParams,
    BarrierParams,
    AsianParams
)


class TestOptionParams:
    """OptionParams 基类的测试"""
    
    def test_vanilla_params_creation(self):
        """测试 VanillaParams 的创建"""
        params = VanillaParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call'
        )
        assert params.strike_price == 100.0
        assert params.time_to_maturity == 0.25
        assert params.option_type == 'call'
    
    def test_vanilla_params_put(self):
        """测试 VanillaParams 看跌期权"""
        params = VanillaParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='put'
        )
        assert params.option_type == 'put'
    
    def test_vanilla_params_case_insensitive(self):
        """测试期权类型大小写不敏感"""
        params = VanillaParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='CALL'
        )
        assert params.option_type == 'call'
    
    def test_strike_price_validation_positive(self):
        """测试执行价格必须为正数"""
        with pytest.raises(ValueError, match="strike_price 必须为正数"):
            VanillaParams(
                strike_price=-100.0,
                time_to_maturity=0.25,
                option_type='call'
            )
    
    def test_strike_price_validation_zero(self):
        """测试执行价格不能为零"""
        with pytest.raises(ValueError, match="strike_price 必须为正数"):
            VanillaParams(
                strike_price=0.0,
                time_to_maturity=0.25,
                option_type='call'
            )
    
    def test_strike_price_type_validation(self):
        """测试执行价格类型验证"""
        with pytest.raises(ValueError, match="strike_price 必须是数值类型"):
            VanillaParams(
                strike_price='100',
                time_to_maturity=0.25,
                option_type='call'
            )
    
    def test_time_to_maturity_validation_positive(self):
        """测试到期时间必须为正数"""
        with pytest.raises(ValueError, match="time_to_maturity 必须为正数"):
            VanillaParams(
                strike_price=100.0,
                time_to_maturity=-0.25,
                option_type='call'
            )
    
    def test_time_to_maturity_validation_zero(self):
        """测试到期时间不能为零"""
        with pytest.raises(ValueError, match="time_to_maturity 必须为正数"):
            VanillaParams(
                strike_price=100.0,
                time_to_maturity=0.0,
                option_type='call'
            )
    
    def test_option_type_validation(self):
        """测试期权类型验证"""
        with pytest.raises(ValueError, match="option_type 必须是 'call' 或 'put'"):
            VanillaParams(
                strike_price=100.0,
                time_to_maturity=0.25,
                option_type='invalid'
            )
    
    def test_option_type_type_validation(self):
        """测试期权类型必须是字符串"""
        with pytest.raises(ValueError, match="option_type 必须是字符串类型"):
            VanillaParams(
                strike_price=100.0,
                time_to_maturity=0.25,
                option_type=123
            )
    
    def test_int_to_float_conversion(self):
        """测试整数自动转换为浮点数"""
        params = VanillaParams(
            strike_price=100,
            time_to_maturity=1,
            option_type='call'
        )
        assert isinstance(params.strike_price, float)
        assert isinstance(params.time_to_maturity, float)
        assert params.strike_price == 100.0
        assert params.time_to_maturity == 1.0
    
    def test_repr(self):
        """测试字符串表示"""
        params = VanillaParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call'
        )
        repr_str = repr(params)
        assert 'VanillaParams' in repr_str
        assert 'strike_price=100.0' in repr_str
        assert 'time_to_maturity=0.25' in repr_str
        assert "option_type='call'" in repr_str
    
    def test_equality(self):
        """测试对象相等性"""
        params1 = VanillaParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call'
        )
        params2 = VanillaParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call'
        )
        assert params1 == params2
    
    def test_inequality_different_values(self):
        """测试不同值的对象不相等"""
        params1 = VanillaParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call'
        )
        params2 = VanillaParams(
            strike_price=110.0,
            time_to_maturity=0.25,
            option_type='call'
        )
        assert params1 != params2
    
    def test_inequality_different_types(self):
        """测试不同类型对象不相等"""
        params1 = VanillaParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call'
        )
        params2 = DigitalParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call'
        )
        assert params1 != params2


class TestDigitalParams:
    """DigitalParams 类的测试"""
    
    def test_digital_params_creation(self):
        """测试 DigitalParams 的创建"""
        params = DigitalParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call'
        )
        assert params.strike_price == 100.0
        assert params.time_to_maturity == 0.25
        assert params.option_type == 'call'
    
    def test_digital_params_put(self):
        """测试 DigitalParams 看跌期权"""
        params = DigitalParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='put'
        )
        assert params.option_type == 'put'


class TestBarrierParams:
    """BarrierParams 类的测试"""
    
    def test_barrier_params_creation(self):
        """测试 BarrierParams 的创建（使用新参数）"""
        params = BarrierParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call',
            barrier_level=110.0,
            barrier_direction='up',
            knock_type='knock-out'
        )
        assert params.strike_price == 100.0
        assert params.time_to_maturity == 0.25
        assert params.option_type == 'call'
        assert params.barrier_level == 110.0
        assert params.barrier_direction == 'up'
        assert params.knock_type == 'knock-out'
        assert params.monitoring_frequency == 'continuous'
        # 测试向后兼容性
        assert params.barrier_price == 110.0
        assert params.barrier_type == 'up'
    
    def test_barrier_params_creation_with_monitoring_frequency(self):
        """测试 BarrierParams 创建（指定监控频率）"""
        params = BarrierParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call',
            barrier_level=110.0,
            barrier_direction='up',
            knock_type='knock-out',
            monitoring_frequency=12
        )
        assert params.monitoring_frequency == 12
    
    def test_barrier_params_down(self):
        """测试向下障碍期权"""
        params = BarrierParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call',
            barrier_level=90.0,
            barrier_direction='down',
            knock_type='knock-out'
        )
        assert params.barrier_direction == 'down'
        assert params.barrier_type == 'down'
    
    def test_barrier_params_knock_in(self):
        """测试敲入障碍期权"""
        params = BarrierParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call',
            barrier_level=110.0,
            barrier_direction='up',
            knock_type='knock-in'
        )
        assert params.knock_type == 'knock-in'
    
    def test_barrier_direction_case_insensitive(self):
        """测试障碍方向大小写不敏感"""
        params = BarrierParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call',
            barrier_level=110.0,
            barrier_direction='UP',
            knock_type='knock-out'
        )
        assert params.barrier_direction == 'up'
    
    def test_knock_type_case_insensitive(self):
        """测试敲出/敲入类型大小写不敏感"""
        params = BarrierParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call',
            barrier_level=110.0,
            barrier_direction='up',
            knock_type='KNOCK-OUT'
        )
        assert params.knock_type == 'knock-out'
    
    def test_barrier_level_validation_positive(self):
        """测试障碍水平必须为正数"""
        with pytest.raises(ValueError, match="barrier_level 必须为正数"):
            BarrierParams(
                strike_price=100.0,
                time_to_maturity=0.25,
                option_type='call',
                barrier_level=-110.0,
                barrier_direction='up',
                knock_type='knock-out'
            )
    
    def test_barrier_level_validation_zero(self):
        """测试障碍水平不能为零"""
        with pytest.raises(ValueError, match="barrier_level 必须为正数"):
            BarrierParams(
                strike_price=100.0,
                time_to_maturity=0.25,
                option_type='call',
                barrier_level=0.0,
                barrier_direction='up',
                knock_type='knock-out'
            )
    
    def test_barrier_direction_validation(self):
        """测试障碍方向验证"""
        with pytest.raises(ValueError, match="barrier_direction 必须是 'up' 或 'down'"):
            BarrierParams(
                strike_price=100.0,
                time_to_maturity=0.25,
                option_type='call',
                barrier_level=110.0,
                barrier_direction='invalid',
                knock_type='knock-out'
            )
    
    def test_barrier_direction_type_validation(self):
        """测试障碍方向必须是字符串"""
        with pytest.raises(ValueError, match="barrier_direction 必须是字符串类型"):
            BarrierParams(
                strike_price=100.0,
                time_to_maturity=0.25,
                option_type='call',
                barrier_level=110.0,
                barrier_direction=123,
                knock_type='knock-out'
            )
    
    def test_knock_type_validation(self):
        """测试敲出/敲入类型验证"""
        with pytest.raises(ValueError, match="knock_type 必须是 'knock-out' 或 'knock-in'"):
            BarrierParams(
                strike_price=100.0,
                time_to_maturity=0.25,
                option_type='call',
                barrier_level=110.0,
                barrier_direction='up',
                knock_type='invalid'
            )
    
    def test_knock_type_type_validation(self):
        """测试敲出/敲入类型必须是字符串"""
        with pytest.raises(ValueError, match="knock_type 必须是字符串类型"):
            BarrierParams(
                strike_price=100.0,
                time_to_maturity=0.25,
                option_type='call',
                barrier_level=110.0,
                barrier_direction='up',
                knock_type=123
            )
    
    def test_monitoring_frequency_continuous(self):
        """测试连续监控频率"""
        params = BarrierParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call',
            barrier_level=110.0,
            barrier_direction='up',
            knock_type='knock-out',
            monitoring_frequency='continuous'
        )
        assert params.monitoring_frequency == 'continuous'
    
    def test_monitoring_frequency_discrete(self):
        """测试离散监控频率（正整数）"""
        params = BarrierParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call',
            barrier_level=110.0,
            barrier_direction='up',
            knock_type='knock-out',
            monitoring_frequency=12
        )
        assert params.monitoring_frequency == 12
        assert isinstance(params.monitoring_frequency, int)
    
    def test_monitoring_frequency_validation_string(self):
        """测试监控频率字符串验证"""
        with pytest.raises(ValueError, match="monitoring_frequency 字符串值必须是 'continuous'"):
            BarrierParams(
                strike_price=100.0,
                time_to_maturity=0.25,
                option_type='call',
                barrier_level=110.0,
                barrier_direction='up',
                knock_type='knock-out',
                monitoring_frequency='invalid'
            )
    
    def test_monitoring_frequency_validation_positive(self):
        """测试监控频率必须为正整数"""
        with pytest.raises(ValueError, match="monitoring_frequency 必须为正整数"):
            BarrierParams(
                strike_price=100.0,
                time_to_maturity=0.25,
                option_type='call',
                barrier_level=110.0,
                barrier_direction='up',
                knock_type='knock-out',
                monitoring_frequency=-1
            )
    
    def test_monitoring_frequency_validation_zero(self):
        """测试监控频率不能为零"""
        with pytest.raises(ValueError, match="monitoring_frequency 必须为正整数"):
            BarrierParams(
                strike_price=100.0,
                time_to_maturity=0.25,
                option_type='call',
                barrier_level=110.0,
                barrier_direction='up',
                knock_type='knock-out',
                monitoring_frequency=0
            )
    
    def test_monitoring_frequency_validation_float(self):
        """测试监控频率不能为浮点数"""
        with pytest.raises(ValueError, match="monitoring_frequency 数值必须是正整数"):
            BarrierParams(
                strike_price=100.0,
                time_to_maturity=0.25,
                option_type='call',
                barrier_level=110.0,
                barrier_direction='up',
                knock_type='knock-out',
                monitoring_frequency=12.5
            )
    
    def test_monitoring_frequency_int_conversion(self):
        """测试监控频率整数转换"""
        params = BarrierParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call',
            barrier_level=110.0,
            barrier_direction='up',
            knock_type='knock-out',
            monitoring_frequency=12.0
        )
        assert isinstance(params.monitoring_frequency, int)
        assert params.monitoring_frequency == 12
    
    def test_monitoring_frequency_type_validation(self):
        """测试监控频率类型验证"""
        with pytest.raises(ValueError, match="monitoring_frequency 必须是字符串 'continuous' 或正整数"):
            BarrierParams(
                strike_price=100.0,
                time_to_maturity=0.25,
                option_type='call',
                barrier_level=110.0,
                barrier_direction='up',
                knock_type='knock-out',
                monitoring_frequency=[12]
            )
    
    def test_barrier_params_repr(self):
        """测试 BarrierParams 的字符串表示"""
        params = BarrierParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call',
            barrier_level=110.0,
            barrier_direction='up',
            knock_type='knock-out',
            monitoring_frequency='continuous'
        )
        repr_str = repr(params)
        assert 'BarrierParams' in repr_str
        assert 'barrier_level=110.0' in repr_str
        assert "barrier_direction='up'" in repr_str
        assert "knock_type='knock-out'" in repr_str
        assert "monitoring_frequency='continuous'" in repr_str
    
    def test_barrier_params_equality(self):
        """测试 BarrierParams 对象相等性"""
        params1 = BarrierParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call',
            barrier_level=110.0,
            barrier_direction='up',
            knock_type='knock-out',
            monitoring_frequency='continuous'
        )
        params2 = BarrierParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call',
            barrier_level=110.0,
            barrier_direction='up',
            knock_type='knock-out',
            monitoring_frequency='continuous'
        )
        assert params1 == params2
    
    def test_barrier_params_inequality_different_level(self):
        """测试 BarrierParams 对象不相等（不同障碍水平）"""
        params1 = BarrierParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call',
            barrier_level=110.0,
            barrier_direction='up',
            knock_type='knock-out',
            monitoring_frequency='continuous'
        )
        params2 = BarrierParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call',
            barrier_level=120.0,
            barrier_direction='up',
            knock_type='knock-out',
            monitoring_frequency='continuous'
        )
        assert params1 != params2
    
    def test_barrier_params_inequality_different_knock_type(self):
        """测试 BarrierParams 对象不相等（不同敲出/敲入类型）"""
        params1 = BarrierParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call',
            barrier_level=110.0,
            barrier_direction='up',
            knock_type='knock-out',
            monitoring_frequency='continuous'
        )
        params2 = BarrierParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call',
            barrier_level=110.0,
            barrier_direction='up',
            knock_type='knock-in',
            monitoring_frequency='continuous'
        )
        assert params1 != params2
    
    def test_barrier_params_inequality_different_monitoring_frequency(self):
        """测试 BarrierParams 对象不相等（不同监控频率）"""
        params1 = BarrierParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call',
            barrier_level=110.0,
            barrier_direction='up',
            knock_type='knock-out',
            monitoring_frequency='continuous'
        )
        params2 = BarrierParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call',
            barrier_level=110.0,
            barrier_direction='up',
            knock_type='knock-out',
            monitoring_frequency=12
        )
        assert params1 != params2


class TestAsianParams:
    """AsianParams 类的测试"""
    
    def test_asian_params_creation_default(self):
        """测试 AsianParams 的创建（使用默认值）"""
        params = AsianParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call'
        )
        assert params.strike_price == 100.0
        assert params.time_to_maturity == 0.25
        assert params.option_type == 'call'
        assert params.averaging_type == 'arithmetic'
        assert params.monitoring_points == 12
    
    def test_asian_params_creation_custom(self):
        """测试 AsianParams 的创建（自定义参数）"""
        params = AsianParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call',
            averaging_type='geometric',
            monitoring_points=24
        )
        assert params.averaging_type == 'geometric'
        assert params.monitoring_points == 24
    
    def test_averaging_type_case_insensitive(self):
        """测试平均类型大小写不敏感"""
        params = AsianParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call',
            averaging_type='ARITHMETIC'
        )
        assert params.averaging_type == 'arithmetic'
    
    def test_averaging_type_validation(self):
        """测试平均类型验证"""
        with pytest.raises(ValueError, match="averaging_type 必须是 'arithmetic' 或 'geometric'"):
            AsianParams(
                strike_price=100.0,
                time_to_maturity=0.25,
                option_type='call',
                averaging_type='invalid'
            )
    
    def test_averaging_type_type_validation(self):
        """测试平均类型必须是字符串"""
        with pytest.raises(ValueError, match="averaging_type 必须是字符串类型"):
            AsianParams(
                strike_price=100.0,
                time_to_maturity=0.25,
                option_type='call',
                averaging_type=123
            )
    
    def test_monitoring_points_validation_positive(self):
        """测试监控点数必须为正整数"""
        with pytest.raises(ValueError, match="monitoring_points 必须为正整数"):
            AsianParams(
                strike_price=100.0,
                time_to_maturity=0.25,
                option_type='call',
                monitoring_points=-1
            )
    
    def test_monitoring_points_validation_zero(self):
        """测试监控点数不能为零"""
        with pytest.raises(ValueError, match="monitoring_points 必须为正整数"):
            AsianParams(
                strike_price=100.0,
                time_to_maturity=0.25,
                option_type='call',
                monitoring_points=0
            )
    
    def test_monitoring_points_validation_float(self):
        """测试监控点数不能为浮点数"""
        with pytest.raises(ValueError, match="monitoring_points 必须是整数"):
            AsianParams(
                strike_price=100.0,
                time_to_maturity=0.25,
                option_type='call',
                monitoring_points=12.5
            )
    
    def test_monitoring_points_int_conversion(self):
        """测试监控点数整数转换"""
        params = AsianParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call',
            monitoring_points=12.0
        )
        assert isinstance(params.monitoring_points, int)
        assert params.monitoring_points == 12
    
    def test_asian_params_repr(self):
        """测试 AsianParams 的字符串表示"""
        params = AsianParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call',
            averaging_type='arithmetic',
            monitoring_points=12
        )
        repr_str = repr(params)
        assert 'AsianParams' in repr_str
        assert "averaging_type='arithmetic'" in repr_str
        assert 'monitoring_points=12' in repr_str
    
    def test_asian_params_equality(self):
        """测试 AsianParams 对象相等性"""
        params1 = AsianParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call',
            averaging_type='arithmetic',
            monitoring_points=12
        )
        params2 = AsianParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call',
            averaging_type='arithmetic',
            monitoring_points=12
        )
        assert params1 == params2
    
    def test_asian_params_inequality(self):
        """测试 AsianParams 对象不相等"""
        params1 = AsianParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call',
            averaging_type='arithmetic',
            monitoring_points=12
        )
        params2 = AsianParams(
            strike_price=100.0,
            time_to_maturity=0.25,
            option_type='call',
            averaging_type='geometric',
            monitoring_points=12
        )
        assert params1 != params2
