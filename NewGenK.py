import numpy as np

# Simulate Damage
# Number of defected Regions

def get_K(n, k0, combination, damage_bin, dof=8):
    k = k0*np.ones(dof)
    damaged_k_indices = combination
    damaged_k = []
    for i in damaged_k_indices:
        _bin = damage_bin
        damage = 1 - np.round(np.random.uniform(_bin[0], _bin[1]), decimals=3)
        damaged_k.append({
            'index': i,
            'damage' : damage,
            'value' : np.round(damage*k[i], decimals=3),
            'damage_bin': _bin,
        })
        k[i] = damage*k[i] 

    K = np.zeros((dof, dof))
    for i in range(dof - 1):
        K[i, i] += k[i] + k[i + 1]
        K[i, i + 1] = -k[i + 1]
        K[i + 1, i] = -k[i + 1]
    K[dof - 1, dof - 1] = k[dof - 1]

    return {
        'K' : K,
        'k' : k,
        'damaged_indices': damaged_k_indices,
        'degree_of_damage' : n,
        'damaged_k_list' : damaged_k
    }

if __name__ == "__main__":
    print(get_K(2, 1e9, [1], [0.5, 1])['K'])
