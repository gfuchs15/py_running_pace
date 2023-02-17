import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyrunpace",
    version="0.0.1",
    author="Guillaume Fuchs",
    author_email="guillaume.fuchs@gmail.com",
    description="Compute pace and speed from time and distance.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gfuchs15/py_running_pace",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
    ],
    license="MIT",
    python_requires=">=3.7",
)
