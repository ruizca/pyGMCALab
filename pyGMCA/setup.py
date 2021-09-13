# -\*- coding: utf-8 -\*-
r"""
setup.py - This file is part of pygmca.
The pygmca package aims at performing non-negative matrix factorization.
Copyright 2014 CEA
Contributor : Jérémy Rapin (jeremy.rapin.math@gmail.com)
Created on December 13, 2014, last modified on December 14, 2014

This software is governed by the CeCILL  license under French law and
abiding by the rules of distribution of free software.  You can  use,
modify and/ or redistribute the software under the terms of the CeCILL
license as circulated by CEA, CNRS and INRIA at the following URL
"http://www.cecill.info".

As a counterpart to the access to the source code and  rights to copy,
modify and redistribute granted by the license, users are provided only
with a limited warranty  and the software's author,  the holder of the
economic rights,  and the successive licensors  have only  limited
liability.

In this respect, the user's attention is drawn to the risks associated
with loading,  using,  modifying and/or developing or reproducing the
software by the user in light of its specific status of free software,
that may mean  that it is complicated to manipulate,  and  that  also
therefore means  that it is reserved for developers  and  experienced
professionals having in-depth computer knowledge. Users are therefore
encouraged to load and test the software's suitability as regards their
requirements in conditions enabling the security of their systems and/or
data to be ensured and,  more generally, to use and operate it in the
same conditions as regards security.

The fact that you are presently reading this means that you have had
knowledge of the CeCILL license and that you accept its terms.
"""
__version__ = "1.0"
__author__ = "Jeremy Rapin"
__url__ = "http://www.cosmostat.org/GMCALab.html"
__copyright__ = "(c) 2014 CEA"
__license__ = "CeCill"

from setuptools import setup, find_packages

# with open("README.rst", "r") as fh:
#     long_description = fh.read()

setup(
    name="pyGMCA",
    version="1.0",
    # author="Angel Ruiz",
    # author_email="angel.ruizca@gmail.com",
    description="pyGMCA",
    # long_description=long_description,
    # long_description_content_type="text/x-rst",
    url="https://github.com/ruizca/pyGMCA",
    install_requires=["numpy", "scipy", "matplotlib", "imageio"],
    #packages=find_packages(include=["pyGMCA", "pyGMCA.*"]),
    packages=find_packages(),
    # package_dir={"gdpyc": "gdpyc"},
    package_data={"pyGMCA": ["data/*"]},
)
