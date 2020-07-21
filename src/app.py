import dash 
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from components import Header, NetworkState, Nodes, Layers

from mixnet import mixnet_document, prometheus_data

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = html.Div(
    children=[
        Header,
        NetworkState,
        Layers,
        Nodes,
    ],
    style={
        'display': 'flex',
        'flex-direction': 'column',
        'align-items': 'center',
        'margin': '0 auto',
    }
)

"""
@app.callback(
    [Output(component_id='network_container', component_property='children')],
    [Input(component_id='update_all', component_property='value')]
)
def update_network():
    return
    pass
"""

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", debug=True)
