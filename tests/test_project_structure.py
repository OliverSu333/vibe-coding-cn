"""
测试项目基础结构是否正确
"""

import sys
from pathlib import Path


def test_project_structure():
    """测试项目目录结构是否正确创建"""
    # 检查必要的目录是否存在
    assert Path("src").exists(), "src 目录不存在"
    assert Path("tests").exists(), "tests 目录不存在"
    assert Path("docs").exists(), "docs 目录不存在"
    assert Path("src/pricing_tool").exists(), "src/pricing_tool 目录不存在"
    
    # 检查必要的文件是否存在
    assert Path("requirements.txt").exists(), "requirements.txt 文件不存在"
    assert Path("pyproject.toml").exists(), "pyproject.toml 文件不存在"
    assert Path("src/pricing_tool/__init__.py").exists(), "src/pricing_tool/__init__.py 文件不存在"
    
    # 检查是否可以导入主包
    sys.path.insert(0, str(Path(__file__).parent.parent))
    import pricing_tool
    assert pricing_tool.__version__ == "0.1.0", "版本号不正确"
    
    print("✅ 项目基础结构测试通过")


if __name__ == "__main__":
    test_project_structure()
