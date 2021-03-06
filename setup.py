from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='VidmaPy',
      version='0.0.1',
      description="Easy to use python access to Kurucz's SYNTHE/ATLAS codes",
      author="Tomasz Różański",
      author_email="tomasz.rozanski95@gmail.com",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/RozanskiT/vidmapy.git",
      packages=find_packages(exclude=["tests"]),
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        ],
      python_requires='>=3.5',
      include_package_data=True,
      package_data={'':['bin/*','grids/*','atomic_data/lines/*','atomic_data/molecules/*','atomic_data/ODF/NEW/*']},
)

# Way to install in develop mode
# python setup.py develop
# https://setuptools.readthedocs.io/en/latest/setuptools.html#development-mode

# or simply install
# python setup.py install