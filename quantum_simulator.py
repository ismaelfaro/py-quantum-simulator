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
    def __init__(self, quantum_circuit):
        self.circuit = quantum_circuit.circuit
        self.Qubits =  quantum_circuit.Qubits
        self.Bits =  self.Qubits
        self.state_vector = []
    
    def initialize_state_vector(self):
        self.state_vector = [[0.0,0.0] for _ in range(2**self.Qubits)] 
        self.state_vector[0] = [1.0,0.0] 

    def superposition(self,x,y):
        return [[r2*(x[0]+y[0]),r2*(x[1]+y[1])],
                [r2*(x[0]-y[0]),r2*(x[1]-y[1])]]
    
    def run(self, shots=1024, format="statevector"):
        self.initialize_state_vector()
        for gate in self.circuit:
            if gate[0] in ['x','h','rx']:
                qubit = gate[1]
                for counter_qubit in range(2**qubit):
                    for counter_state in range(2**(self.Qubits-qubit-1)):
                        qb0=counter_qubit+(2**qubit+1)*counter_state
                        qb1=qb0+(2**qubit)
                        if gate[0]=='x':
                            temp = self.state_vector[qb0]
                            self.state_vector[qb0] = self.state_vector[qb1]
                            self.state_vector[qb1] = temp
                        if gate[0]=='h':
                            superpositionResult = self.superposition(self.state_vector[qb0],self.state_vector[qb1])
                            self.state_vector[qb0] = superpositionResult[0]
                            self.state_vector[qb1] = superpositionResult[1]

                print(gate[0])
            elif gate[0] == 'cx':
                print(gate[0])

    def __repr__(self):
        return str(self.state_vector)

if __name__ == "__main__":
    print("Quantum Simulator for Developers project")
    qc = QuantumCircuit(5)
    qc.x(0)
    qc.x(1)
    # qc.x(0)
    # qc.x(2)
    # qc.z(0)
    # qc.x(0)
    
    qc.h(1)
    # qc.h(0)
    # qc.h(1)
    
    # qc.cx(0,1)
    # qc.cx(0,1)
    # qc.m(0,0)

    print(qc)
    
    quantumSimulator =  QuantumSimulator(qc)
    quantumSimulator.run()
    print(quantumSimulator)
    # result = quantumSimulator.run("counts", 1024)
    # print(result)
    pass