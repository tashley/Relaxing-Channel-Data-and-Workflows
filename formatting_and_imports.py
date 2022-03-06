import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from scipy.optimize import curve_fit
import matplotlib.colors as colors
import warnings
from scipy.stats import norm
import pandas as pd
warnings.filterwarnings('ignore')

plt.style.use(plt.style.available[1])
mpl.rcParams['axes.grid'] = False
mpl.rcParams['xtick.bottom'] = True
mpl.rcParams['xtick.top'] = False

mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['xtick.major.size'] = 3
mpl.rcParams['xtick.major.width'] = 1.2

mpl.rcParams['ytick.direction'] = 'in'
mpl.rcParams['ytick.major.size'] = 3
mpl.rcParams['ytick.major.width'] = 1.2

mpl.rcParams['xtick.minor.size'] = 2
mpl.rcParams['xtick.minor.width'] = 0.7

mpl.rcParams['ytick.minor.size'] = 2
mpl.rcParams['ytick.minor.width'] = 0.7


mpl.rcParams['axes.facecolor'] = 'white'
mpl.rcParams['axes.edgecolor'] = 'black'
mpl.rcParams['axes.linewidth'] = '1.1'

mpl.rcParams['font.family'] = 'arial'
mpl.rcParams['font.size'] = 10.33

# ==============================================================
def make_colorbar(cax, cmap, ticklocs=[0,1], ticklabels=[0,1], label=None, labelpad=0):
    cmap = mpl.cm.get_cmap(cmap)
    norm = mpl.colors.Normalize(vmin=0, vmax=1)
    cb = mpl.colorbar.ColorbarBase(cax, cmap=cmap, norm=norm)
    cb.set_ticks(ticklocs)
    cb.set_ticklabels(ticklabels)
    cb.set_label(label, labelpad=labelpad)
    return cb

# ==============================================================
def fig2_axes():
    axw = 3.5
    axh = axw
    top = 0.1
    right = 0.1
    wspace = 0.6
    left = 0.6
    bottom = 0.5

    figw = left + axw + wspace + axw + right
    figh = top + axh + bottom

    fig = plt.figure(figsize=(figw, figh), constrained_layout=False)

    ax0 = fig.add_axes([left/figw, bottom/figh, axw/figw, axh/figh])
    ax1 = fig.add_axes([(left + axw + wspace)/figw, bottom/figh, axw/figw, axh/figh])
    
    axins0 = ax0.inset_axes([0.08, 0.07, 0.4, 0.4])
    axins1 = ax1.inset_axes([0.08, 0.57, 0.4, 0.4])
    
    cax0 = ax0.inset_axes([0.49, 0.07, 0.03, 0.4])
    cax1 = ax1.inset_axes([0.49, 0.57, 0.03, 0.4])
    
    return [ax0, ax1], [axins0, axins1], [cax0, cax1]

# ==============================================================
def fig3_axes():
    ax1h = 3
    ax1w = ax1h

    wspace = 0.5
    hspace = 0.5

    top = 0.1
    left = 0.5
    bottom = 0.5
    right = 0.1

    ax0h = ax1h*(2/3)
    ax1h = ax0h
    ax1w = ax1h

    figh = top + ax0h + hspace + ax1h + bottom
    figw = left + ax1w + wspace + ax1w + right
    ax0w = (left + wspace + ax1w + right)

    fig = plt.figure(figsize=(figw, figh), constrained_layout=False)

    ax0 = fig.add_axes([left/figw, (bottom + ax1h + hspace)/figh, ax0w/figw, ax0h/figh])
    ax1 = fig.add_axes([left/figw, bottom/figh, ax1w/figw, ax1h/figh])
    ax2 = fig.add_axes([(left+ax1w+wspace)/figw, bottom/figh, ax1w/figw, ax1h/figh])

    return[ax0, ax1, ax2]
