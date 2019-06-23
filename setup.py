import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="big-num-format",
    version="0.1.4",
    scripts=[],
    author="MBmasher",
    author_email="mbmasher@gmail.com",
    description="A package to convert very large numbers into human readable text.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MBmasher/big-num-format",
    packages=["big_num_format"],
    package_dir={"big_num_format":"big_num_format"},
    package_data={
        "":["README.md"],
        "big_num_format":["*.txt"]
        },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
