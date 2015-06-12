# -*- coding: utf-8 -*-
"""
Created on Sat May 30 08:57:38 2015

@author: Tobal
"""

__author__ = 'Tobal'
__email__ = 'lopeztobal@gmail.com'
__version__ = '1.0'


from bokeh.embed import components


regression_line = lambda x, slope, intercept: slope * x + intercept


def plot_settings(my_figure, title, xlabel, ylabel, pwidth, pheight, xrange, yrange, legend_space):
    my_figure.title = title
    my_figure.xaxis.axis_label = xlabel
    my_figure.yaxis.axis_label = ylabel
    my_figure.plot_width = pwidth
    my_figure.plot_height = pheight
    my_figure.x_range = xrange
    my_figure.y_range = yrange
    my_figure.legend.legend_spacing = legend_space


def my_function_plot(my_figure, x, y, legend, line_width, color, alpha):
    my_figure.line(
        x, y, legend=legend, line_width=line_width, color=color, alpha=alpha)


def asymptote(my_figure, x, y, legend, line_width, line_dash, color, alpha):
    my_figure.line(x, y, legend=legend, line_width=line_width,
                   line_dash=line_dash, color=color, alpha=alpha)


def scatter_plot(my_figure, x, y, legend, line_width, color, alpha):
    my_figure.circle(
        x, y, legend=legend, line_width=line_width, color=color, alpha=alpha)


def circles_plot(my_figure, x, y, legend, line_width, color, fill_color, alpha):
    my_figure.circle(
        x, y, legend=legend, line_width=line_width, color=color, fill_color=fill_color, alpha=alpha)


def regr_segment(my_figure, x0, y0, x1, y1, legend, line_width, color, alpha):
    my_figure.segment(
        x0, y0, x1, y1, legend=legend, line_width=line_width, color=color, alpha=alpha)


def plot_html(myfigure, myfilejs, myclass):
    script, div = components(myfigure)
    with open(myfilejs, 'wt') as myfile:
        script = script.replace('</script>', '')
        script = script.replace('<script type="text/javascript">', '')
        div = div.replace(
            div, 'document.querySelector(".' + myclass + '").innerHTML = ' + "'" + div + "'")
        print(script + div, file=myfile)
