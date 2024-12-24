from setuptools import setup, find_packages
with open("requirements.txt") as f:
    install_requires = f.read().splitlines()
setup(
    name = 'byteff',  
    version = '0.0.1',
    keywords = ['byteff'],
    description = 'byteff source code.',
    license = 'Apache License 2.0',
    author="Bytedance Inc.",
    author_email="zhengtianze@bytedance.com,wen.yan@bytedance.com",
    packages=find_packages(
        exclude=(
            "data",
            "scripts",
            "tests"
        )
    ),
    include_package_data=True,
    data_files=["requirements.txt"],
    platforms = 'manylinux1',
    install_requires = install_requires,
)
