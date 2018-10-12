# -*- coding: utf-8 -*-

# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

"""Aer Backends."""

from .aerprovider import AerProvider
from .aerjob import AerJob
from .qasm_simulator import QasmSimulator
from .statevector_simulator import StatevectorSimulator
from .unitary_simulator import UnitarySimulator

# Global instance to be used as the entry point for convenience.
Aer = AerProvider()  # pylint: disable=invalid-name
