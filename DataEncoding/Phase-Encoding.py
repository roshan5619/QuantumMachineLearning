import math
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from math import pi

qc = QuantumCircuit(1)
qc.h(0)  # Hadamard gate rotates state down to Bloch equator
state1 = Statevector.from_instruction(qc)

qc.p(pi / 2, 0)  # Phase gate rotates by an angle pi/2
state2 = Statevector.from_instruction(qc)

states = state1, state2

qc.draw("text", scale=1)