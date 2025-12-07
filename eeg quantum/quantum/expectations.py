from qiskit import Aer, execute

def get_expectation_values(qc):
    backend = Aer.get_backend("qasm_simulator")
    job = execute(qc, backend, shots=512)
    res = job.result().get_counts()
    return res