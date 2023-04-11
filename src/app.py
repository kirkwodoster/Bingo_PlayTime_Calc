# -*- coding: utf-8 -*-
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.SLATE]

app = Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server


app.layout = dbc.Container(
    [
    
        dbc.Row(
            dbc.Col(
                html.Div(
                    html.H3("Calculate Bingo")
                        )
                    )
                ),
                
        html.Br(),

        dbc.Row(
            [
                dbc.Col(
                        html.Div("Nautical Miles", className="text-info")),
                dbc.Col(
                        html.Div("Ground Speed", className="text-info")),
                dbc.Col(
                        html.Div("Fuel Flow", className="text-info"))
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Input(id='distance', type="number", value=0)),
                dbc.Col(
                    dcc.Input(id='speed', type="number", value=0)),
                dbc.Col(
                    dcc.Input(id='fuelflow', type="number", value=0)),                    
            ]
        ),

        html.Br(),

        dbc.Row(
            [
             dbc.Col(
                dbc.Button(id='bingobutton', n_clicks=0, children='Calculate Bingo', className="btn btn-success", size = 'sm')
                    )
            ]),
        dbc.Row(
            [
            dbc.Col(
                html.Div(
                        html.H3(className="text-danger", id='bingo')
                )
            ,)]),

        html.Br(),

        dbc.Col(
            html.Div(
                html.H3("Calculate Play Time")
                    )
                ),

        html.Br(),
         dbc.Row(
            [
                dbc.Col(
                        html.Div("Total Fuel", className="text-info")),
                dbc.Col(
                        html.Div("Bingo", className="text-info")),
                dbc.Col(
                        html.Div("Fuel Flow", className="text-info")),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Input(id='totalfuel', type="number", value=0)),
                dbc.Col(
                    dcc.Input(id='bingoinput', type="number", value=0)),
                dbc.Col(
                    dcc.Input(id='fuelflow2', type="number", value=0)),
            ]
        ),
        html.Br(),
        dbc.Row(
            [
             dbc.Col(
                dbc.Button(id='playtimebutton', n_clicks=0, children='Calculate Play Time', className="btn btn-success", size = 'sm')
                    )
            ]
                ),
         dbc.Row(
            [
            dbc.Col(
                html.Div(
                        html.H3(className="text-danger", id="playtime")
                )
            ,)])
    ]
)

def Bingo(distance, speed, ff):
    bingo = (((distance / speed) + (1/3)) * ff) + 22
    return bingo

def Playtime(tf, bingo, ff):
    playtime = (tf - bingo)/ff
    hours = int(playtime)
    minutes = (playtime*60) % 60
    return "%d+%02d" % (hours, minutes)


@app.callback(Output('bingo', 'children'),
              Input('bingobutton', 'n_clicks'),
              State('distance', 'value'),
              State('speed', 'value'),
              State('fuelflow', 'value'))

def update_bingo(n_clicks, distance, speed, fuelflow):
    if n_clicks == 0:
        raise PreventUpdate
    else:
        bingo = Bingo(distance, speed, fuelflow)
        return u'''BINGO IS 
        {:,.0f}
        '''.format(bingo)



@app.callback(Output('playtime', 'children'),
              Input('playtimebutton', 'n_clicks'),
              State('totalfuel', 'value'),
              State('bingoinput', 'value'),
              State('fuelflow2', 'value'))

def update_playtime(n_clicks, totalfuel, bingoinput, fuelflow2):
    if n_clicks == 0:
        raise PreventUpdate
    else:
        playtime = Playtime(totalfuel, bingoinput, fuelflow2)
        return u''' PLAY TIME IS
        {}
        '''.format(playtime)



if __name__ == '__main__':
    app.run_server(debug=True)
