from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import ephem # to make coordinate systems conversions

# alpha is the right ascension (ra)
# delta is the declination (dec)
# both in degrees!
def plot_ait(alpha, delta, origin = 0):
  x = np.remainder(alpha + 360 - origin, 360) # shift alpha values, mod 360
  x[x > 180] -= 360 # from -180 to 180
  x = -x # reverse the scale: East to the left
  x = np.radians(x) # in radians

  y = np.radians(delta) # in radians

  tick_labels = np.arange(150, -180, -30)
  tick_labels = np.remainder(tick_labels + 360 + origin, 360)

  fig = plt.figure(dpi=200)
  ax = fig.add_subplot(111, projection='aitoff')
  ax.scatter(x, y, s=1, marker='.', color='grey')

  # configure ticks and labels
  ax.set_xticklabels(tick_labels, fontsize=8)
  for tick in ax.yaxis.get_major_ticks(): tick.label.set_fontsize(8)
  ax.set_xlabel('Ascensão Reta')
  ax.xaxis.label.set_fontsize(8)
  ax.set_ylabel('Declinação')
  ax.yaxis.label.set_fontsize(8)
  ax.grid(True)

  return fig
