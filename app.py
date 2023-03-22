import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import altair as alt

df = pd.read_csv('data/raw/owid-covid-data.csv', parse_dates=['date'])
china_df = df[df['iso_code'] == 'CHN']

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("COVID-19 Visualization")),
    ]),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='cases-deaths-graph')
        ),
    ]),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='vaccinations-graph')
        ),
    ]),
    dbc.Row([
        dbc.Col(html.Label("Select Date:")),
    ]),
    dbc.Row([
        dbc.Col(
            dcc.Dropdown(
                id='date-dropdown',
                options=[{'label': month, 'value': month} for month in china_df['date'].dt.strftime('%Y-%m').unique()],
                value=china_df['date'].dt.strftime('%Y-%m').max()
            )
        ),
        dbc.Col(
            dcc.Dropdown(
                id='metric-dropdown',
                options=[
                    {'label': 'Total Cases', 'value': 'total_cases'},
                    {'label': 'Total Deaths', 'value': 'total_deaths'}
                ],
                value='total_cases'
            )
        ),
    ]),
    dbc.Row([
        dbc.Col(html.Label("Source: Our World in Data"))
    ])
])

@app.callback(
    [Output('cases-deaths-graph', 'figure'),
     Output('vaccinations-graph', 'figure')],
    [Input('date-dropdown', 'value'),
     Input('metric-dropdown', 'value')]
)
def update_figures(date, metric):
    # Filter data by date
    china_data = df[df['iso_code'] == 'CHN']
    china_data = china_data[china_data['date'].dt.strftime('%Y-%m') == date]
    world_data = df[df['location'] == 'World']
    world_vaccinations_data = world_data[['date', 'total_vaccinations']]

    # Create a bar chart for daily cases or deaths in China
    if metric == 'total_cases':
        chart_title = 'Monthly COVID-19 Cases in China'
        y_axis_label = 'New Cases'
        color = ['blue']
        y = 'new_cases'
    else:
        chart_title = 'Monthly COVID-19 Deaths in China'
        y_axis_label = 'New Deaths'
        color = ['red']
        y = 'new_deaths'

    chart = px.bar(china_data, x='date', y=y, color_discrete_sequence=color,
                   title=chart_title)

    # Create a line chart for the total vaccinations in China
    vaccinations_chart = px.line(china_df, x='date', y='total_vaccinations', color='location', 
                                 title='Trend of Total COVID-19 Vaccinations in China vs. World', height=400)
    vaccinations_chart.add_scatter(x=world_vaccinations_data['date'], y=world_vaccinations_data['total_vaccinations'], 
                                    mode='lines', name='World')

    return chart, vaccinations_chart
# Run app
if __name__ == '__main__':
    app.run_server(debug=True)