try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import ftoml

with open("README.md") as readme_file:
    readme_string = readme_file.read()

setup(
    name="ftoml",
    version=ftoml.__version__,
    description="Python library unifying f-strings with Tom's Obvious, Minimal Language",
    author="Florian Schüller",
    author_email="florian.schueller@gmail.com",
    url="https://github.com/schuellerf/ftoml",
    packages=['ftoml'],
    license="MIT",
    long_description=readme_string,
    python_requires=">=2.6, !=3.0.*, !=3.1.*, !=3.2.*",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
