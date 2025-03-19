from setuptools import setup, find_packages

setup(
    name="morse_code_converter",
    version="0.1.0",
    author="Byte Busters",
    description="A Python package to convert text to Morse code and vice versa.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/orgs/software-students-spring2025/teams/bytebusters",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
    "sounddevice>=0.4.6",
    "numpy>=2.2.4",
    "pytest",
    ],
    keywords="morse code converter text",
    project_urls={
        "Documentation": "https://github.com/orgs/software-students-spring2025/teams/bytebusters#readme",
        "Bug Tracker": "https://github.com/orgs/software-students-spring2025/teams/bytebusters/issues",
    },
)