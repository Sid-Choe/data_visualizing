from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from data import countries_df
from builder import make_table

print(countries_df.columns)

stylesheets = ["https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css",
 "https://fonts.googleapis.com/css2?family=Open+Sans&display=swap"]

app = Dash(__name__, external_stylesheets=stylesheets)

app.layout = html.Div(
    style={
        "textAlign": "center", 
        "minHeight":"100vh", 
        "backgroundColor":"#111111", 
        "color":"white",
        "fontFamily": "Open Sans, sans-serif"
        },
    children = [
        html.Header(
            style={"text_Aling":"center", "paddingTop": "50px"}, 
            children=[html.H1("Corona Dashboard", style={"fontSize": "40px"})]
            ),
        html.Div(
            children=[
                make_table(countries_df)
            ]
        )
        ], 
    )

if __name__ == '__main__':
    app.run_server(debug=True)
