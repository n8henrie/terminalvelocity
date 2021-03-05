from setuptools import find_packages, setup

setup(
    name="terminalvelocity",
    version="0.2.0",
    author="Nathan Henrie",
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": ["tv=terminalvelocity.cli:run"],
    },
    url="https://github.com/n8henrie/terminalvelocity/",
    license="MIT",
    description="A fast note-taking app for the UNIX terminal",
    long_description=open("README.md").read(),
    install_requires=open("requirements.txt").read().splitlines(),
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
