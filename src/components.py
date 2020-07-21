import dash 
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from collections import defaultdict
from pprint import pprint

from mixnet import mixnet_document

document = mixnet_document()

def createMixTableRow(index, public_key, layer):
    return html.Tr(children=[
        html.Th(children=index),
        html.Th(children=public_key),
        html.Th(children=layer)
    ])

def createProviderTableRow(public_key, cryptos_supported):
    return html.Tr(children=[
        html.Th(children=public_key),
        html.Th(children=[html.P(children=crypto) for crypto in cryptos_supported])
    ])

def public_keys():
    pass

def generate_layer(layer: int, nodes: list):
    return html.Div(
        id='layer-{}'.format(layer),
        children=[html.Div(n['Name'], style={'align-self': 'center'}) for n in nodes if n['Layer'] == layer],
        style = {
            'display':'flex',
            'flex-direction': 'column',
            'flex': '0 0 20px',
            'padding': '20px',
            'margin': '10px',
            'border':'1px solid',
    })

def layers():
    layer_numbers = defaultdict(int)
    topology = []
 
    # Topology is a a list of nested lists of each layer
    for layer in document['Topology']:
        topology.extend([node for node in layer])
        number = topology[-1]['Layer']
        layer_numbers[number] = layer_numbers[number] + 1

    return html.Div(
        children = [generate_layer(l, topology) for l in layer_numbers.keys()],
        style = {
            'display':'flex',
            'flex-direction': 'row',
    })

Header = html.Div(children=[
    html.H1(children="Meson Mixnet Statistics"),
    html.P(id="epoch", children="Current Epoch: "+str(document['Epoch'])),
])

NetworkState = html.Div(id="network_container", children=[])
Layers = html.Div(id="layers", children=layers())
Providers = html.Div("Providers")
Mixnodes = html.Div("Nodes")
Nodes = html.Div(children=[
    Providers,
    Mixnodes,
])
