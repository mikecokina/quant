from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram
from matplotlib import pyplot as plt


def simple_xor_circuit(n0, n1):
    qc_output = QuantumCircuit(2, 2)
    qc_encode = QuantumCircuit(2)

    for i, bit_i in enumerate([n0, n1]):
        if bit_i:
            qc_encode.x(i)

    qc_encode.cx(0, 1)
    qc = qc_encode + qc_output
    qc.draw(output="mpl")
    return qc


def simple_xor_circuit_evaluate(n0, n1):
    print(f"evaluating binary number {n1}{n0}")
    qc = simple_xor_circuit(n0, n1)
    for j in range(2):
        qc.measure(j, j)

    counts = execute(qc, backend=Aer.get_backend('qasm_simulator'), shots=256).result().get_counts()
    plot_histogram(counts)
    plt.show()


def add_circuit(n0, n1):
    qc_add = QuantumCircuit(4, 2)

    # switch initialized 0 to desired 1 if presented on input
    for i, bit_i in enumerate([n0, n1]):
        if bit_i:
            qc_add.x(i)

    # sum table
    #               AND   XOR
    # 0 + 0 = 00  -> 0  |  0
    # 0 + 1 = 01  -> 0  |  1
    # 1 + 0 = 01  -> 0  |  1
    # 1 + 1 = 10  -> 1  |  0
    # this snippet will do flip of 2 qbit if 0 is 1 and as well as if qbit 1 is equal 1
    #  0 + 0 -> no flip of 2nd qbit = 0
    #  0 + 1 -> flip of 2nd qbit    = 1
    #  1 + 0 -> flip of 2nd qbit    = 1
    #  1 + 1 -> flip 2nd qbit twice = 0
    qc_add.barrier()
    qc_add.cx(0, 2)
    qc_add.cx(1, 2)

    # this part solves an AND
    # trigger NOT on 3rd qbit if 0th and 1st are 1
    qc_add.ccx(0, 1, 3)
    qc_add.barrier()

    return qc_add


def add(n0, n1):
    qc = add_circuit(n0, n1)
    qc.measure(2, 0)
    qc.measure(3, 1)

    counts = execute(qc, backend=Aer.get_backend('qasm_simulator'), shots=256).result().get_counts()

    qc.draw(output="mpl")
    plot_histogram(counts)
    plt.show()


if __name__ == "__main__":
    add(1, 1)

