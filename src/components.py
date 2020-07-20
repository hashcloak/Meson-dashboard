import dash 
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

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

def layers():
    style = {
        'display':'flex'
    }
    topology = [item for sublist in document['Topology'] for item in sublist]
    zero = [k for k in topology if k['Layer'] == 0]
    one = [k for k in topology if k['Layer'] == 1]
    two = [k for k in topology if k['Layer'] == 2]

    return html.Div(children = [
        html.Div(id='layer-zero', children=[n['Name'] for n in zero]),
        html.Div(id='layer-one', children=[n['Name'] for n in one]),
        html.Div(id='layer-two', children=[n['Name'] for n in two]),
    ], style = style)

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
