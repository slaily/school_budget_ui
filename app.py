# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_html_components as html
import pandas as pd
import dash_table
import dash_bootstrap_components as dbc

from dash import Input, Output, html, State
import dash_bootstrap_components as dbc


fte_input = dbc.Row(
    [
        dbc.Label("FTE", html_for="fte-input"),
        dbc.Col(
            dbc.Input(
                id="fte-input", 
                type="number", 
                step="any",
                placeholder="Enter FTE"
            ),
            width=10,
        ),
    ],
    className="mb-3",
)
facility_or_department_input = dbc.Row(
    [
        dbc.Label("Facility or Department", html_for="facility-or-department-input"),
        dbc.Col(
            dbc.Input(
                id="facility-or-department-input",
                type="text",
                placeholder="Enter facility or department",
            ),
            width=10,
        ),
    ],
    className="mb-3",
)
function_description_input = dbc.Row(
    [
        dbc.Label("Function Description", html_for="function-description-input"),
        dbc.Col(
            dbc.Input(
                id="function-description-input",
                type="text",
                placeholder="Enter function description",
            ),
            width=10,
        ),
    ],
    className="mb-3",
)
fund_description_input = dbc.Row(
    [
        dbc.Label("Fund Description", html_for="fund-description-input"),
        dbc.Col(
            dbc.Input(
                type="text",
                id="fund-description-input",
                placeholder="Enter fund description",
            ),
            width=10,
        ),
    ],
    className="mb-3",
)
job_title_description_input = dbc.Row(
    [
        dbc.Label("Job Title Description", html_for="job-title-description-input"),
        dbc.Col(
            dbc.Input(
                type="text",
                id="job-title-description-input",
                placeholder="Enter job title description",
            ),
            width=10,
        ),
    ],
    className="mb-3",
)
location_description_input = dbc.Row(
    [
        dbc.Label("Location Description", html_for="location-description-input"),
        dbc.Col(
            dbc.Input(
                type="text",
                id="location-description-input",
                placeholder="Enter location description",
            ),
            width=10,
        ),
    ],
    className="mb-3",
)
object_description_input = dbc.Row(
    [
        dbc.Label("Object Description", html_for="object-description-input"),
        dbc.Col(
            dbc.Input(
                type="text",
                id="object-description-input",
                placeholder="Enter object description",
            ),
            width=10,
        ),
    ],
    className="mb-3",
)
position_extra_input = dbc.Row(
    [
        dbc.Label("Position Extra", html_for="position-extra-input"),
        dbc.Col(
            dbc.Input(
                type="text",
                id="position-extra-input",
                placeholder="Enter position extra",
            ),
            width=10,
        ),
    ],
    className="mb-3",
)
program_description_input = dbc.Row(
    [
        dbc.Label("Program Description", html_for="program-description-input"),
        dbc.Col(
            dbc.Input(
                type="text",
                id="program-description-input",
                placeholder="Enter program description",
            ),
            width=10,
        ),
    ],
    className="mb-3",
)
subfund_description_input = dbc.Row(
    [
        dbc.Label("Sub Fund Description", html_for="subfund-description-input"),
        dbc.Col(
            dbc.Input(
                type="text",
                id="subfund-description-input",
                placeholder="Enter subfund description",
            ),
            width=10,
        ),
    ],
    className="mb-3",
)
sub_object_description_input = dbc.Row(
    [
        dbc.Label("Sub Object Description", html_for="sub-object-description-input"),
        dbc.Col(
            dbc.Input(
                type="text",
                id="sub-object-description-input",
                placeholder="Enter sub object description",
            ),
            width=10,
        ),
    ],
    className="mb-3",
)
text_1_input = dbc.Row(
    [
        dbc.Label("Text 1", html_for="text-1-input"),
        dbc.Col(
            dbc.Input(
                type="text",
                id="text-1-input",
                placeholder="Enter text 1",
            ),
            width=10,
        ),
    ],
    className="mb-3",
)
text_2_input = dbc.Row(
    [
        dbc.Label("Text 2", html_for="text-2-input"),
        dbc.Col(
            dbc.Input(
                type="text",
                id="text-2-input",
                placeholder="Enter text 2",
            ),
            width=10,
        ),
    ],
    className="mb-3",
)
text_3_input = dbc.Row(
    [
        dbc.Label("Text 3", html_for="text-3-input"),
        dbc.Col(
            dbc.Input(
                type="text",
                id="text-3-input",
                placeholder="Enter text 3",
            ),
            width=10,
        ),
    ],
    className="mb-3",
)
text_4_input = dbc.Row(
    [
        dbc.Label("Text 4", html_for="text-4-input"),
        dbc.Col(
            dbc.Input(
                type="text",
                id="text-4-input",
                placeholder="Enter text 4",
            ),
            width=10,
        ),
    ],
    className="mb-3",
)
total_input = dbc.Row(
    [
        dbc.Label("Total", html_for="total-input"),
        dbc.Col(
            dbc.Input(
                id="total-input", 
                type="number", 
                step="any",
                placeholder="Enter total"
            ),
            width=10,
        ),
    ],
    className="mb-3",
)
form = dbc.Form(
    [
        fte_input, 
        facility_or_department_input, 
        function_description_input,
        fund_description_input,
        job_title_description_input,
        location_description_input,
        object_description_input,
        position_extra_input,
        program_description_input,
        subfund_description_input,
        sub_object_description_input,
        text_1_input,
        text_2_input,
        text_3_input,
        text_4_input,
        total_input,
    ]
)
# csv_path = "datasets/TrainingData.csv"
# df = pd.read_csv(csv_path, index_col=0, nrows=5)
# Main App
# Define app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
# Define Layout
app.layout = html.Div(
    dbc.Container(
        fluid=True,
        children=[
            dbc.Navbar(
                dbc.Container(
                    [
                        html.A(
                            # Use row and col to control vertical alignment of logo / brand
                            dbc.Row(
                                [
                                    dbc.Col(html.Img(src=app.get_asset_url("school.png"), height="30px")),
                                    dbc.Col(dbc.NavbarBrand("School Budget", className="ms-2")),
                                ],
                                align="center",
                                className="g-0",
                            ),
                            href="/",
                            style={"textDecoration": "none"},
                        ),
                    ]
                ),
             ),
            html.Div(
                [
                    html.Br(),
                    html.P(
                        "Budgets for schools are huge, complex, and not standartized.",
                        className="lead",
                    ),
                    html.P(
                        "Hundreds of hours each year are spent manually labelling.",
                        className="lead",
                    ),
                    html.Img(src=app.get_asset_url("budget.png"), height="30px"),
                ],
                style={'textAlign': 'center'}
            ),
            html.Br(),
            html.Div(
                [
                    form,
                ],
                style=dict(display='flex', justifyContent='center')
            ),
            html.Div(
                [
                    dbc.Button(
                        "Classify Line Item",
                        id="example-button",
                        color="success",
                        className="me-1"
                    ),
                    html.Span(id="example-output", style={"verticalAlign": "middle"}),
                ],
                style=dict(display='flex', justifyContent='center')
            ),
        ],
        style={"margin": "auto"},
    )
)


@app.callback(
    Output("example-output", "children"),
    [
        Input("example-button", "n_clicks"),
        Input("fte-input", "value"),
        Input("facility-or-department-input", "value"),
        Input("function-description-input", "value"),
        Input("job-title-description-input", "value"),
        Input("location-description-input", "value"),
        Input("object-description-input", "value"),
        Input("position-extra-input", "value"),
        Input("program-description-input", "value"),
        Input("subfund-description-input", "value"),
        Input("sub-object-description-input", "value"),
        Input("text-1-input", "value"),
        Input("text-2-input", "value"),
        Input("text-3-input", "value"),
        Input("text-4-input", "value"),
        Input("total-input", "value"),
    ]
)
def on_button_click(
    *args
):
    print(args)
    if args is None:
        return "Not clicked."
    else:
        return f"Clicked {args} times."


if __name__ == '__main__':
    app.run_server(debug=True)
