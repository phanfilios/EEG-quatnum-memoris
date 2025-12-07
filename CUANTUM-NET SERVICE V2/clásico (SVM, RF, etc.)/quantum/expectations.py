from qiskit import Aer, transpile, execute

def get_expectation_values(qc, shots=512):

    backend = Aer.get_backend("qasm_simulator")
    compiled = transpile(qc, backend)
    job = execute(compiled, backend, shots=shots)
    return job.result().get_counts()