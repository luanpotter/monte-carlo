from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import ephem # to make coordinate systems conversions

def plot_ait(RA,Dec,org=0, projection='aitoff',alpha_d=None,delta_d=None):
  # RA e Dec devem ser dados em grau
  x = np.remainder(RA+360-org,360) # shift RA values
  ind = x>180
  if type(x) == type(np.float64()):
    x -= 360
  else:
    x[ind] -=360
  x=-x # reverse the scale: East to the left
  tick_labels = np.array([150, 120, 90, 60, 30, 0, 330, 300, 270, 240, 210])
  tick_labels = np.remainder(tick_labels+360+org,360)
  fig = plt.figure(dpi=100)
  ax = fig.add_subplot(111, projection=projection)
  ax.scatter(np.radians(x),np.radians(Dec),s=12,marker='.',color='#03a0ff') # convert degrees to radians
  if alpha_d is not None and delta_d is not None:
    y = np.remainder(alpha_d+360-org,360)
    y -= 360
    y = -y
    ax.scatter(np.radians(y),np.radians(delta_d),color='r')
  ax.set_xticklabels(tick_labels) # we add the scale on the x axis
  ax.set_xlabel('RA')
  ax.xaxis.label.set_fontsize(8)
  ax.set_ylabel('Dec')
  ax.yaxis.label.set_fontsize(8)
  ax.grid(True)
