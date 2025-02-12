import numpy as np
from qiskit import QuantumCircuit, Aer, execute
qc = QuantumCircuit(8, 8)
Apply ry gates in loop for optimization
for qubit in range(4):
    qc.ry(np.pi/4, qubit)
    qc.cx(qubit, qubit+4)
qc.measure(range(8), range(8))
