# 项目架构文档

## 文件职责说明

### 步骤 1 完成后的文件

- `requirements.txt`: 项目依赖管理文件，定义了核心运行时依赖（numpy, scipy）和开发依赖（pytest, black, mypy）
- `pyproject.toml`: 现代 Python 项目配置文件，包含项目元数据、构建系统配置、开发工具配置（black 格式化、mypy 类型检查、pytest 测试配置）
- `src/pricing_tool/__init__.py`: 主包初始化文件，定义了包的版本号和基本信息，作为整个定价工具包的入口点
- `tests/__init__.py`: 测试模块初始化文件
- `tests/test_project_structure.py`: 项目结构验证测试文件，用于确保项目基础结构正确创建

## 架构洞察

### 步骤 1 完成后的洞察

- **项目结构设计**：采用标准的 Python 项目布局（src/、tests/、docs/），符合 Python 最佳实践，便于代码组织和维护
- **包管理策略**：使用 pyproject.toml 作为现代 Python 项目的标准配置文件，替代传统的 setup.py，提供更灵活的配置方式
- **依赖管理**：将依赖分为核心依赖（numpy, scipy）和开发依赖（pytest, black, mypy），便于不同环境下的依赖安装
- **开发工具集成**：在 pyproject.toml 中配置了 black（代码格式化）、mypy（类型检查）、pytest（测试框架），确保代码质量和一致性
- **模块化设计基础**：主包目录 `src/pricing_tool/` 为后续模块化开发奠定了基础，便于后续添加 options、pricing、engine、utils 等子模块
- **测试驱动开发**：从一开始就建立了测试目录和测试文件，体现了测试驱动开发的理念，确保项目结构可验证
