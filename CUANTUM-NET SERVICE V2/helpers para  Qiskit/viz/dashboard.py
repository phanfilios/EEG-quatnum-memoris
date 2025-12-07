import warnings

try:
    # qiskit modern import
    from qiskit import Aer
    HAS_AER = True
except Exception:
    HAS_AER = False
    warnings.warn("Qiskit Aer backend no disponible. Algunas funciones cuánticas pueden fallar.")

from qiskit import execute
from qiskit.providers.aer import AerSimulator
from qiskit.quantum_info import Statevector

def get_simulator_backend():
    """Devuelve un backend de simulación. Intenta Aer, si no falla devuelve None."""
    if HAS_AER:
        try:
            return Aer.get_backend("aer_simulator")
        except Exception:
            try:
                return AerSimulator()
            except Exception:
                return None
    return None

def run_circuit_and_counts(qc, shots=512):
    backend = get_simulator_backend()
    if backend is None:
        # fallback: intentar obter statevector y construir conteos simples
        sv = Statevector.from_instruction(qc)
        # convertir statevector a prob de 0/1 en primer qubit (ejemplo simple)
        probs = (abs(sv.data)**2).tolist()
        return {"statevector_probs_len": len(probs), "probs_sample": probs[:8]}
    job = execute(qc, backend, shots=shots)
    res = job.result()
    counts = res.get_counts()
    return counts