import matplotlib.pyplot as plt
import sys

h = -0.01
hh = 0
hhh = 0
h_t = []
t_t = []
dummy = []
l = 0.05
t = 0
dt = 0.00001
k = 16.77
rho_ice = 916.7
rho_water = 997
L = 6e3
P = 1
while (t<3 and l>0):
    l = max(0, pow(max(0, pow(0.3, 3) - t*P/(L * rho_ice)), 1/3))
    h_t.append(h)
    t_t.append(t)
    hhh = -rho_water * pow(l, 2) * 9.81 * h - k * l * hh + hh * P/L
    dummy.append(pow(l, 3))
    hh += hhh*dt
    h += hh*dt
    t += dt
    hhh = 0
plt.plot(t_t, h_t)
plt.plot(t_t, [h_t[-1] for i in t_t])
# plt.plot(t_t, dummy)
print(len(t_t))
# for i in dummy:
#     print(i)