import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="personalnames",
    version="0.0.2",
    author="Matt McGrattan",
    author_email="matt.mcgrattan@digirati.com",
    description="Generate variant forms for personal names.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/digirati-co-uk/personalnames",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
