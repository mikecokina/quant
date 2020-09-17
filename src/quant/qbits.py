from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram
from qiskit.tools.visualization import plot_bloch_multivector
import qiskit as q
from math import sqrt, pi
from matplotlib import pyplot as plt


def first():
    qc = QuantumCircuit(1)
    initial_state = [0, 1]  # Define initial_state as |1>
    qc.initialize(initial_state, 0)  # Apply initialisation operation to the 0th qubit

    print(qc)

    backend = Aer.get_backend('statevector_simulator')  # Tell Qiskit how to simulate our circuit

    result = execute(qc, backend).result()  # Do the simulation, returning the result
    out_state = result.get_statevector()
    print(out_state)  # Display the output state vector

    qc.measure_all()
    print(qc)

    result = execute(qc, backend).result()
    counts = result.get_counts()
    plot_histogram(counts)
    plt.show()


def second():
    qc = QuantumCircuit(1)
    initial_state = [-1j/sqrt(2), 1j/sqrt(2)]
    qc.initialize(initial_state, 0)
    backend = Aer.get_backend('statevector_simulator')

    state = execute(qc, backend).result().get_statevector()
    print(state)

    backend = Aer.get_backend('qasm_simulator')
    qc.measure_all()
    print(qc)

    results = execute(qc, backend).result().get_counts()
    plot_histogram(results)
    plt.show()


def bloch_1():
    qc = q.QuantumCircuit(2)
    init = [1j/sqrt(2), 1j/sqrt(2)]
    qc.initialize(init, 0)
    backend = Aer.get_backend('statevector_simulator')

    state_vector = q.execute(qc, backend=backend).result().get_statevector()
    plot_bloch_multivector(state_vector)
    plt.show()


second()
