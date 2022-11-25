# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt


# setting up the grid
sx = np.linspace(-1.2, 1.2, 24)
sy = np.linspace(-1, 1, 20)
x, y = np.meshgrid(sx,sy)
dx = x[0,1] - x[0,0]
dy = y[1,0] - y[0,0]

# physical parameters
k = 9E9
q1 = 1E-9
x1, y1  = -0.3, 0
q2 = -1E-9
x2, y2  = 0.3, 0

# The potential
V = (k*q1/np.sqrt((x-x1)**2+(y-y1)**2) + 
     k*q2/np.sqrt((x-x2)**2+(y-y2)**2))

# Plotting the potential
plt.contourf(x,y,V, levels=300, cmap='seismic', vmin=-150, vmax=150)
plt.colorbar(label='Electrical potential [$V$]')
plt.title('Electrical potential of a dipole')
plt.xlabel('Horizontal position [m]')
plt.ylabel('Vertical position [m]')
plt.show()


# The electric field (theory)
Ex = (k*q1*(x-x1)/((x-x1)**2+(y-y1)**2)**(3/2) +
      k*q2*(x-x2)/((x-x2)**2+(y-y2)**2)**(3/2))

Ey = (k*q1*(y-y1)/((x-x1)**2+(y-y1)**2)**(3/2) +
      k*q2*(y-y2)/((x-x2)**2+(y-y2)**2)**(3/2))

E = np.hypot(Ex, Ey)
cos = Ex/E
sin = Ey/E

E_max = 400
E[E>E_max] = E_max
E[E<-E_max] = -E_max

# Plotting the electric field (theory)
plt.quiver(x, y, cos, sin, E, pivot='mid')
plt.colorbar(label='Electrical field [$V/m$]')
plt.title('Electrical field of a dipole (theory)')
plt.xlabel('Horizontal position [m]')
plt.ylabel('Vertical position [m]')
plt.show()


# Calculating the electric field from the potential
Ey_, Ex_ = np.gradient(V, dy, dx)
Ex_ = -1 * Ex_
Ey_ = -1 * Ey_

E_ = np.hypot(Ex, Ey)
cos_ = Ex_/E_
sin_ = Ey_/E_

E_max_ = 400
E_[E_>E_max_] = E_max_
E_[E_<-E_max_] = -E_max_

# Plotting the electric field (claculated)
plt.quiver(x, y, cos_, sin_, E_, pivot='mid')
plt.colorbar(label='Electrical field [V/m]')
plt.title('Electrical field of a dipole (calculated)')
plt.xlabel('Horizontal position [m]')
plt.ylabel('Vertical position [m]')
plt.show()
