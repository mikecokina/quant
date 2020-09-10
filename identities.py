import qiskit as q
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from matplotlib import pyplot as plt
from math import sqrt
import numpy as np


qc = q.QuantumCircuit(2, 2)
t = 1
c = 0


def ry_controller():
    qc.x(0)

    theta = np.pi / 4
    qc.ry(theta/2, t)
    qc.cx(c, t)
    qc.ry(-theta / 2, t)
    qc.cx(c, t)

    statevector_backend = q.Aer.get_backend('statevector_simulator')
    final_state = q.execute(qc, statevector_backend).result().get_statevector()
    plot_bloch_multivector(final_state)
    plt.show()


ry_controller()
