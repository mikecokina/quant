import qiskit as q
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from matplotlib import pyplot as plt
from math import sqrt
import numpy as np


qc = q.QuantumCircuit(2, 2)


def superpos_two():
    qc.h(0)
    qc.h(1)
    qc.cx(0, 1)

    qc.measure(0, 0)
    qc.measure(1, 1)
    backend = q.Aer.get_backend('qasm_simulator')
    results = q.execute(qc, backend).result().get_counts()
    plot_histogram(results)
    plt.show()


def rev_superpos_cnot():
    qc.h(0)

    qc.x(1)
    qc.h(1)
    qc.cx(0, 1)

    qc.measure(0, 0)
    qc.measure(1, 1)

    backend = q.Aer.get_backend('qasm_simulator')
    results = q.execute(qc, backend).result().get_counts()
    plot_histogram(results)
    plt.show()


def phase_kickback():
    """
    example of phase kickback

    output is same as application qc.cx(1, 0) w/o all Hadamard;s gates

    1 0 0 0
    0 1 0 0
    0 0 0 1
    0 0 1 0
    """
    qc.h(0)
    qc.h(1)
    qc.cx(0, 1)
    qc.h(0)
    qc.h(1)

    backend = q.Aer.get_backend('unitary_simulator')
    results = q.execute(qc, backend).result().get_unitary()
    print(np.round(np.real(results), 1))


def controlerd_t_gate():
    qc.h(0)
    qc.cu1(0, 1)

    qc.measure(0, 0)
    qc.measure(1, 1)

    backend = q.Aer.get_backend('qasm_simulator')
    results = q.execute(qc, backend).result().get_counts()
    plot_histogram(results)
    plt.show()


def controled_t_gate_bloch():
    qc.h(0)
    qc.x(1)

    # Add Controlled-T
    qc.cu1(np.pi / 4, 0, 1)

    statevector_backend = q.Aer.get_backend('statevector_simulator')
    final_state = q.execute(qc, statevector_backend).result().get_statevector()
    plot_bloch_multivector(final_state)
    plt.show()


def controled_sdg_gate_bloch():
    qc.h(0)
    qc.x(1)

    # Add controlled-Sdg gate
    qc.cu1(-np.pi / 2, 0, 1)

    statevector_backend = q.Aer.get_backend('statevector_simulator')
    final_state = q.execute(qc, statevector_backend).result().get_statevector()
    plot_bloch_multivector(final_state)
    plt.show()


controled_sdg_gate_bloch()

















