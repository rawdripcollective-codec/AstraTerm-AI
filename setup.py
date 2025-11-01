from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_file = Path(__file__).parent / "README.md"
long_description = ""
if readme_file.exists():
    long_description = readme_file.read_text(encoding="utf-8")

setup(
    name="astraterm-ai",
    version="1.2.0",
    author="AstraTerm Team",
    author_email="contact@astraterm.dev",
    description="AI-Powered Terminal with Security Tools Integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/astraterm/astraterm-ai",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Topic :: System :: Shells",
        "Topic :: Terminals",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "textual>=0.40.0",
        "rich>=13.0.0",
        "prompt-toolkit>=3.0.0",
        "requests>=2.31.0",
        "python-nmap>=0.7.1",
    ],
    extras_require={
        "ai": [
            "openai>=1.0.0",
            "anthropic>=0.7.0",
        ],
        "osint": [
            "shodan",
        ],
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "astraterm=astraterm.main:run_app",
            "astraterm-ai=astraterm.main:run_app",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="terminal, ai, security, osint, pentesting, hacking, tools",
    project_urls={
        "Bug Reports": "https://github.com/astraterm/astraterm-ai/issues",
        "Source": "https://github.com/astraterm/astraterm-ai",
        "Documentation": "https://astraterm.dev/docs",
    },
)
