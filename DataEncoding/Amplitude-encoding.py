import math
import numpy as np
from qiskit import QuantumCircuit
desired_state = [
    1 / math.sqrt(105) * 4,
    1 / math.sqrt(105) * 8,
    1 / math.sqrt(105) * 5,
    1 / math.sqrt(105) * 0,
]

qc = QuantumCircuit(2)
qc.initialize(desired_state, [0, 1])

qc.decompose(reps=5).draw(output="text")