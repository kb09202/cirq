from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# Circuit avec 3 qubits et 3 bits classiques
qc = QuantumCircuit(3,3)

# Création état GHZ
qc.h(0)       # Hadamard sur qubit 0
qc.cx(0,1)    # CNOT qubit 0 -> 1
qc.cx(1,2)    # CNOT qubit 1 -> 2

# Mesure
qc.measure([0,1,2],[0,1,2])

# Simulation
sim = Aer.get_backend('qasm_simulator')
result = execute(qc, sim, shots=1024).result()
counts = result.get_counts()
print("Résultats GHZ 3 qubits :", counts)

# Optionnel : afficher histogramme
plot_histogram(counts)