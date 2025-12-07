from qiskit import QuantumCircuit

def build_full_quantum_model(embedded_state: QuantumCircuit):

    qc = embedded_state.copy()
    num_qubits = qc.num_qubits

    for i in range(num_qubits - 1):
        qc.cx(i, i + 1)

    return qc