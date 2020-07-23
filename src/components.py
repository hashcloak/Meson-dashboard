import dash 
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from collections import defaultdict
from pprint import pprint

from mixnet import mixnet_document, prometheus_data

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
    names = [
        html.Div(n['Name'], style={'align-self':'center'}) for n in nodes if n['Layer'] == layer
    ]
    return html.Div(
        id='layer-{}'.format(layer),
        children = [
            html.Div(
                'Layer {}'.format(layer),
                style={
                    'align-self':'center',
                    'padding':'10px',
                    'width': '1.3em',
                }
            ),
            html.Div(names)
        ],
        style = {
            'display':'flex',
            'flex-direction': 'column',
            'flex': '0 0 auto',
            'padding': '20px',
            'margin': '5px',
            'border-color':'lightblue',
            'width': '1.5rem'
    })

def layers():
    layer_numbers = []
    topology = []
    # Topology is a a list of nested lists of each layer
    for layer in document['Document']['Topology']:
        topology.extend([node for node in layer])
        if topology[-1]['Layer'] not in layer_numbers:
            layer_numbers.append(topology[-1]['Layer'])

    return html.Div(
        children = [generate_layer(l, topology) for l in layer_numbers],
        style = {
            'display':'flex',
            'width': '80%',
            'margin':'auto',
            'flex':'1 0 75%',
            'flex-direction': 'row',
    })

def generate_providers(provider):

    addresses = [item for sublist in provider['Addresses'].values() for item in sublist]
    coins = []
    for plugin in provider['Kaetzchen'].values():
        if plugin.get('name') =='currency_trickle':
            coins.append(plugin.get('endpoint').replace('+', ''))
            
    nameDiv = html.Div(
        provider['Name'],
        style = {
            'font-size': '1.3rem',
        }
    )
    addressesDiv = html.Div(
        children=[
            html.Div('Addresses: ' if len(addresses) == 0 else 'Address: '),
            html.Div(addresses)
        ],
        style = {
            'display': 'flex',
            'flex-direction': 'row',
            'flex': '0 0 1.1rem'
        }
    )
    coinsDiv = html.Div(
        children=[
            html.Div('Supported coins: '),
            html.Div(coins)
        ],
        style = {
            'display': 'flex',
            'flex-direction': 'row',
            'flex': '0 0 1.1rem'
        }
    )
    return html.Div(
        children = [nameDiv, addressesDiv, coinsDiv,],
        style = {
            'display': 'flex',
            'flex-direction': 'column',
            'flex': '0 0 100px',
            'align-self': 'center',
        }
    )

def get_provider_address():
    pass

def get_node_address():
    pass

def network_state():
    return html.Div(
        'a'
    )

Header = html.H1("Meson Mixnet Statistics")

NetworkState = html.Div(
    id="network_container",
    children=[
        network_state(),
        html.Div("Current Epoch: {}".format(document['Document']['Epoch']))
    ]
)

Layers = html.Div(
    id="layers",
    children=layers(),
    style = {
        'display': 'flex'
    }
)
Providers = html.Div(
    id='providers',
    children=[generate_providers(p) for p in document['Document']['Providers']],
    style = {
        'display':'flex',
        'flex-direction': 'column',
    }
)
Authority = html.Div(
)
