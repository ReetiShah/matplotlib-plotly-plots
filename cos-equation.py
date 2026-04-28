import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import plotly.graph_objects as go

from sympy import *
x = sp.symbols('x')
y = sp.exp(-x) * sp.cos(2*3.14*x)
f = sp.lambdify(x, y,'numpy')

xValue = np.linspace(-3,5)
yValue = f(xValue)

#Matplotlib Static Graph
plt.title('Matplotlib Static Graph')
plt.xlabel('x')
plt.ylabel('y = e^-x cos(2πx)')
plt.plot(xValue,yValue)
plt.show()

#Plotly Interactive Graph
graph = go.Figure()
graph.add_trace(go.Scatter(
    x = xValue, 
    y = yValue, 
    name = "y = e^-x cos(2πx)",
))
graph.update_layout(
    title = 'Plotly Interactive Graph',
    xaxis_title = 'x',
    yaxis_title = 'y = e^-x cos(2πx)',
)
