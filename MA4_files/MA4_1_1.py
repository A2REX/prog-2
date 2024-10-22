
"""
Solutions to module 4
Review date:
"""

student = "Albion Rexhaj"
reviewer = ""


import random as r
import matplotlib.pyplot as plt 
import math

def approximate_pi(n):
    nc = 0
    points_x_cr = []
    points_y_cr = []
    points_x_sq = []
    points_y_sq = []
    for i in range(n):
        x = r.uniform(-1, 1)
        y = r.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            nc += 1
            points_x_cr.append(x)
            points_y_cr.append(y)
        else:
            points_x_sq.append(x)
            points_y_sq.append(y)
    pi = 4*nc/n
    print(f'Number of points inside circle for {n} points: {nc}')
    print(f'Approximation of pi for {n} points: {4*nc/n}', end='\n\n')
    ax = plt.subplot()
    ax.plot(points_x_cr, points_y_cr, '.', color='red')
    ax.plot(points_x_sq, points_y_sq, '.', color='blue')
    ax.set(title = f'Randomized points with n = {n}')
    plt.show()
    return pi
    
def main():
    print(f'Real value of pi: {math.pi}', end='\n\n')
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)

if __name__ == '__main__':
	main()
