# Py Quantum Simulator 

This is a very basic implementation of a Quantum Simulator in Python to learn the basic component.
Allow to create your Quantum circuits with the basic Quantum Gates, and you can execute it in Nodejs or in your browser in a simple way.

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
    // Create your quantum circuit with 5 Qubits
    qc = new Qcircuit(5)
    qc.x(0);
    qc.rx(0,2);
    qc.x(1)
    qc.x(0)
    qc.x(2)
    qc.z(0)
    qc.x(0)
    
    qc.h(2)
    qc.h(0)
    qc.h(1)
    
    qc.cx(0,1);
    qc.cx(0,1);
    qc.m(0,0);
    
    print(qc.circuit);
    
    // use the quantum simulator
    qsimulator = new Qsimulator(qc)
    statevector = qsimulator.run("statevector")
    console.log(statevector)
    counts = qsimulator.run("counts", 1024)
    console.log(counts)


# TODO:
- Import Open Quasm 2.0
- create a basic visual interface to create circuits and understand "how work" a quantum executions.
- Integrate with https://github.com/JavaFXpert/grok-bloch bloch sphere visualization
- Integrate with https://github.ibm.com/Ismael-Faro1/box-phase-visualization

# references
Inspired in MicroQiskit python implementation https://github.com/qiskit-community/MicroQiskit by James Wootton