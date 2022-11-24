# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt

_ = np.linspace(-1, 1, 91)
x, y = np.meshgrid(_,_)

k = 9E9
q1 = 1E-9
x1, y1  = -0.3, 0
q2 = 1E-9
x2, y2  = 0.3, 0
V = k*q1/np.sqrt((x-x1)**2+(y-y1)**2) - k*q2/np.sqrt((x-x2)**2+(y-y2)**2)

plt.style.use(['nature','notebook'])
plt.contourf(x,y,V, levels=300, cmap='seismic', vmin=-150, vmax=150)
plt.colorbar(label='Electrical Potential [$V$]')
plt.title('Electrical Potential of a Dipole')
plt.xlabel('Horizontal Position [m]')
plt.ylabel('Vertical Position [m]')
plt.show()

_ = np.linspace(-1, 1, 31)
x, y = np.meshgrid(_,_)

Ex = k*q1*(x-x1)/((x-x1)**2+(y-y1)**2)**(3/2) - k*q2*(x-x2)/((x-x2)**2+(y-y2)**2)**(3/2)
Ey = k*q1*(y-y1)/((x-x1)**2+(y-y1)**2)**(3/2) - k*q2*(y-y2)/((x-x2)**2+(y-y2)**2)**(3/2)

E = np.sqrt(Ex**2 + Ey**2)
Ex = Ex/E
Ey = Ey/E

plt.style.use(['nature','notebook'])
plt.quiver(x, y, Ex, Ey, E)
plt.colorbar(label='Electrical Field [$V/m$]')
plt.title('Electrical Field of a Dipole')
plt.xlabel('Horizontal Position [m]')
plt.ylabel('Vertical Position [m]')
plt.show()

dx = x[0,1] - x[0,0]
dy = y[1,0] - y[0,0]
Ex_ = -1 * np.gradient(V, dx, dy)[0]
Ey_ = -1 * np.gradient(V, dx, dy)[1]
# E = -1 * np.gradient(V, dx, dy)

plt.style.use(['nature','notebook'])
plt.quiver(x, y, Ex_, Ey_)
plt.colorbar(label='Electrical Field [$V/m$]')
plt.title('Electrical Field of a Dipole')
plt.xlabel('Horizontal Position [m]')
plt.ylabel('Vertical Position [m]')
plt.show()
