from setuptools import setup, find_packages

# Чтение зависимостей из файла requirements.txt
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='Artemonim\'s_Educational-2025-Python',
    version='0.1',
    packages=find_packages(),
    install_requires=required,
)