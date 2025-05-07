from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT, Diagonal
from qiskit.quantum_info import Statevector
import numpy as np
import matplotlib.pyplot as plt

# Constants
N_qubits = 4
delta_t = 0.01
steps = 200
state_vector = np.ones(16, dtype=complex) / np.sqrt(16)
initial_state = Statevector(state_vector)

# Build one time-step circuit
qc = QuantumCircuit(N_qubits)

# Step 1: QFT
qft = QFT(num_qubits=N_qubits)
qc.append(qft, range(N_qubits))

# Step 2: D gate (Z and Φ phases)
theta_z = [np.pi**2 / (4 ** (N_qubits - k)) for k in range(N_qubits)]
phi_pairs = [(3,2), (3,1), (3,0), (2,1), (2,0), (1,0)]
theta_phi = [np.pi**2 / (2**i) for i in range(1, 7)]

D_diag = []
for i in range(2 ** N_qubits):
    b = f"{i:04b}"
    z_phase = sum(theta_z[k] for k in range(N_qubits) if b[3 - k] == '1')
    phi_phase = sum(theta for (c, t), theta in zip(phi_pairs, theta_phi)
                    if b[3 - c] == '1' and b[3 - t] == '1')
    D_diag.append(np.exp(-1j * (z_phase + phi_phase) * delta_t))

qc.append(Diagonal(D_diag), range(N_qubits))

# Step 3: Inverse QFT
qc.append(QFT(num_qubits=N_qubits, inverse=True), range(N_qubits))

# Step 4: Q gate (potential)
a = 50
b = 0.5
positions = np.linspace(-1, 1, 16)
V = a * (positions**2 - b**2)**2
V = V.tolist()

Q_diag = [np.exp(-1j * v * delta_t) for v in V]
qc.append(Diagonal(Q_diag), range(N_qubits))

# --- Simulate Evolution ---
evolution = qc
for _ in range(steps - 1):
    evolution = evolution.compose(qc)

final_state = initial_state.evolve(evolution)
max_V = max(V)
V_scaled = [v / max_V for v in V]

# --- Plot Result ---
probs = np.abs(final_state.data) ** 2
states = [f"{i:04b}" for i in range(2 ** N_qubits)]

plt.figure(figsize=(10, 6))

# Create the bar plot for probabilities
bars = plt.bar(states, probs, color='blue', alpha=0.7, label="Quantum Probability")

# Plot the energy potential function V as a curve, scaled to the same range as the probabilities
plt.plot(states, V_scaled, color='green', label="Scaled Potential Energy", linewidth=2)

# Add labels and title
plt.xlabel("Basis States (Position)")
plt.ylabel("Probability / Scaled Energy")
plt.title(f"Tunneling After {steps} Steps (from superposition at each basis state)")
plt.xticks(rotation=45)
plt.grid(True, axis='y')

# Add a legend to distinguish between the energy function and quantum probability
plt.legend()

plt.tight_layout()
plt.show()
