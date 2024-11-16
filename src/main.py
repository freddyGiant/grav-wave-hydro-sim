import numpy as np

class Simulation:
    def __init__(self, n_r, n_theta, r_max, density, dt):
        '''
        Args:
            n_r (int): \# rectangles radial
            n_theta (int): \# rectangles angular
            r_max (float): radius of simulated area
            dt (float): time step
        '''
        self._n_r = n_r
        self._n_theta = n_theta
        self._r_max = r_max
        self._dt = dt
        
        self._r = np.linspace(0, r_max, n_r)
        self._theta = np.linspace(0, 2 * np.pi, n_theta)
        
        self._dr = r_max / n_r
        self._dtheta = 2 * np.pi / n_theta
        
        self._v_r = np.zeros((n_r, n_theta))
        self._v_theta = np.zeros((n_r, n_theta))
        
        self._density = density

def main():
    sim = Simulation(5, 8, 10e9, 1)

if __name__ == '__main__':
    main()