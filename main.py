import qiskit as q
from matplotlib import pyplot as plt
from qiskit import IBMQ
from qiskit.tools.monitor import job_monitor
from qiskit.visualization import plot_histogram
from matplotlib import style
from qiskit import Aer


def get_token():
    with open("token", "r") as f:
        return f.readline().strip()


def circuit_1():
    access_token = get_token()
    # circuit = q.QuantumCircuit(2, 2)  # 2 quibits, 2 classical bits?????
    circuit = q.QuantumCircuit(2)  # 2 quibits

    # Pauli X matrix
    # gate NOT applied to quibit zero (0)
    # initial state 0, 0
    # apply NOT on first quibit will gives us 1, 0 state
    circuit.x(0)
    # cnot (controlled NOT)
    # flips second quibit value IF first quibit is a 1
    # QuantumCircuit.cx(control_qubit, target_qubit, ...)
    # other words, if qbit on first position (qbit 0) is 1 then switch value of target qbit (qbit 1) to 1
    # after this operation from previous state (1, 0) we should have state (1, 1)
    circuit.cx(0, 1)
    # measurment
    circuit.measure_all()
    # plot circuit
    # circuit.draw(output="mpl")
    # plt.show()

    # save credentials to ~/.qiskit/qiskitrc
    # IBMQ.save_account(access_token)
    IBMQ.load_account()
    access_provider = IBMQ.get_provider()

    # for backend in access_provider.backends():
    #     try:
    #         qbit_count = len(backend.properties().qubits)
    #     except Exception as e:
    #         qbit_count = 'simulated'
    #
    #     print(f"{backend.name()} has {backend.status().pending_jobs} queued and {qbit_count} qbits")

    # backend = access_provider.get_backend("ibmq_essex")
    backend = access_provider.get_backend("ibmq_qasm_simulator")
    job = q.execute(circuit, backend=backend, shots=500)
    job_monitor(job)
    result = job.result()
    counts = result.get_counts(circuit)

    plot_histogram([counts])
    plt.show()


def circuit_2():
    circuit = q.QuantumCircuit(2)  # 2 quibits
    # h - superposion of qbit
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.measure_all()
    IBMQ.load_account()
    access_provider = IBMQ.get_provider()

    backend = access_provider.get_backend("ibmq_qasm_simulator")
    job = q.execute(circuit, backend=backend, shots=500)
    job_monitor(job)
    result = job.result()
    counts = result.get_counts(circuit)

    plot_histogram([counts])
    plt.show()


def circuit_2_local():
    circuit = q.QuantumCircuit(2)  # 2 quibits
    # h - superposion of qbit
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.measure_all()

    # state_vector, unitary_simulator, qasm_simulator
    backend = Aer.get_backend("qasm_simulator")
    job = q.execute(circuit, backend=backend, shots=500)
    job_monitor(job)
    result = job.result()
    counts = result.get_counts(circuit)

    plot_histogram([counts])
    plt.show()


if __name__ == "__main__":
    style.use("dark_background")
    # circuit_1()
    circuit_2_local()
