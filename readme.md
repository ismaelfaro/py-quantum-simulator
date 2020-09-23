# Py Quantum Simulator 

This is a very basic implementation of a Quantum Simulator in Python to learn the basic component.
Allow to create your Quantum circuits with the basic Quantum Gates, and you can execute it using plain python

# Components
- Quantum Circuit Class:
    - Quantum Gates: x, rx, ry, rz, z, y, h, cx, m
- Quanrtum Simulator Class: 
    - imput: Qcircuit
    - outputs: 
        - statevector
        - counts
        - memory

# Example:
'''
    print('Quantum Simulator for Developers project')
    qc = QuantumCircuit(5)
    qc.h(0)
    qc.x(1)
    qc.rx(2,pi)
    qc.z(0)
    qc.h(1)
    qc.cx(0,1)
    qc.cx(1,0)
    qc.m(0,0)

    print('\ncircuit:') 
    print(qc)
    
    print('\nsimulate and show state_vector:') 
    quantumSimulator =  QuantumSimulator(qc)
    result = quantumSimulator.run()
    print(result)

    print('\nsimulate 1024 shots and show the counts:') 
    result = quantumSimulator.run(1024, "counts")
    print(result)       
'''

# TODO:
- Import Open Quasm 2.0
- create a basic visual interface to create circuits and understand "how work" a quantum executions.
- Integrate with https://github.com/JavaFXpert/grok-bloch bloch sphere visualization
- Integrate with https://github.ibm.com/Ismael-Faro1/box-phase-visualization

# references
Inspired in MicroQiskit python implementation https://github.com/qiskit-community/MicroQiskit by James Wootton
