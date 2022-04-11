import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from scipy.optimize import minimize
import matplotlib.colors as colors
import matplotlib.patches as mpatches
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
mpl.rcParams['font.size'] = 11

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
def fig2_axes(scale):
    axw = scale
    axh = axw
    top = 0.2
    right = 0.1
    wspace = 0.6
    left = 0.6
    bottom = 0.5

    figw = left + axw + wspace + axw + right
    figh = top + axh + bottom

    fig = plt.figure(figsize=(figw, figh), constrained_layout=False)

    ax0 = fig.add_axes([left/figw, bottom/figh, axw/figw, axh/figh])
    ax1 = fig.add_axes([(left + axw + wspace)/figw, bottom/figh, axw/figw, axh/figh])
    
    axins0 = ax0.inset_axes([0.09, 0.07, 0.4, 0.4])
    axins1 = ax1.inset_axes([0.47, 0.07, 0.4, 0.4])
    
    cax0 = ax0.inset_axes([0.5, 0.07, 0.03, 0.4])
    cax1 = ax1.inset_axes([0.88, 0.07, 0.03, 0.4])
    
    return [ax0, ax1], [axins0, axins1], [cax0, cax1]

# ==============================================================
def fig3_axes(scale):
    ax2h = scale
    ax2w = ax2h

    wspace0 = 0
    wspace2 = 0.2
    hspace = 0.5

    top = 0.2
    left = 0.5
    bottom = 0.5
    right = 0.1

    ax0h = ax2h*(2/3)
    ax0w = ax0h
    
    figh = top + ax0h + hspace + ax2h + bottom
    figw = left + ax2w + wspace2 + ax2w + right
    ax1w = figw - (wspace0 + ax0w + left + right)

    fig = plt.figure(figsize=(figw, figh), constrained_layout=False)

    ax0 = fig.add_axes([left/figw, (bottom + ax2h + hspace)/figh, ax0w/figw, ax0h/figh])
    ax1 = fig.add_axes([(left + ax0w + wspace0)/figw, (bottom + ax2h + hspace)/figh, ax1w/figw, ax0h/figh])
    ax2 = fig.add_axes([left/figw, bottom/figh, ax2w/figw, ax2h/figh])
    ax3 = fig.add_axes([(left+ax2w+wspace2)/figw, bottom/figh, ax2w/figw, ax2h/figh])

    return[ax0, ax1, ax2, ax3]
