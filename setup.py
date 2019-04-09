from setuptools import setup, find_packages

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name="knotcloudwebsocket",
    version="0.1.0",
    author="KNoT",
    description="KNoT Cloud WebSocket library for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CESARBR/knot-cloud-websocket-python",
    packages=find_packages(),
    install_requires=[]
)