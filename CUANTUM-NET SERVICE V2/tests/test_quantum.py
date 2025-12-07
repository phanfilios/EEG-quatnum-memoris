from qiskit import QuantumCircuit
from quantum.utils import run_circuit_and_counts

def test_qc_simulation_basic():
    qc = QuantumCircuit(1)
    qc.h(0)
    res = run_circuit_and_counts(qc, shots=32)
    assert res is not None