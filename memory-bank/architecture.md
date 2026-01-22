# 项目架构文档

## 目录结构

```
项目根目录/
├── src/                          # 源代码目录
│   ├── options/                  # 期权类型模块
│   │   ├── __init__.py
│   │   ├── option.py            # 期权抽象基类
│   │   ├── option_params.py     # 期权参数类
│   │   ├── vanilla_option.py    # Vanilla 期权
│   │   ├── digital_option.py    # Digital 期权
│   │   ├── barrier_option.py    # Barrier 期权
│   │   └── asian_option.py      # Asian 期权
│   ├── pricing/                  # 定价方法模块
│   │   ├── __init__.py
│   │   ├── pricing_method.py   # 定价方法抽象基类
│   │   ├── monte_carlo.py       # 蒙特卡洛方法
│   │   ├── pde.py               # PDE 方法
│   │   └── black_scholes.py     # Black-Scholes 解析解
│   ├── market_data/              # 市场数据模块
│   │   ├── __init__.py
│   │   └── market_data.py       # 市场数据类
│   ├── numerical/                # 数值计算模块
│   │   ├── __init__.py
│   │   └── finite_difference.py # 有限差分求解器
│   ├── stochastic/               # 随机过程模块
│   │   ├── __init__.py
│   │   └── gbm.py               # 几何布朗运动
│   ├── validation/               # 验证模块
│   │   ├── __init__.py
│   │   └── validator.py         # 验证器
│   └── pricing_engine.py        # 统一定价接口
├── tests/                        # 测试目录
│   ├── test_market_data.py
│   ├── test_option_params.py
│   ├── test_gbm.py
│   ├── test_option_base.py
│   ├── test_vanilla_option.py
│   ├── test_digital_option.py
│   ├── test_barrier_option.py
│   ├── test_asian_option.py
│   ├── test_pricing_method_base.py
│   ├── test_monte_carlo.py
│   ├── test_pde_base.py
│   ├── test_finite_difference.py
│   ├── test_pde.py
│   ├── test_validator.py
│   ├── test_black_scholes.py
│   ├── test_pricing_engine.py
│   └── integration/             # 集成测试
│       ├── test_integration.py
│       └── test_performance.py
├── docs/                         # 文档目录
│   └── examples.md              # 使用示例
├── memory-bank/                  # 项目上下文文档
│   ├── project-context.md
│   ├── implementation-plan.md
│   ├── progress.md
│   ├── architecture.md
│   └── tech-stack.md
├── requirements.txt              # Python 依赖
├── README.md                     # 项目说明
└── .gitignore                    # Git 忽略文件
```

## 模块说明

### 期权类型模块（src/options/）

**职责**：定义各种期权类型及其参数

- `option.py`: 期权抽象基类，定义统一的期权接口
- `option_params.py`: 期权参数类，封装不同期权的特定参数
- `vanilla_option.py`: 标准期权实现
- `digital_option.py`: 二元期权实现
- `barrier_option.py`: 障碍期权实现
- `asian_option.py`: 亚式期权实现

### 定价方法模块（src/pricing/）

**职责**：实现各种数值定价方法

- `pricing_method.py`: 定价方法抽象基类
- `monte_carlo.py`: 蒙特卡洛定价方法
- `pde.py`: 偏微分方程定价方法
- `black_scholes.py`: Black-Scholes 解析解（用于验证）

### 市场数据模块（src/market_data/）

**职责**：管理市场数据（标的价格、波动率、利率等）

- `market_data.py`: 市场数据类，提供数据验证和访问

### 数值计算模块（src/numerical/）

**职责**：提供数值计算工具

- `finite_difference.py`: 有限差分求解器（显式、隐式、Crank-Nicolson）

### 随机过程模块（src/stochastic/）

**职责**：模拟随机过程

- `gbm.py`: 几何布朗运动路径生成

### 验证模块（src/validation/）

**职责**：验证定价结果的正确性

- `validator.py`: 验证器，提供与解析解对比、方法对比、收敛性测试等功能

### 统一定价接口（src/pricing_engine.py）

**职责**：提供统一的定价接口，简化用户使用

## 设计模式

- **策略模式**：定价方法（MC、PDE）作为可替换的策略
- **工厂模式**：期权对象的创建（可选）
- **模板方法模式**：定价流程的统一框架
- **抽象基类**：Option 和 PricingMethod 作为抽象接口

## 数据流

```
用户输入
  ↓
期权参数 + 市场数据
  ↓
期权对象创建（Option）
  ↓
定价方法选择（PricingMethod）
  ↓
数值计算执行
  ↓
定价结果 + 验证报告
  ↓
用户输出
```

## 关键设计决策

（在此记录重要的设计决策和原因）

## 架构洞察

### 步骤 1 完成后的洞察
- 项目采用模块化目录结构，每个功能模块独立目录
- 使用 __init__.py 文件使目录成为 Python 包
- 测试目录结构与源代码目录结构对应，便于维护
- 集成测试单独放在 tests/integration/ 目录

### 步骤 2 完成后的洞察
- 虚拟环境已创建，项目依赖隔离良好
- requirements.txt 明确记录了所有依赖及版本要求
- 项目结构测试验证了目录创建的正确性
- 后续开发需要在激活虚拟环境后进行

### 步骤 3 完成后的洞察
- MarketData 类采用值对象（Value Object）设计模式，确保数据不可变性和一致性
- 参数验证在构造函数中完成，遵循"快速失败"原则，及早发现错误
- 使用私有方法（_validate_*）封装验证逻辑，提高代码可维护性
- 数值类型自动转换（int 转 float），提高接口的易用性
- 测试覆盖全面，包括正常情况、边界值、异常情况和类型验证
- 模块导出清晰，通过 __init__.py 统一管理公共接口

### 步骤 4 完成后的洞察
- OptionParams 采用继承层次结构，基类定义通用属性，子类扩展特定属性，符合开闭原则
- 使用抽象基类（ABC）作为基类，虽然当前未定义抽象方法，但为未来扩展预留接口
- 参数验证逻辑复用：基类的 _validate_positive 方法被子类复用，减少代码重复
- BarrierParams 设计考虑了实际金融需求：支持 knock-out/in、barrier level、monitoring frequency 等完整属性
- 向后兼容性设计：BarrierParams 保留 barrier_price 和 barrier_type 作为别名，确保旧代码仍可使用
- 监控频率的灵活设计：支持连续监控（'continuous'）和离散监控（正整数），满足不同定价方法的需求
- 类型转换策略：自动将 int 转换为 float（数值参数），将 float 转换为 int（整数参数），提高易用性
- 测试覆盖全面：54 个测试用例覆盖所有参数类、所有属性、边界值和异常情况
- 命名规范统一：使用清晰的英文命名（barrier_level、barrier_direction、knock_type），符合金融术语习惯

---

## 文件职责说明

### 步骤 1-2 完成后的文件

#### 项目根目录文件
- `requirements.txt`: Python 项目依赖管理文件，包含 numpy、scipy、pytest 等依赖及版本要求
- `README-option-pricing.md`: 期权定价器项目的说明文档，包含项目介绍、安装说明、使用示例（待补充）
- `.gitignore`: Git 版本控制忽略文件配置（已存在，包含 Python 相关忽略规则）

#### 源代码目录（src/）
- `src/options/__init__.py`: 期权类型模块的包初始化文件
- `src/pricing/__init__.py`: 定价方法模块的包初始化文件
- `src/market_data/__init__.py`: 市场数据模块的包初始化文件
- `src/numerical/__init__.py`: 数值计算模块的包初始化文件
- `src/stochastic/__init__.py`: 随机过程模块的包初始化文件
- `src/validation/__init__.py`: 验证模块的包初始化文件

#### 测试目录（tests/）
- `tests/__init__.py`: 测试模块的包初始化文件
- `tests/integration/__init__.py`: 集成测试模块的包初始化文件
- `tests/test_project_structure.py`: 项目结构验证测试，验证目录和文件是否正确创建

#### 文档目录（docs/）
- 目前为空，后续将存放使用示例和项目文档

#### 虚拟环境（venv/）
- Python 虚拟环境目录，用于隔离项目依赖
- 已创建但依赖安装因网络问题暂未完成

### 步骤 3 完成后的文件

#### 市场数据模块（src/market_data/）
- `src/market_data/market_data.py`: MarketData 类的实现，提供市场数据存储和验证功能
  - 职责：封装市场数据（标的价格、波动率、无风险利率、股息率）
  - 功能：参数验证、默认值处理、数据访问
  - 设计：值对象模式，确保数据一致性和不可变性
- `src/market_data/__init__.py`: 市场数据模块的包初始化文件，导出 MarketData 类

#### 测试目录（tests/）
- `tests/test_market_data.py`: MarketData 类的单元测试
  - 测试覆盖：参数验证、默认值处理、类型转换、对象相等性、边界值
  - 测试用例数：12 个
  - 测试状态：全部通过

### 步骤 4 完成后的文件

#### 期权参数模块（src/options/）
- `src/options/option_params.py`: 期权参数类的实现，提供所有期权类型的参数封装
  - 职责：封装不同期权类型的特定参数，提供统一的参数验证和访问接口
  - 功能：
    - OptionParams 基类：定义通用参数（执行价格、到期时间、期权类型）和验证逻辑
    - VanillaParams：标准期权参数（无额外属性）
    - DigitalParams：二元期权参数（无额外属性）
    - BarrierParams：障碍期权参数，包含 barrier_level、barrier_direction、knock_type、monitoring_frequency
    - AsianParams：亚式期权参数，包含 averaging_type、monitoring_points
  - 设计：
    - 继承层次结构，基类定义通用属性，子类扩展特定属性
    - 参数验证在构造函数中完成，遵循"快速失败"原则
    - 使用私有方法（_validate_*）封装验证逻辑，提高代码可维护性
    - 类型自动转换（int 转 float，float 转 int），提高接口易用性
    - BarrierParams 保持向后兼容性（barrier_price 和 barrier_type 作为别名）
- `src/options/__init__.py`: 期权类型模块的包初始化文件，导出所有参数类

#### 测试目录（tests/）
- `tests/test_option_params.py`: 期权参数类的单元测试
  - 测试覆盖：所有参数类的创建、参数验证、类型转换、对象相等性、边界值、异常情况
  - 测试用例数：54 个
  - 测试状态：全部通过
