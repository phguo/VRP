from setuptools import setup


with open("README.md", 'r') as readme:
    long_description = readme.read()

setup(
    name="PyVRP",
    version="0.0.2",
    description="A Python package for plotting Vehicle Routing Problem (VRP) solutions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GPL-3.0",
    url="https://github.com/phguo/PyVRP",

    author="Penghui Guo",
    author_email="m@guo.ph",

    packages=["pyvrp"],
    install_requires=["matplotlib"]
)
