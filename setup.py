import os
from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=[
        "numpy==1.26.0",
    ],
    python_requires='>=3.8',
    author="Jiawei Zhang",
    description="A math quiz package",
    long_description=open('README.md').read() if os.path.exists('README.md') else "",
    long_description_content_type="text/markdown",
    url="https://github.com/Leon42325/dsss_homework_2",

)
