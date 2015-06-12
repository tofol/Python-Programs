# -*- coding: utf-8 -*-
"""
Created on Sat May 30 08:57:38 2015

@author: Tobal
"""

__author__ = 'Tobal'
__email__ = 'lopeztobal@gmail.com'
__version__ = '1.0'


from bokeh.plotting import figure
from bokeh.models import Range1d
from mybokeh import *
import numpy as np
from scipy import stats


f = lambda x: 1. / x

x = np.linspace(-5.0, 5.0, 200)
pos = np.where(np.abs(np.diff(f(x))) >= 10.0)[0]
x = np.insert(x, pos, np.nan)

TOOLS = 'pan, wheel_zoom, box_zoom, reset, save, help'

p = figure(tools=TOOLS)
plot_settings(p, 'Rational Function', 'x', 'f(x)', 500, 500, Range1d(-5, 5), Range1d(-5, 5), 10)

my_function_plot(p, x, f(x), 'f(x)=1/x', 2, 'firebrick', 0.75)
asymptote(p, np.arange(-5, 6), 0, 'y=0', 2, [6, 4], 'navy', 0.75)
asymptote(p, 0, np.arange(-5, 6), 'x=0', 2, [6, 4], 'red', 0.75)

samplex = np.array([2, 2, 3, 3, 4, 4, 4, 5, 5, 5])
sampley = np.array([1, 2, 2, 3, 3, 4, 5, 4, 5, 6])

slope, intercept, r_value, p_value, std_err = stats.linregress(
    samplex, sampley)
r_squared = r_value ** 2
slopex, interceptx, r_valuex, p_valuex, std_errx = stats.linregress(
    sampley, samplex)
r_squaredx = r_valuex ** 2

p1 = figure(tools=TOOLS)
plot_settings(p1, 'Linear Regression', 'Number Of Rooms', 'Number Of Persons', 500, 500, Range1d(0, 7), Range1d(0, 8), 10)

scatter_plot(p1, samplex, sampley, 'Rooms / People', 2, 'firebrick', 0.75)
legend1 = 'y = {0:2.1f} + {1:2.3f}(x-{2:2.1f})'.format(
    np.mean(sampley), slope, np.mean(samplex))
legend2 = 'x = {0:2.1f} + {1:2.3f}(y-{2:2.1f})'.format(
    np.mean(samplex), slopex, np.mean(sampley))
regr_segment(p1, samplex[0], regression_line(samplex[0], slope, intercept), samplex[-1], regression_line(samplex[-1], slope, intercept), legend1, 2, 'navy', 0.75)
regr_segment(p1, sampley[0], regression_line(sampley[0], slopex, interceptx), sampley[-1], regression_line(sampley[-1], slopex, interceptx), legend2, 2, 'green', 0.75)

p2 = figure(tools=TOOLS)
abcisa = np.linspace(-7.0, 7.0, 1000)
pos = np.where(np.abs(np.diff(np.floor(abcisa))) >= 1.0)[0] + 1
abcisa = np.insert(abcisa, pos, np.nan)
igual = np.arange(-7, 7, 1)
igual_mas_uno = igual + np.ones(7 - (-7), np.int)
plot_settings(p2, 'Floor Function', 'x', 'y', 500, 500, Range1d(-7, 7), Range1d(-7, 8), 10)
my_function_plot(p2, abcisa, np.floor(abcisa), 'f(x)', 2, 'blue', 0.75)
circles_plot(p2, igual, igual, '', 2, 'blue', 'blue', 0.75)
circles_plot(p2, igual_mas_uno, igual, '', 2, 'blue', 'white', 0.75)

plot_html(p, './js/figures.js', 'myplot')
plot_html(p1, './js/figures1.js', 'myplot1')
plot_html(p2, './js/figures2.js', 'myplot2')
