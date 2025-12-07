from qiskit import QuantumCircuit
import numpy as np

def eeg_to_quantum_state(vec):
   
    norm = np.linalg.norm(vec)
    if norm == 0:
        vec = np.zeros(len(vec))
        vec[0] = 1.0
    else:
        vec = vec / norm

    num_qubits = int(np.ceil(np.log2(len(vec))))
    qc = QuantumCircuit(num_qubits)
    qc.initialize(vec.tolist(), qc.qubits)
    return qc