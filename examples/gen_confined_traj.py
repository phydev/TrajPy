import trajpy.traj_generator as tjg
import numpy as np
"""
    generate N confined trajectories for each value of diffusion coefficient
"""

n_steps = 250  # number of time steps
n_samples = 1  # number of trajectories
dt = 1.0  # time increment
radius = np.array([5., 10., 20.])
D = 100.

for value in radius:

    xa, ya = tjg.confined_diffusion(value, n_steps, n_samples, 1.0, 0.0, D, dt)

    for n in range(0, n_samples):
        np.savetxt('data/confined/trj' + str(np.round(value, decimals=1)) + str(n) + '.csv', ya[:, n], delimiter=",",
                   header='m')
        print(np.round(value, decimals=2), n)