# Quantum Tunneling Simulation
A quantum tunneling simulation across a double-well potential using a 4-qubit register in Qiskit. It models the evolution of a quantum wavefunction under a custom Hamiltonian and uses the Quantum Fourier Transform to analyze energy dynamics. 
Built by Cole McLaren and Dan Griffith. 

# Features
- 4-Qubit register quantum state simulation (16 spatial positions)
- Custom Hamiltonian representing a double-well potential: `V = a(x² - b²)²`
- Quantum Fourier Transform (QFT) and Inverse QFT for kinetic energy operations
- Custom quantum gates:
  - D-Gate: momentum evolution with Z and Phi phase rotations
  - Q-Gate: position-based potential application
- Tunneling behaviour visualized via probability distribution over time

# Technologies Used
- Python
- Qiskit
- NumPy
- Matplotlib

# How To Run
1. Setup Environment
   - Creating a clean python environment to avoid version conflicts is recommended.
   - Set this up in same directory that Quantum Simulation.py file is in:
     - python3 -m venv qiskit-env
2. Activate Environment
   - On Mac/Linux:
     - source qiskit-env/bin/activate
   - On Windows:
     - qiskit-env\Scripts\activate
3. Installed Required Packages
     - pip install qiskit numpy matplotlib
     - (if errors with pip, use pip3 install qiskit numpy matplotlib)
4. Run Simulation
   - To run simulation once environment is created, simply run:
     - python3 Quantum_Simulation_Tunneling.py

Once running, 
