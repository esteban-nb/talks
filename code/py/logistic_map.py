import numpy as np

import numba
import plotly.graph_objects as go

NUM_FRAMES = 100
DURATION = 50  # ms per frame
R_MIN, R_MAX = 2.5, 4.0

@numba.njit(parallel=True)
def get_bifurcation_data(r_min, r_max, steps=1000):
    iterations = 1000
    last = 100
    r_values = np.linspace(r_min, r_max, steps)

    r_out = np.empty(steps * last, dtype=np.float64)
    x_out = np.empty(steps * last, dtype=np.float64)

    for i in numba.prange(steps):
        r = r_values[i]
        x = 1e-5

        # Transient iterations
        for j in range(iterations - last):
            x = r * x * (1.0 - x)

        # Steady state iterations to save
        for j in range(last):
            x = r * x * (1.0 - x)
            idx = i * last + j
            r_out[idx] = r
            x_out[idx] = x

    return r_out, x_out


# ------------------------------
# Data & Frames
# ------------------------------

numba.set_num_threads(4)
r_data, x_data = get_bifurcation_data(R_MIN, R_MAX)

indices = np.linspace(0, len(r_data), NUM_FRAMES + 1, dtype=int)

frames = [go.Frame(
    data=[go.Scatter(x=r_data[:indices[i]], y=x_data[:indices[i]])],
    name=str(i) 
) for i in range(1, NUM_FRAMES + 1)]


# ------------------------------
# Static HTML
# ------------------------------

fig = go.Figure(data=go.Scattergl(x=r_data, y=x_data, mode='markers', 
                                  marker=dict(size=1, color='black', opacity=0.1)))
fig.update_layout(title=None, xaxis_title="r", yaxis_title="x")
fig.write_html("bifurcation_static.html")


# ------------------------------
# Dynamic HTML
# ------------------------------

fig = go.Figure(
    data=[go.Scatter(x=[], y=[], mode='markers', marker=dict(size=1, color='black', opacity=0.3))],
    layout=go.Layout(
        title=None,
        xaxis=dict(range=[2.5, 4.0], autorange=False, title="r"),
        yaxis=dict(range=[0, 1], autorange=False, title="x"),
        updatemenus=[]
    ),
    frames=frames
)

fig.write_html(
    "bifurcation_autoplay.html", 
    auto_play=True, 
    animation_opts={
        "frame": {"duration": DURATION, "redraw": False},
        "transition": {"duration": 0}
    }
)


# ------------------------------
# Interactive HTML
# ------------------------------

slider_steps = [
    {
        "method": "animate",
        "args": [
            [str(i)],
            {
                "mode": "immediate",
                "frame": {"duration": 0, "redraw": False},
                "transition": {"duration": 0},
            },
        ],
        "label": f"{R_MIN + (R_MAX - R_MIN) * i / NUM_FRAMES:.2f}",
    }
    for i in range(1, NUM_FRAMES + 1)
]

sliders = [
    {
        "active": 0,
        "y": -0.08,
        "x": 0.05,
        "len": 0.9,
        "pad": {"b": 10, "t": 10},
        "currentvalue": {
            "prefix": "r ≈ ",
            "font": {"size": 14},
        },
        "steps": slider_steps,
    }
]

updatemenus = [
    {
        "type": "buttons",
        "direction": "left",
        "x": 0.04,
        "y": -0.13,
        "pad": {"r": 10, "t": 10},
        "buttons": [
            {
                "label": "▶",
                "method": "animate",
                "args": [
                    None,
                    {
                        "frame": {"duration": DURATION, "redraw": False},
                        "transition": {"duration": 0},
                        "fromcurrent": True,
                        "mode": "immediate",
                    },
                ],
                "args2": [
                    [None],
                    {
                        "frame": {"duration": 0, "redraw": False},
                        "mode": "immediate",
                    },
                ],
            }
        ],
    }
]

fig = go.Figure(
    data=[
        go.Scattergl(
            x=[],
            y=[],
            mode="markers",
            marker=dict(size=1, color="black", opacity=0.35),
        )
    ],
    layout=go.Layout(
        title=None,
        xaxis=dict(range=[R_MIN, R_MAX], title="r"),
        yaxis=dict(range=[0, 1], title="x"),
        sliders=sliders,
        updatemenus=updatemenus,
        margin=dict(l=60, r=20, t=60, b=80),
    ),
    frames=frames,
)

fig.write_html("bifurcation_interactive.html", auto_play=False)