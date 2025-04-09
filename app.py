import pandas as pd
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import plotly.express as px

# Load data
df = pd.read_csv(r"C:\Users\HP\OneDrive\เอกสาร\Pandas project\stockdata.csv")
df['Date'] = pd.to_datetime(df['Date'])
external_stylesheets=["https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"]
# External stylesheet for better styling
app = Dash(__name__, external_stylesheets=external_stylesheets)

# App layout
app.layout = html.Div(
    style={
        'background': 'linear-gradient(135deg, #f0f4f8, #d9e2ec)',
        'minHeight': '100vh',
        'padding': '30px'},
    children=[
    html.Div([
        html.H1("📊 Stock Price Analysis", className="text-center my-4",
        style={
        'fontWeight': 'bold',
        'fontSize': '3rem',
        'color': '#2b9348',
        'textShadow': '1px 1px 2px #999'
        }),
        

        html.Div([
            html.Label("Select a Stock", className="form-label font-weight=bold",
            style={'fontSize': '1.22rem', 'font-weight':'bold','color':'dark'}),
            dcc.Dropdown(
                options=[{'label': stock, 'value': stock} for stock in ['MSFT', 'IBM', 'SBUX', 'AAPL', 'GSPC']],
                value='AAPL',
                id='stock-dropdown',
                clearable=False,
                className="form-select",
                style={
                    'padding':'10px',
                    'margin': 'auto',
                    
                }
                            )
        ], className="mb-4"),

        html.Div([
            html.H5("Stock Price Table", className="text-secondary mb-3",
                    style={'font-weight':'bold', 'font-size':'1.2rem'}),
            dash_table.DataTable(
                data=df.to_dict('records'),
                page_size=6,
                columns=[{"name": i, "id": i} for i in df.columns],
                style_table={'overflowX': 'auto'},
                style_header={'backgroundColor': '#f8f9fa', 'fontWeight': 'bold'},
                style_cell={'textAlign': 'center', 'padding': '10px'},
                style_data={'backgroundColor': '#ffffff'},
                style_data_conditional=[
                    {
                        'if': {'row_index': 'odd'},
                        'backgroundColor': '#f2f2f2'
                    }
                ],
            )
        
                ]
            )
        ], className="mb-4"),

        html.Div([
            dcc.Graph(figure={}, id='controls-and-graph')
        ])
    ], className="container shadow p-4 mb-5 bg-white rounded")



# Callback
@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='stock-dropdown', component_property="value")  # 🔄 Changed ID
)
def update_graph(col_chosen):
    fig = px.line(df, x='Date', y=col_chosen, title=f"{col_chosen} Stock Price Over Time")
    return fig

if __name__ == '__main__':
    app.run(debug=True)
