# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt


sx = np.linspace(-1.2, 1.2, 24)
sy = np.linspace(-1, 1, 20)
x, y = np.meshgrid(sx,sy)

k = 9E9
q1 = 1E-9
x1, y1  = -0.3, 0
q2 = -1E-9
x2, y2  = 0.3, 0


V = (k*q1/np.sqrt((x-x1)**2+(y-y1)**2) + 
     k*q2/np.sqrt((x-x2)**2+(y-y2)**2))

plt.contourf(x,y,V, levels=300, cmap='seismic', vmin=-150, vmax=150)
plt.colorbar(label='Electrical Potential [$V$]')
plt.title('Electrical Potential of a Dipole')
plt.xlabel('Horizontal Position [m]')
plt.ylabel('Vertical Position [m]')
plt.show()


Ex = (k*q1*(x-x1)/((x-x1)**2+(y-y1)**2)**(3/2) +
      k*q2*(x-x2)/((x-x2)**2+(y-y2)**2)**(3/2))

Ey = (k*q1*(y-y1)/((x-x1)**2+(y-y1)**2)**(3/2) +
      k*q2*(y-y2)/((x-x2)**2+(y-y2)**2)**(3/2))

E = np.sqrt(Ex**2 + Ey**2)
cos = Ex/E
sin = Ey/E

E_max = 400
E[E>E_max] = E_max
E[E<-E_max] = -E_max

plt.quiver(x, y, cos, sin, E, pivot='mid')
#plt.streamplot(x, y, Ex, Ey)
plt.colorbar(label='Electrical Field [$V/m$]')
plt.title('Electrical Field of a Dipole')
plt.xlabel('Horizontal Position [m]')
plt.ylabel('Vertical Position [m]')
plt.show()

dx = x[0,1] - x[0,0]
dy = y[1,0] - y[0,0]

Ex_, Ey_ = np.gradient(V, dx, dy)
Ex_ = -1 * Ex_
Ey_ = -1 * Ey_


E_ = np.sqrt(Ex_**2 + Ey_**2)
cos_ = Ex_/E_
sin_ = Ey_/E_

E_max_ = 400
E_[E_>E_max_] = E_max_
E_[E_<-E_max_] = -E_max_

plt.quiver(x, y, cos_, sin_, E_, pivot='mid')
#plt.streamplot(x, y, Ex_, Ey_)
plt.colorbar(label='Electrical Field [$V/m$]')
plt.title('Electrical Field of a Dipole')
plt.xlabel('Horizontal Position [m]')
plt.ylabel('Vertical Position [m]')
plt.show()
