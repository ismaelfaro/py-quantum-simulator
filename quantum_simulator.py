import random
from math import cos,sin,pi

r2=0.70710678118 # 1/sqrt(2)

class QuantumCircuit:
    def __init__(self, qubits):
        if (qubits == 0):
            print('Number of Qubits need to ne more than 0')
        self.Qubits = qubits
        self.Bits = qubits
        self.circuit = []
    
    def add_gate(self, gate):
        self.circuit.append(gate)
    
    def x(self, qubit):
        self.add_gate(['x',qubit])

    def z(self, qubit):
        self.rz(qubit,pi) 

    def y(self, qubit):
        self.rz(qubit,pi)
        self.x(qubit)

    def h(self, qubit):
        self.add_gate(['h',qubit])

    def cx(self, qubit, target):
        self.add_gate(['cx',qubit,target])

    def rx(self, qubit, theta):
        self.add_gate(['rx',qubit, theta])
    
    def ry(self, qubit, theta):
        self.rx(qubit,pi/2)
        self.h(qubit)
        self.rx(qubit,theta)
        self.h(qubit)
        self.rx(qubit,-pi/2)

    def rz(self, qubit, theta):
        self.h(qubit)
        self.rx(qubit,theta)
        self.h(qubit)

    def m(self, qubit, target):
        self.add_gate(['m',qubit,target])

    def __repr__(self):
        return str(self.circuit)
class QuantumSimulator:
    pass

if __name__ == "__main__":
    print("Quantum Simulator for Developers project")
    qc = QuantumCircuit(5)
    qc.x(0)
    
    qc.x(1)
    qc.x(0)
    qc.x(2)
    qc.z(0)
    qc.x(0)
    
    qc.h(2)
    qc.h(0)
    qc.h(1)
    
    qc.cx(0,1)
    qc.cx(0,1)
    qc.m(0,0)

    print(qc)
    # print(qc.circuit)
    
    # quantumSimulator =  QuantumSimulator(qc)
    # stateVector = quantumSimulator.run("statevector")
    # print(stateVector)
    # result = quantumSimulator.run("counts", 1024)
    # print(result)
    pass