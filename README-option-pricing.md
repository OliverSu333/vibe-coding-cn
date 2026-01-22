# 期权定价器 (Option Pricing Engine)

一个支持多种期权类型和定价方法的 Python 期权定价引擎。

## 功能特性

- 支持多种期权类型：Vanilla、Digital、Barrier、Asian
- 支持多种定价方法：蒙特卡洛方法（MC）、偏微分方程方法（PDE）
- 模块化设计，易于扩展
- 完整的测试覆盖

## 安装

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
```

## 使用示例

（待补充）

## 项目结构

```
option-pricing-engine/
├── src/                    # 源代码
├── tests/                  # 测试代码
├── docs/                   # 文档
└── memory-bank/            # 项目上下文文档
```

## 开发

运行测试：
```bash
pytest tests/ -v
```

生成测试覆盖率报告：
```bash
pytest --cov=src tests/
```

## 许可证

（待补充）
