import qiskit as q
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from matplotlib import pyplot as plt
from math import sqrt


qc = q.QuantumCircuit(2, 1)


def do():
    qc.draw('mpl')
    backend = q.Aer.get_backend('statevector_simulator')
    out = q.execute(qc, backend).result().get_statevector()
    plot_bloch_multivector(out)
    plt.show()


# NOT gate
def gate_x():
    qc.x(0)
    do()


def gate_y():
    qc.y(0)
    do()


def gate_z():
    qc.z(0)
    do()


def gate_hadamard():
    qc.h(0)
    do()


def gate_hadamard_rev():
    initial_state = [0, 1]
    qc.initialize(initial_state, 0)
    qc.h(0)
    do()


def eigen_x_plus():
    """
    init vector is qigenstate of X pauli matrix thus NOT gate do nothing on init vector
    """
    init = [1 / sqrt(2), 1 / sqrt(2)]
    qc.initialize(init, 0)
    qc.x(0)
    do()


def x_base(qbit):
    """Show 'qbit' value in the X-basis"""
    initial_state = [1 / sqrt(2), 1 / sqrt(2)]
    qc.initialize(initial_state, 0)

    qc.h(qbit)
    qc.z(qbit)
    qc.h(qbit)
    do()


def x_basis():
    def x_base_measuring(_qc, qbit):
        """
        Measure 'qubit' in the X-basis, and store the result in 'cbit'
        """

        _qc.h(qbit)
        _qc.measure(qbit, 0)
        _qc.h(qbit)

        return _qc

    _qc = q.QuantumCircuit(1, 1)
    # initialise qbit in state |1>
    initial_state = [0, 1]
    _qc.initialize(initial_state, 0)

    # measuremnt collapse qbit to state |+> or |-> (to superposition)
    __qc = x_base_measuring(_qc, 0)

    backend = q.Aer.get_backend('qasm_simulator')
    counts = q.execute(__qc, backend).result().get_counts()
    plot_histogram(counts)
    plt.show()


def r_phi_gate(phi):
    """
    R_z gate (rotate state around bloch Z axis about phi)
    """
    initial_state = [1 / sqrt(2), 1 / sqrt(2)]
    qc.initialize(initial_state, 0)

    qc.rz(phi, 0)
    do()


def i_gate():
    """
    Identity
    """
    initial_state = [1 / sqrt(2), 1 / sqrt(2)]
    qc.initialize(initial_state, 0)

    qc.i(0)
    do()


# x_basis()
# r_phi_gate(3.14 / 4)
i_gate()

