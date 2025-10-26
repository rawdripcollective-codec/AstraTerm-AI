from setuptools import setup, find_packages

setup(
    name="astraterm-ai",
    version="1.2.0",
    packages=find_packages(),
    install_requires=["textual", "prompt_toolkit", "requests", "python-nmap"],
    entry_points={"console_scripts": ["astraterm-ai = astraterm.main:run_app"]},
)
