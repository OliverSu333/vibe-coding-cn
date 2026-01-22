"""
测试项目目录结构是否正确创建
"""
import os
from pathlib import Path


def test_project_directories_exist():
    """测试项目目录是否存在"""
    base_dir = Path(__file__).parent.parent
    
    # 检查主要目录
    required_dirs = [
        'src',
        'tests',
        'docs',
        'memory-bank',
    ]
    
    for dir_name in required_dirs:
        dir_path = base_dir / dir_name
        assert dir_path.exists(), f"目录 {dir_name} 不存在"
        assert dir_path.is_dir(), f"{dir_name} 不是目录"


def test_src_subdirectories_exist():
    """测试 src 子目录是否存在"""
    base_dir = Path(__file__).parent.parent
    
    required_src_dirs = [
        'src/options',
        'src/pricing',
        'src/market_data',
        'src/numerical',
        'src/stochastic',
        'src/validation',
    ]
    
    for dir_path_str in required_src_dirs:
        dir_path = base_dir / dir_path_str
        assert dir_path.exists(), f"目录 {dir_path_str} 不存在"
        assert dir_path.is_dir(), f"{dir_path_str} 不是目录"


def test_init_files_exist():
    """测试 __init__.py 文件是否存在"""
    base_dir = Path(__file__).parent.parent
    
    required_init_files = [
        'src/options/__init__.py',
        'src/pricing/__init__.py',
        'src/market_data/__init__.py',
        'src/numerical/__init__.py',
        'src/stochastic/__init__.py',
        'src/validation/__init__.py',
        'tests/__init__.py',
        'tests/integration/__init__.py',
    ]
    
    for init_file_str in required_init_files:
        init_file = base_dir / init_file_str
        assert init_file.exists(), f"文件 {init_file_str} 不存在"


def test_required_files_exist():
    """测试必需文件是否存在"""
    base_dir = Path(__file__).parent.parent
    
    required_files = [
        'requirements.txt',
        '.gitignore',
    ]
    
    for file_name in required_files:
        file_path = base_dir / file_name
        assert file_path.exists(), f"文件 {file_name} 不存在"


def test_venv_exists():
    """测试虚拟环境目录是否存在"""
    base_dir = Path(__file__).parent.parent
    venv_path = base_dir / 'venv'
    
    # 虚拟环境可能还未创建，所以这个测试是可选的
    # 如果存在，检查是否是目录
    if venv_path.exists():
        assert venv_path.is_dir(), "venv 不是目录"
