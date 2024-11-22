#https://aac-mi-sim.onrender.com

import dash
from dash import Dash,dcc, html, Input, Output, State,no_update
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np


from config import box_shadow
from config import chart_bg_space_style

# Initialize Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server=app.server


# Load the CSV data and dictionaries
data = pd.read_csv('vehicle_data.csv',index_col=False)

# Convert all columns in the DataFrame to numeric, with non-numeric entries set as NaN
data = data.apply(pd.to_numeric, errors='coerce')

month_dict = {'July': 1, 'August': 2, 'September': 3, 'October': 4}
visit_dict = {'1st Visit': 1, '2nd Visit': 2}
model_dict = {
    'Land Cruiser': 1, 'Coolray': 2, 'Accord': 3, 'RAV4': 4, 'Expedition': 5,
    'Territory': 6, 'Sonata': 7, 'Seltos': 8, 'Camry': 9, 'Tucson': 10,
    'Rush': 11, 'Altima': 12, 'Kicks': 13, 'X-Trail': 14, 'Patrol': 15
}
segment_dict = {'Seg D': 1, 'SUV B': 2, 'SUV C': 3, 'SUV F': 5}

# Apply dictionary mappings for dropdowns
data['Month'] = data['Month'].map({v: k for k, v in month_dict.items()})
data['Visit'] = data['Visit'].map({v: k for k, v in visit_dict.items()})
data['Model'] = data['Model'].map({v: k for k, v in model_dict.items()})
data['Segment'] = data['Segment'].map({v: k for k, v in segment_dict.items()})

#data.to_csv('Out.csv')



# Layout
app.layout =  dbc.Container([
    html.Div([
        dbc.Row([
            dbc.Col([html.Img(src='assets/DG_Logo.png', height="75px")], width=2),
            dbc.Col([html.H1("")], width=2),
            dbc.Col([html.H1("Vehicle EMI Calculator")], width=4),
            dbc.Col([html.H1("")], width=2),
            dbc.Col([html.H1("")], width=2),
            #dbc.Col([html.Img(src='assets/DG_Logo.png', height="75px",style={"float": "right"})], width=2),
        ]),
        dbc.Row([html.Hr()]),
    ]),
    html.Div([
        dbc.Row([
            dbc.Col([    
                html.Div([
                html.Label("MONTH(S):"),
                dbc.Row([dcc.Dropdown(id='month', options=[{'label': k, 'value': k} for k in month_dict.keys()], multi=True, placeholder="Select Month(s)"),]),
                html.Label("VISIT(S):"),
                dbc.Row([dcc.Dropdown(id='visit', options=[{'label': k, 'value': k} for k in visit_dict.keys()], multi=True, placeholder="Select Visit(s)"),]),
                html.Label("SEGMENT:"),
                dbc.Row([dcc.Dropdown(id='segment', options=[{'label': k, 'value': k} for k in segment_dict.keys()], placeholder="Select Segment"),]),
                html.Label("MODEL:"),                
                dbc.Row([dcc.Dropdown(id='model', placeholder="Select Model"),]),
                html.Label("LOAN TENURE:"),                
                dbc.Row([dcc.Dropdown(id='loan_tenure', options=[{'label': '3 Years', 'value': 3}, {'label': '5 Years', 'value': 5}], placeholder="Loan Tenure (Years)"),]),
                html.Label("DOWN PAYMENT:"),                
                dbc.Row([dcc.Dropdown(id='downpayment', options=[{'label': '0%', 'value': 0}, {'label': '10%', 'value': 0.1}, {'label': '20%', 'value': 0.2}],  placeholder="Downpayment %"),]),
                dbc.Row([html.Label("Vehicle Price:"),dcc.Input(id='vehicle_price', type='number', placeholder="Vehicle Retail Price"),]),
                dbc.Row([html.Label("Int Rate:"),dcc.Input(id='interest_rate', type='number', placeholder="Interest Rate (%)"),]),
                dbc.Row([html.Label("Discount Amount:"),dcc.Input(id='discount', type='number', placeholder="Discount"),]),
                dbc.Row([html.Label("Processing Fees:"),dcc.Input(id='processing_fee', type='number', placeholder="Processing Fees"),]),
                html.Hr(),
                dbc.Row([dbc.Button('Submit', id='submit-button', n_clicks=0,),], justify="center"),
                ], style=box_shadow),
            ],width=6),
            dbc.Col([    
                html.Div(id='output')    
            ]),    
        ]),  
    ]),
     
   
],fluid=True)

# Callback to update Model dropdown based on Segment selection
@app.callback(
    Output('model', 'options'),
    Input('segment', 'value')
)
def update_model_dropdown(segment_val):
    if segment_val == 'Seg D':
        model_options = [{'label': 'Altima', 'value': 'Altima'},{'label': 'Accord', 'value': 'Accord'},{'label': 'Sonata', 'value': 'Sonata'},{'label': 'Camry', 'value': 'Camry'},]
    elif segment_val == 'SUV B':
        model_options = [{'label': 'Kicks', 'value': 'Kicks'},{'label': 'Coolray', 'value': 'Coolray'},{'label': 'Seltos', 'value': 'Seltos'},{'label': 'Rush', 'value': 'Rush'},]
    elif segment_val == 'SUV C':
        model_options = [{'label': 'X-Trail', 'value': 'X-Trail'},{'label': 'RAV4', 'value': 'RAV4'},{'label': 'Territory', 'value': 'Territory'},{'label': 'Tucson', 'value': 'Tucson'},]
    elif segment_val == 'SUV F':
        model_options = [{'label': 'Patrol', 'value': 'Patrol'},{'label': 'Land Cruiser', 'value': 'Land Cruiser'},{'label': 'Expedition', 'value': 'Expedition'},]
    else:
        model_options = []
        
    return model_options

# Callback to update vehicle-related values based on model, month, and visit
@app.callback(
    Output('vehicle_price', 'value'),
    Output('interest_rate', 'value'),
    Input('model', 'value'),
    Input('month', 'value'),
    Input('visit', 'value')
)
def update_values_from_model(selected_model, months, visits):
    if selected_model and months and visits:
        filtered_data = data[(data['Model'] == selected_model) & 
                             (data['Month'].isin(months)) & 
                             (data['Visit'].isin(visits))]
        avg_price = filtered_data['Dealer_Price'].mean() if not filtered_data.empty else 0
        avg_interest = filtered_data['Interest_Rate'].mean() if not filtered_data.empty else 0
        #print(avg_price)
        #print(avg_interest)
    else:
        avg_price, avg_interest = 0, 0

    return avg_price, avg_interest

# Callback to calculate EMI and display output
@app.callback(
    Output('output', 'children'),    
    Input('submit-button', 'n_clicks'),
    State('vehicle_price', 'value'),
    State('discount', 'value'),
    State('interest_rate', 'value'),
    State('loan_tenure', 'value'),
    State('downpayment', 'value'),
    State('processing_fee', 'value')
)
def calculate_emi(n_clicks,vehicle_price, discount, interest_rate, loan_tenure, downpayment, processing_fee):

    if n_clicks == 0:
        return no_update
    
    if vehicle_price is None or discount is None or interest_rate is None or loan_tenure is None or downpayment is None or processing_fee is None : 
        return [html.P("All Values requried to calculate EMI"),]
    
    # Ensure defaults if any input is None
    discount = discount or 0
    vehicle_price = vehicle_price or 0
    interest_rate = interest_rate or 0
    downpayment = downpayment or 0
    processing_fee = processing_fee or 0

    # Transactional Price Calculation
    transactional_price = vehicle_price - discount
    downpayment_amount = transactional_price * downpayment
    finance_amount = transactional_price - downpayment_amount + processing_fee

    # EMI Calculation
    monthly_rate = interest_rate / 100 / 12
    num_payments = loan_tenure * 12
    emi_monthly = finance_amount * (monthly_rate * (1 + monthly_rate) ** num_payments) / ((1 + monthly_rate) ** num_payments - 1)
    total_paid = emi_monthly * num_payments
    actual_price = total_paid

    

    # Display results
    result =html.Div( [
        html.P(f"Transactional Price: {transactional_price:.2f}"),
        html.P(f"Total Finance Amount: {finance_amount:.2f}"),
        html.P(f"Amount to be paid to bank in {loan_tenure} years: {total_paid:.2f}"),
        html.P(f"EMI Monthly: {emi_monthly:.2f}"),
        html.P(f"Actual Price of the Car: {actual_price:.2f}")
    ],style=chart_bg_space_style)

    return result

if __name__ == '__main__':
    app.run_server(debug=True)
