import numpy as np

# def get_K(n, k0, combination, damage_bins, dof=8):
#     k = k0*np.ones(dof)
#     damaged_k_indices = combination
#     damaged_k = []
#     count=0
#     for i in damaged_k_indices:
#         _bin = damage_bins[count]
#         damage = 1 - np.round(np.random.uniform(_bin[0], _bin[1]), decimals=3)
#         damaged_k.append({
#             'index': i,
#             'damage' : damage,
#             'value' : np.round(damage*k[i], decimals=3),
#             'damage_bin': _bin,
#         })
#         k[i] = damage*k[i] 
#         count = count+1
#     return k


# k = 1e9 * np.ones(8)
# stiffness_data = get_K(3, k, (1,2,7), [[0.05, 0.1 ], [0.1 , 0.15], [0.9,0.95]])
# print(stiffness_data)
damage_proportion = np.arange(0.05, 0.95, 0.05)
damage_proportion_bins = np.array([(damage_proportion[i], damage_proportion[i+1]) for i in range(0, len(damage_proportion)-1)])
print((damage_proportion_bins))