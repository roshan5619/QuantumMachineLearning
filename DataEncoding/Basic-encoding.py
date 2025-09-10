import math
import numpy as np
from qiskit import QuantumCircuit

desired_state = [1 / math.sqrt(3), 0, 0, 0, 0, 1 / math.sqrt(3), 0, 1 / math.sqrt(3)]

qc = QuantumCircuit(3)
qc.initialize(desired_state, [0, 1, 2])
qc.decompose(reps=8).draw(output="text")