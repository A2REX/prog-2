
"""
Solutions to module 4
Review date:
"""

student = "Albion Rexhaj"
reviewer = ""

import math as m
import random as r

def sphere_volume(n, d):
    nc = 0
    n_tot = 0
    for i in range(n):
        coor = [r.uniform(-1, 1) for dim in range(d)]
        if sum(list(map(lambda a : a**2, coor))) <= 1:
            nc += 1
        n_tot += 1
    return 2**d*nc/n_tot

def hypersphere_exact(n, d):
    return m.pi**(d/2)/m.gamma(d/2+1)
     
def main():
    n = 100000
    d = 2
    print(f'Computed volume: {sphere_volume(n,d)}')
    print(f'Exact volume: {round(hypersphere_exact(n, d), 5)}')

if __name__ == '__main__':
	main()
