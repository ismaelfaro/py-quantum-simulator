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

    def cx(self, control, target):
        self.add_gate(['cx',control, target])

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

    def superposition(self, x, y):
        return [[r2*(x[0]+y[0]),r2*(x[1]+y[1])],
                [r2*(x[0]-y[0]),r2*(x[1]-y[1])]]
    
    def turn(self, x, y, theta):
        part1 = [x[0]*cos(theta/2)+y[1]*sin(theta/2),x[1]*cos(theta/2)-y[0]*sin(theta/2)]
        part2 = [y[0]*cos(theta/2)+x[1]*sin(theta/2),y[1]*cos(theta/2)-x[0]*sin(theta/2)]
        return [ part1, part2]
    
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
                            self.state_vector[qb0], self.state_vector[qb1] = self.state_vector[qb1], self.state_vector[qb0]
                            
                        if gate[0]=='h':
                            superpositionResult = self.superposition(self.state_vector[qb0],self.state_vector[qb1])
                            self.state_vector[qb0] = superpositionResult[0]
                            self.state_vector[qb1] = superpositionResult[1]

                        if gate[0]=='rx':
                            theta = gate[2]
                            turn = self.turn(self.state_vector[qb0],self.state_vector[qb1],theta)
                            self.state_vector[qb0] = turn[0]
                            self.state_vector[qb1] = turn[1]

            elif gate[0] == 'cx':
                control = gate[1]
                target = gate[2]

                [low,high] = sorted([control,target])
         
                for cx0 in range(2**low):
                    limit_cx2 = 2**(high-low-1)
                    for cx1 in range(limit_cx2):
                        for cx2 in range(2**(self.Qubits-high-1)):
                            qb0 = cx0 + 2**(low+1)*cx1 + 2**(high+1)*cx2 + 2**control  
                            qb1 = qb0 + 2**target 
                            self.state_vector[qb0],self.state_vector[qb1] = self.state_vector[qb1],self.state_vector[qb0]
                           
    def __repr__(self):
        return str(self.state_vector)

if __name__ == "__main__":
    print("Quantum Simulator for Developers project")
    qc = QuantumCircuit(5)
    qc.x(0)
    qc.x(1)
    qc.rx(0,pi)
    qc.x(2)
    qc.z(0)
    # qc.x(0)
    
    qc.h(0)
    qc.h(1)

    # qc.h(1)
    
    qc.cx(0,1)
    qc.cx(1,0)
    # qc.m(0,0)

    print(qc)
    
    quantumSimulator =  QuantumSimulator(qc)
    quantumSimulator.run()
    print(quantumSimulator)
    # result = quantumSimulator.run("counts", 1024)
    # print(result)
    pass