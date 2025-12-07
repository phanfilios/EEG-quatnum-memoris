from qiskit import QuantumCircuit
import numpy as np

def eeg_to_quantum_state(features, num_qubits=100):
    vector = np.array(features)

    if len(vector) < num_qubits:
        padded = np.pad(vector, (0, num_qubits - len(vector)))
    else:
        padded = vector[:num_qubits]

    qc = QuantumCircuit(num_qubits)

    for i, val in enumerate(padded):
        angle = float(val) % (2 * np.pi)
        qc.ry(angle, i)

    return qc