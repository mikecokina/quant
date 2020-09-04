import qiskit as q
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from matplotlib import pyplot as plt
from math import sqrt
import numpy as np


qc = q.QuantumCircuit(2, 2)


def first():
    qc.i(0)
    qc.i(1)
    backend = q.Aer.get_backend('unitary_simulator')
    u = q.execute(qc, backend).result().get_unitary()
    print(u)


def unitary():
    qc.h(0)
    qc.x(1)
    backend = q.Aer.get_backend('unitary_simulator')
    u = q.execute(qc, backend).result().get_unitary()
    print(u)


def unitary_01():
    qc.initialize([1, 0], 0)
    qc.initialize([0, 1], 1)
    qc.i(0)
    qc.i(1)
    backend = q.Aer.get_backend('unitary_simulator')
    u = q.execute(qc, backend).result().get_unitary()
    print(u)

    qc.draw('mpl')
    plt.show()


def unitary_xi():
    """
    this is weird - requires investigation
    """
    # qc.initialize([1, 0], 0)
    qc.initialize([0, 1], 1)

    qc.i(0)
    qc.x(1)

    backend = q.Aer.get_backend('unitary_simulator')
    u = q.execute(qc, backend).result().get_unitary()
    print(np.round(np.real(u), 1))

    qc.draw('mpl')
    plt.show()


def superpos_cnot():
    qc.h(0)
    qc.cx(0, 1)

    qc.draw()

    backend = q.Aer.get_backend('statevector_simulator')
    final_state = q.execute(qc, backend).result().get_statevector()

    print(final_state)
    plt.show()


def superpos_cnot_prob():
    qc.h(0)
    qc.cx(0, 1)

    qc.measure(0, 0)
    qc.measure(1, 1)
    backend = q.Aer.get_backend('qasm_simulator')
    results = q.execute(qc, backend).result().get_counts()
    plot_histogram(results)
    plt.show()


superpos_cnot_prob()
