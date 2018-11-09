#!/bin/python

import math
import numpy as np
import matplotlib.pyplot as plt

[cos, sin, pi, acos] = [math.cos, math.sin, math.pi, math.acos]
POINTS = 100

delta_min = np.radians(-90)
delta_max = np.radians(90)

theta_m = np.radians(80)
alpha_0 = np.radians(-35.2)

xi = lambda delta: (cos(theta_m) - sin(alpha_0) * sin(delta)) / (cos(alpha_0) * cos(delta))
alpha_m = lambda xi: 0 if xi > 1 else pi if xi < -1 else acos(xi)
omega = lambda delta: cos(alpha_0)*cos(delta)*sin(alpha_m(xi(delta))) + alpha_m(xi(delta))*sin(alpha_0)*sin(delta)

def plot(xs, ys):
  plt.plot(xs, ys, color='black')
  plt.xlabel('$\delta$ (degrees)')
  plt.ylabel('$\omega(\delta)$')
  plt.title('Gráfico da Exposição $\omega$ em função da declinação $\delta$')
  plt.draw()

def main():
  deltas = np.linspace(delta_min, delta_max, num = POINTS)
  deltas_degrees = list(map(np.degrees, deltas))
  omegas = list(map(omega, deltas))
  plot(deltas_degrees, omegas)

main()
plt.show()
