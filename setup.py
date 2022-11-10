import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="effectzigbee",
    version="0.0.2",
    author="Antonin Alves",
    author_email="antonin@alors-la.fr",
    description="E-ffect Zigbee",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/antonin-alves/effect-zigbee",
    project_urls={
        "Bug Tracker": "https://github.com/antonin-alves/effect-zigbee/issues"
    },
    license="",
    packages=["effectzigbee"],
    install_requires=["pyserial"],
)
