import dash 
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

## Style dicts for divs
style_aggregate_stat_divs = {
    'display': 'inline-block',
    'border-style': 'dash',
    'border-color': 'black'
}

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


Header = html.H1(children="Meson Dashboard")

NetworkState = html.Div(children=[
        html.Div(children=[
            html.Div(children=[
            html.H2(children="Average latency"),
            html.H3(children="100 ms") # placeholder until we get data from prometheus instrumentation
            ], className="col-sm"),
            html.Div(children=[
                html.H2(children="Overall Anonymity Set"),
                html.H3(children="100") # placeholder until we get data from prometheus instrumentation
            ], className="col-sm"),
            html.Div(children=[
                html.H2(children="Largest Outgress Anonymity Set"),
                html.H3(children="100") # placeholder until we get data from prometheus instrumentation
            ], className="col-sm")
        ], className="row")
    ], style={'display': 'inline-block'}, className="container")

Nodes = html.Div(children=[
        html.Div(children=[
            html.Div(children=[
                html.Table(children=[
                    html.Thead(children=[html.H2(children="Mix Nodes")]),
                    html.Tr(children=[
                        html.Th(children="#"),
                        html.Th(children="public key"),
                        html.Th(children="layer")
                    ]),
                    createMixTableRow("1", "gewpin566", "2")
                    ], style={'margin': '1%', 'display': 'inline-block', 'border-style': 'solid'},
                    className="table")
            ], className="col-4"),
            html.Div(children=[
                html.Table(children=[
                html.Thead(children=[html.H2(children="Provider Nodes")]),
                html.Tr(children=[
                    html.Th(children="public key"),
                    html.Th(children="Cryptocurrencies supported")
                ]),
                createProviderTableRow("geiwpjg0r9ipgjmr", ["ETH", "ETC", "BNB"]),
                createProviderTableRow("90ugejwgnpojegef", ["ETH", "RIN", "GOR"])
                ], 
                style={'margin': '1%', 'display':'inline-block', 'border-style': 'dashed'},
                className="table")
            ], className="col-8")
        ], className="row")
    ], className="container")
