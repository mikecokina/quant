from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram
from matplotlib import pyplot as plt

n = 8
n_q = n
n_b = n
qc_output = QuantumCircuit(n_q, n_b)

qc_encode = QuantumCircuit(n)
qc_encode.x(7)

qc = qc_encode + qc_output

for j in range(n):
    qc.measure(j, j)

qc.draw(output="mpl")

counts = execute(qc, backend=Aer.get_backend('qasm_simulator'), shots=1024).result().get_counts()
plot_histogram(counts)
plt.show()
