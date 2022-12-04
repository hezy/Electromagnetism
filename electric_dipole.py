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



def plc_V(q, R, x, y, x0, y0):
# the potential at x,y of a point like charge q at x0,y,0
    k = 9E9
    V = k*q/np.hypot((x-x0),(y-y0))
    return V


def plc_Ex(q, x, y, x0, y0):
# the x componenet of the field at x,y, of a point like charge q at x0,y,0
    k = 9E9
    Ex = k*q*(x-x0)/(np.hypot((x-x0),(y-y0)))**3
    return Ex


k = 9E9
# physical parameters
q1 = 1E-9
R1 = 0.1
x1, y1  = -0.3, 0
q2 = -1E-9
R2 = 0.1
x2, y2  = 0.3, 0

# The potential
V = plc_V(q1, R1, x, y, x1, y1) + plc_V(q2, R2, x, y, x2, y2)

# Plotting the potential
plt.contourf(x,y,V, levels=300, cmap='seismic', vmin=-150, vmax=150)
plt.colorbar(label='Electrical potential [$V$]')
plt.title('Electrical potential of a dipole')
plt.xlabel('Horizontal position [m]')
plt.ylabel('Vertical position [m]')
plt.show()


# The electric field (theory)
Ex = plc_Ex(q1, x, y, x1, y1) + plc_Ex(q2, x, y, x2, y2)
Ey = plc_Ex(q1, y, x, y1, x1) + plc_Ex(q2, y, x, y2, x2)

E = np.hypot(Ex, Ey)
cos = Ex/E
sin = Ey/E

E_max = 500
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

E_max_ = 500
E_[E_>E_max_] = E_max_
E_[E_<-E_max_] = -E_max_

# Plotting the electric field (claculated)
plt.quiver(x, y, cos_, sin_, E_, pivot='mid')
plt.colorbar(label='Electrical field [V/m]')
plt.title('Electrical field of a dipole (calculated)')
plt.xlabel('Horizontal position [m]')
plt.ylabel('Vertical position [m]')
plt.show()
