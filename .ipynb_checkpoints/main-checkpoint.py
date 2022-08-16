from turtle import title
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from data import countries_df,total_df
from builder import make_table
from dash.dependencies import Input, Output

country_names = countries_df.sort_values("Country_Region").reset_index()
country_names = country_names["Country_Region"]

stylesheets = ["https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css",
 "https://fonts.googleapis.com/css2?family=Open+Sans&display=swap"]

app = Dash(__name__, external_stylesheets=stylesheets)

bubble_map = px.scatter_geo(countries_df, size="Confirmed", title="Confirmed By Country" ,color_continuous_scale=px.colors.sequential.Oryel , hover_name="Country_Region", color="Confirmed", locations="Country_Region", locationmode="country names", size_max=40, template="plotly_dark", hover_data={"Confirmed":":,2f", "Deaths":":,2f", "Recovered":":,2f", "Country_Region":False})

bars_graph = px.bar(total_df, x="condition" ,y="sum", hover_data={"sum":","},title="Total Global Cases", template="plotly_dark", labels={"condition":"Condition", "sum":"count", "color":"Condition"})
bars_graph.update_traces(marker_color=["#e74c3c", "#8e44ad","#27ae60"])



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
            style={"display":"grid", "gridTemplateColumns":"repeat(5, 1fr)", "gap":"50px", "marginTop":"50px"},
            children=[html.Div(style={"grid-column":"span 3"},children=[dcc.Graph(figure=bubble_map)]), html.Div(style={"grid-column":"span 2"},children=[make_table(countries_df.head())])
        ]),
        html.Div(
            style={"display":"grid", "gridTemplateColumns":"repeat(5, 1fr)", "gap":"50px"},
            children=[
                html.Div(style={"grid-column":"span 2"}, children=[dcc.Graph(figure=bars_graph)]),
                html.Div(
                    children=[
                        dcc.Dropdown(id="country", options=[{"label": name, "value": name} for name in country_names]),
                        html.H1(children="Hello anonymous", id="country-output")
                    ]
                )
                ], )
        ], 
    )




@app.callback(
    Output("country-output", "children"),
    [
        Input("country", "value")
    ]
)
def upadate_hello(value):
    if value is None:
        return "Hello Ananimous"
    else:
        return f"Hello {value}"

if __name__ == '__main__':
    app.run_server(debug=True)
