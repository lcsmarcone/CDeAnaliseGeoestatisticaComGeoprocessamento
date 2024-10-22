# import bokeh.plotting as bp
from bokeh.plotting import figure, show

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(title="Gráfico simples de linha", x_axis_label='x', y_axis_label='y')

p.line(x, y, legend_label="Tempo", line_width=2)

show(p)