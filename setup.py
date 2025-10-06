from setuptools import setup, find_packages

setup(
    name="ukrainian-syllable-splitter",
    version="0.1.0",
    author="Anastasiia Mozghova",
    description="Package that splits Ukrainian words into syllables",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/anastasiia-mozg/Ukrainian-Syllable-Splitter",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
