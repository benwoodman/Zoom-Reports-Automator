from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zoomautomator", # Replace with your own username
    version="0.0.1",
    author="Ben Woodman",
    author_email="benwoodman101@gmail.com",
    description="Automate Zoom report download process.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/benwoodman/Zoom-Reports-Automator/",
    packages=setuptools.find_packages(),
    classifiers=[
        "MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "selenium"
    ],
    entry_points={
        'console_scripts': [
            'zoom-reports-automator = zoom_automator.run:start',
        ],
    },
)