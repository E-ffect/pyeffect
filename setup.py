import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyeffect",
    version="0.0.4",
    author="Antonin Alves",
    author_email="antonin@alors-la.fr",
    description="E-ffect Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/antonin-alves/pyeffect",
    project_urls={"Bug Tracker": "https://github.com/antonin-alves/pyeffect/issues"},
    license="",
    packages=["pyeffect"],
    install_requires=["pyserial"],
)
