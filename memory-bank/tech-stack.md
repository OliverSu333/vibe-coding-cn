# 技术栈文档

## 编程语言

- **Python 3.8+**
  - 原因：项目要求全部使用 Python 实现
  - 版本要求：3.8 及以上（支持类型提示和现代特性）

## 核心依赖库

### NumPy
- **版本**：>= 1.20.0
- **用途**：
  - 数值计算和数组操作
  - 随机数生成
  - 向量化计算优化
- **安装**：`pip install numpy>=1.20.0`

### SciPy
- **版本**：>= 1.7.0
- **用途**：
  - 科学计算工具（如需要）
  - 三对角矩阵求解
  - 统计函数
- **安装**：`pip install scipy>=1.7.0`
- **说明**：主要用于 PDE 方法的矩阵求解

## 测试框架

### pytest
- **版本**：>= 7.0.0
- **用途**：
  - 单元测试
  - 集成测试
  - 测试覆盖率报告
- **安装**：`pip install pytest>=7.0.0 pytest-cov`
- **使用**：`pytest tests/ -v --cov=src`

## 开发工具

### 虚拟环境
- **工具**：Python venv 或 conda
- **用途**：项目依赖隔离
- **创建**：`python -m venv venv`

### 代码质量工具（可选）
- **pylint** 或 **flake8**：代码规范检查
- **mypy**：类型检查（如果使用类型提示）

### Git
- **用途**：版本控制
- **说明**：用于代码版本管理和协作

## 可选优化工具

### Numba（未来考虑）
- **用途**：JIT 编译加速数值计算
- **适用场景**：MC 方法的热点代码优化

### Cython（未来考虑）
- **用途**：将 Python 代码编译为 C 扩展
- **适用场景**：性能关键路径优化

## 依赖管理

### requirements.txt
```
numpy>=1.20.0
scipy>=1.7.0
pytest>=7.0.0
pytest-cov>=3.0.0
```

## 开发环境设置

1. 创建虚拟环境：`python -m venv venv`
2. 激活虚拟环境：
   - Linux/Mac: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate`
3. 安装依赖：`pip install -r requirements.txt`

## 技术选型理由

- **NumPy**：Python 数值计算的标准库，性能优秀，API 成熟
- **SciPy**：提供科学计算工具，特别是矩阵求解功能
- **pytest**：Python 最流行的测试框架，功能强大，易于使用
- **纯 Python 实现**：满足项目要求，便于维护和扩展

## 未来扩展考虑

- **Numba**：如果 MC 方法性能成为瓶颈，可以考虑使用 Numba 加速
- **JAX**：如果需要 GPU 加速或自动微分，可以考虑 JAX
- **QuantLib**：可以作为参考实现或底层库（但不符合纯 Python 要求）
