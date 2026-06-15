.. highlight:: bash

.. _install:

Install app4triqs
*******************

``app4triqs`` is a python-only TRIQS application skeleton. It is installed
from source — there are no PyPI/conda binaries — into the same Python
environment as your TRIQS install. Two source-install paths are supported;
both are equally valid, pick whichever fits your workflow.

.. note:: To guarantee reproducibility in scientific calculations we strongly
   recommend the use of a stable
   `release <https://github.com/TRIQS/triqs/releases>`_ of both TRIQS and its
   applications.

Prerequisites
=============

#. The :ref:`TRIQS <triqslibs:welcome>` library, see
   :ref:`TRIQS installation instructions <triqslibs:triqs_install>`.
   In the following, we assume that TRIQS is installed in the directory
   ``path_to_triqs`` and that you have sourced its environment::

     $ source path_to_triqs/share/triqs/triqsvars.sh

.. _install_pip:

Install from source via pip (recommended)
=========================================

::

    $ git clone https://github.com/TRIQS/app4triqs
    $ pip install -e ./app4triqs

Drop ``-e`` for a non-editable install. ``pip`` resolves the runtime Python
dependencies declared in ``pyproject.toml`` automatically.

This path does **not** install the lmod modulefile, the ``vars.sh`` shell
script, or the CMake config files needed for ``find_package(app4triqs)``;
use the CMake path below if you need any of those.

.. _install_cmake:

Install from source via CMake
=============================

::

    $ git clone https://github.com/TRIQS/app4triqs app4triqs.src
    $ cmake -S app4triqs.src -B app4triqs.build -GNinja
    $ ninja -C app4triqs.build
    $ ninja -C app4triqs.build test
    $ ninja -C app4triqs.build install

The default install prefix is ``$TRIQS_ROOT``; override with
``-DCMAKE_INSTALL_PREFIX=...``. CMake does **not** install the runtime Python
dependencies — install them yourself into the same Python environment with
``pip`` (see ``pyproject.toml`` for the list).

Version compatibility
=====================

The major and minor version of ``app4triqs`` must match your installed TRIQS
library; see the :ref:`TRIQS website <triqslibs:versions>`. The CMake
configure step enforces this and hard-fails on mismatch; with ``pip`` it is
your responsibility to install a compatible version.

To use a particular version, list available tags::

    $ cd app4triqs && git tag

then check out the desired tag::

    $ git checkout 2.1.0

and re-run the install step from your chosen path above.

Custom CMake options
====================

These options apply only to the :ref:`CMake install path <install_cmake>`.
Pass them when configuring::

    cmake -S app4triqs.src -B build -DOPTION1=value1 -DOPTION2=value2 ...

+-----------------------------------------------------------------+-----------------------------------------------+
| Options                                                         | Syntax                                        |
+=================================================================+===============================================+
| Specify an installation path other than ``$TRIQS_ROOT``         | ``-DCMAKE_INSTALL_PREFIX=path_to_app4triqs``  |
+-----------------------------------------------------------------+-----------------------------------------------+
| Build in Debugging Mode                                         | ``-DCMAKE_BUILD_TYPE=Debug``                  |
+-----------------------------------------------------------------+-----------------------------------------------+
| Disable testing (not recommended)                               | ``-DBuild_Tests=OFF``                         |
+-----------------------------------------------------------------+-----------------------------------------------+
| Build the documentation                                         | ``-DBuild_Documentation=ON``                  |
+-----------------------------------------------------------------+-----------------------------------------------+
