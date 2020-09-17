import qiskit as q
from qiskit.extensions import Initialize
from qiskit.quantum_info import random_statevector, Statevector
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from matplotlib import pyplot as plt


TELEPORT_QBIT = 0
A_QBIT = 1
B_QBIT = 2
QASM_BACKEND = q.Aer.get_backend('qasm_simulator')
STATE_VECTOR_BACKEND = q.Aer.get_backend('statevector_simulator')


def setup():
    # Protocol uses 3 qubits
    qr = q.QuantumRegister(3, name="q")
    # and 2 classical bits in 2 different registers
    crz = q.ClassicalRegister(1, name="crz")
    crx = q.ClassicalRegister(1, name="crx")
    teleportation_circuit = q.QuantumCircuit(qr, crz, crx)
    return qr, teleportation_circuit, crx, crz


def initialize_teleport_state(qc, tel_qbit, state):
    init_gate = Initialize(state)
    init_gate.label = "init"
    qc.append(init_gate, [tel_qbit])
    return qc


def create_bell_pair(qc, a, b):
    """Creates a bell pair in qc using qubits a & b"""
    qc.h(a)  # Put qubit a into state |+>
    qc.cx(a, b)  # CNOT with a as control and b as target
    return qc


def alice_bell_measurement(qc, psi, a):
    qc.cx(psi, a)
    qc.h(psi)
    return qc


def measure_and_send(qc, a, b, bit_a, bit_b):
    """Measures qubits a & b and 'sends' the results to Bob"""
    qc.measure(a, bit_a)
    qc.measure(b, bit_b)
    # results = q.execute(qc, M_BACKEND).result().get_counts()
    return qc


def bob_gates(qc, qubit, crz, crx):
    # Here we use c_if to control our gates with a classical
    # bit instead of a qubit
    # Applying order is based on theory
    # \sgima_x \sigma_z |state>_B
    qc.x(qubit).c_if(crx, 1)  # Apply gates if the registers
    qc.z(qubit).c_if(crz, 1)  # are in the state '1'
    return qc, crz, crx


def plot_teleport_state_vector(state_vector):
    # simple vector for single quibit has to be duplicated since plotting for sinqle quibit for some reason doesn't work
    state_vector = Statevector([state_vector[0] * state_vector[0], state_vector[0] * state_vector[1],
                                state_vector[1] * state_vector[0], state_vector[1] * state_vector[1]])
    plot_bloch_multivector(state_vector)


def main():
    qr, qc, crx, crz = setup()

    # initialize state to teleport
    vector_to_teleport = random_statevector(2)
    qc = initialize_teleport_state(qc, tel_qbit=TELEPORT_QBIT, state=vector_to_teleport.data)
    qc.barrier()

    # craete bell pair, as q1 and q2 where q1 shared with Alice and q2 with Bob
    qc = create_bell_pair(qc, a=A_QBIT, b=B_QBIT)

    # find i, j value (which bell states craetes pair q0 and q1 together), i is related to state (q0) and
    # j to Alice's entangeletn quibit q1
    qc.barrier()
    qc = alice_bell_measurement(qc, psi=TELEPORT_QBIT, a=A_QBIT)
    qc.barrier()

    # evaluate bell measurment of Alice's total state
    # measured values are stored in crz and crx
    qc = measure_and_send(qc, a=TELEPORT_QBIT, b=A_QBIT, bit_a=0, bit_b=1)

    # apply gates regards to teleportation protocol theory
    qc.barrier()
    qc, crz, crx = bob_gates(qc, B_QBIT, crz=crz, crx=crx)

    plot_teleport_state_vector(vector_to_teleport.data)

    out_vector = q.execute(qc, STATE_VECTOR_BACKEND).result().get_statevector()
    plot_bloch_multivector(out_vector)

    # qc.draw("mpl")
    plt.show()


if __name__ == "__main__":
    main()
