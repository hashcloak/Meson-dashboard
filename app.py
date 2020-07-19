import dash 
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from components import Header, NetworkState, Nodes

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = html.Div(children=[
    Header,
    NetworkState,
    Nodes,
])

"""
@app.callback(
        )

def update_network():
"""

if __name__ == '__main__':
    app.run_server(debug=True)
