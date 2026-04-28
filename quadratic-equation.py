import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import plotly.graph_objects as go

from sympy import *
x = sp.symbols('x')
y = x**2 - 4*x + 3
f = sp.lambdify(x, y,'numpy')

xValue = np.linspace(-2, 6)
yValue = f(xValue)

# Matplotlib Static Graph
plt.title('Matplotlib Static Graph')
plt.xlabel('x E (-2,6)')
plt.ylabel('y = x^2 - 4x + 3')
plt.plot(xValue,yValue)
plt.show()

#Plotly Interactive Graph
graph = go.Figure()
graph.add_trace(go.Scatter(
    x = xValue, 
    y = yValue, 
    name = "y = x^2 - 4x + 3",
))
graph.update_layout(
    title = 'Plotly Interactive Graph',
    xaxis_title = 'x E (-2,6)',
    yaxis_title = 'y = x^2 - 4x + 3',
)
