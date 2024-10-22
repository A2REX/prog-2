
"""
Solutions to module 4
Review date:
"""

student = "Albion Rexhaj"
reviewer = ""

import math as m
import random as r
from time import perf_counter as pc
import concurrent.futures as future

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

def help_func(n, d):
    return [sphere_volume(n, d) for _ in range(10)]

# parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np):
    #using multiprocessor to perform 10 iterations of volume function
    with future.ProcessPoolExecutor() as ex:
        results = ex.map(help_func, [n//10]*np, [d]*np)
    results = [r for sublist in list(results) for r in sublist]
    results = sum(results)/len(results)
    return results

# parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np):
    with future.ProcessPoolExecutor() as ex:
        results = ex.map(sphere_volume, [n//np]*np, [d]*np)
    results = list(results)
    results = sum(results)/len(results)
    return results

def main():
    # part 1 -- parallelization of a for loop among 10 processes 
    n = 100000
    d = 11
    np = 10
    
    print(f'Exact solution: {round(hypersphere_exact(n, d), 3)}', end='\n\n')
    
    start = pc()
    for _ in range (10):
        sphere_volume(n,d)
    end = pc()
    print(f"Normal process took {round(end-start, 2)} seconds")
    
    start = pc()
    vol1 = sphere_volume_parallel1(n, d, np)
    end = pc()
    print(f"Parallel process took {round(end-start, 2)} seconds")
    print(f'Computed volume of parallel1: {round(vol1, 3)}')
    print('---------')
    
    start = pc()
    sphere_volume(n,d)
    end = pc()
    print(f"Normal process took {round(end-start, 2)} seconds")
    
    start = pc()
    vol2 = sphere_volume_parallel2(n//10, d, np)
    end = pc()
    print(f"Parallel process took {round(end-start, 2)} seconds")
    print(f'Computed volume of parallel2: {round(vol2, 3)}')
    

if __name__ == '__main__':
	main()
