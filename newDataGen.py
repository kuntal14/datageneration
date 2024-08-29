import numpy as np
import matplotlib.pyplot as plt
# from scipy.linalg import eigh
from newmark import newmark_method
from modal_analysis import modal_analysis
from NewGenK import get_K
from scipy.special import comb
import pandas as pd
import json
from Combinations import generate_combinations

# Parameters
dt = 0.5
T_start = 0
T_end = 20
t = np.arange(T_start, T_end + dt, dt)
nt = len(t)

# Structural Properties
dof = 8
M = 625e3 * np.eye(dof)
k = 1e9 * np.ones(dof)

# Simulate Damage
alpha0 = 100
data = []

# number of damaged points
damage_condn = 3

# get the combinations for a particular damage condition
k_indices = np.arange(0,8)
combinations = generate_combinations(k_indices, damage_condn)

json_filename = f"data{damage_condn}.jsonl"

# now we generate the data for singly damage condn
for combination in combinations:
    # we generate 10 data per bin per condition
    damage_proportion = np.arange(0.05, 0.95, 0.05)
    damage_proportion_bins = np.array([(damage_proportion[i], damage_proportion[i+1]) for i in range(0, len(damage_proportion)-1)])
    
    # interate over each damage_bin
    for damage_bin in damage_proportion_bins:

        # generate 10 simulations for each damage condition and a particular damage bin
        for i in range (10):
            stiffness_data = get_K(damage_condn, k, combination, damage_bin)
            K = stiffness_data['K']
            ki = stiffness_data['k']

            # Define Force
            F = np.random.randn(nt, dof).T
            F[0, :] = 0

            # Damping
            C = 0.1 * M + 0.1 * K

            # Modal Analysis
            Mn, Kn, Cn, Fn, phi, W = modal_analysis(M, K, C, F, dof)

            # Newmark Time Integration
            acceleration = 'Linear'
            depl, vel, accl = newmark_method(M, K, C, F, dof, acceleration, dt, nt)
            data_node = {
                'k' : ki.tolist(),
                'K' : K.tolist(),
                'degree_of_damage': damage_condn,
                'degree_of_freedom' : dof,
                'depl' : depl.tolist(),
                'vel' : vel.tolist(),
                'accl' : accl.tolist(),
                'dt': dt
            }
            with (open(json_filename, 'a')) as json_file:
                json_file.write(json.dumps(data_node) + '\n')
