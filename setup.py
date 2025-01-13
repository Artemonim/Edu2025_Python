# Try to import from setuptools
# If can't, then install setuptools with pip
try:
    from setuptools import setup, find_packages
except ImportError:
    import subprocess
    import sys
    # Install setuptools
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'setuptools'])
    from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='Artemonim\'s_Educational-2025-Python',
    version='0.1',
    packages=find_packages(),
    install_requires=required,
)