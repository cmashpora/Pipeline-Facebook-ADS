import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import cdata.facebookads as mod
import plotly.graph_objs as go
 
cnxn = mod.connect("InitiateOAuth=GETANDREFRESH;OAuthSettingsLocation=/PATH/TO/OAuthSettings.txt")
 
df = pd.read_sql("SELECT AccountId, Name FROM AdAccounts WHERE Name = 'Acct Name'", cnxn)
app_name = 'dash-facebookadsdataplot'
 
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
 
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'CData + Dash'
trace = go.Bar(x=df.AccountId, y=df.Name, name='AccountId')
 
app.layout = html.Div(children=[html.H1("CData Extension + Dash", style={'textAlign': 'center'}),
dcc.Graph(
id='example-graph',
figure={
'data': [trace],
'layout':
go.Layout(title='Facebook Ads AdAccounts Data', barmode='stack')
})
], className="container")
 
if __name__ == '__main__':
    app.run_server(debug=True)