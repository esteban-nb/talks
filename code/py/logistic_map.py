import numpy as np
import plotly.graph_objects as go

def get_bifurcation_data(r_min=2.5, r_max=4.0, steps=1e3):
    r_values = np.linspace(r_min, r_max, steps)
    iterations, last = 1000, 100
    x = 1e-5 * np.ones(steps)
    
    r_out, x_out = [], []
    for i in range(iterations):
        x = r_values * x * (1 - x)
        if i >= (iterations - last):
            r_out.extend(r_values)
            x_out.extend(x)
    return r_out, x_out


# ------------------------------
# Static HTML
# ------------------------------

r_data, x_data = get_bifurcation_data()
fig = go.Figure(data=go.Scattergl(x=r_data, y=x_data, mode='markers', 
                                  marker=dict(size=1, color='black', opacity=0.1)))
fig.update_layout(title="Logistic Map Bifurcation Diagram", xaxis_title="r", yaxis_title="x")
fig.write_html("bifurcation_static.html")


# ------------------------------
# Dynamic HTML
# ------------------------------

frames = [go.Frame(data=[go.Scattergl(x=r_data[:k], y=x_data[:k])], name=str(k))
          for k in range(0, len(r_data), len(r_data)//50)]

fig_dynamic = go.Figure(data=[go.Scattergl(x=[], y=[])], frames=frames)
fig_dynamic.update_layout(updatemenus=[dict(type="buttons", buttons=[dict(label="Play", method="animate")])])
fig_dynamic.write_html("bifurcation_dynamic.html")

# ------------------------------
# Interactive HTML
# ------------------------------

fig_interactive = go.Figure(
    data=[go.Scattergl(x=r_data, y=x_data, mode='markers', marker=dict(size=1))],
    layout=go.Layout(
        updatemenus=[dict(type="buttons", buttons=[
            dict(label="Play", method="animate", args=[None, {"frame": {"duration": 50, "redraw": False}}]),
            dict(label="Pause", method="animate", args=[[None], {"frame": {"duration": 0, "redraw": False}, "mode": "immediate"}])
        ])],
        sliders=[dict(steps=[dict(method="animate", args=[[f.name], {"mode": "immediate"}], label=f.name) for f in frames])]
    ),
    frames=frames
)
fig_interactive.write_html("bifurcation_interactive.html")
